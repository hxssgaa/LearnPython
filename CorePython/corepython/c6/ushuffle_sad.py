"""Example of using declarative layer in SqlAlchemy"""

import random
from os.path import dirname
from random import randrange as rand
from timeit import timeit

from sqlalchemy import Column, Integer, String, create_engine, exc, orm
from sqlalchemy.ext.declarative import declarative_base

COLSIZ = 10
FIELDS = ('login', 'userid', 'projid')
DBNAME = 'pymysql'
DBUSER = 'root'
DB_EXC = None
NAMELEN = 16
NAMES = (
    ('aaron', 8312), ('angela', 7603), ('dave', 7306),
    ('davina', 7902), ('elliot', 7911), ('ernie', 7410),
    ('jess', 7912), ('jim', 7512), ('larry', 7311),
    ('leslie', 7808), ('melissa', 8602), ('pat', 7711),
    ('serena', 7003), ('stan', 7607), ('faye', 6812),
    ('amy', 7209), ('mona', 7404), ('jennifer', 7608),
)


def tformat(s): return str(s).title().ljust(COLSIZ)


def cformat(s): return s.upper().ljust(COLSIZ)


DSNs = {  # Database Source Names
    'mysql': 'mysql://root:686713@localhost/%s' % DBNAME
}


def rand_name():
    pick = set(NAMES)
    while pick:
        yield pick.pop()


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    login = Column(String(64))
    userid = Column(Integer, primary_key=True)
    projid = Column(Integer)

    def __str__(self):
        return ''.join(map(tformat,
                           (self.login, self.userid, self.projid)))


class SQLAlchemyTest(object):
    def __init__(self, dsn):
        try:
            eng = create_engine(dsn)  # echo=True for debugging purposes.
        except ImportError:
            raise RuntimeError()

        try:
            eng.connect()
        except exc.OperationalError:
            eng = create_engine(dirname(dsn))
            try:  # The following code would also throw the same exc.OperationalError.
                eng.execute('CREATE DATABASE %s' % DBNAME).close()
            except exc.OperationalError:
                raise RuntimeError()
            eng = create_engine(dsn)

        Session = orm.sessionmaker(bind=eng)  # Session is not thread safe.
        self.ses = Session()
        self.users = Users.__table__
        self.eng = self.users.metadata.bind = eng

    def insert(self):
        self.ses.add_all(
            Users(login=who, userid=userid, projid=rand(1, 5))
            for who, userid in rand_name()
        )
        self.ses.commit()

    def update_slow(self):
        """
        Deprecated usage of updating, because it update row one by one.
        """
        fr = rand(1, 5)
        to = random.sample(set(i for i in xrange(1, 5) if i != fr), 1)[0]  # Avoiding moving users into the same group
        i = -1
        users = self.ses.query(Users).filter_by(projid=fr).all()
        for i, user in enumerate(users):
            user.projid = to
        # self.ses.commit()
        return fr, to, i + 1

    def delete_slow(self):
        """
        Deprecated usage of deleting, because it delete row one by one.
        """
        rm = rand(1, 5)
        while self.ses.query(Users).filter_by(projid=rm).count() == 0:  # Avoiding removing a group which has no users.
            rm = rand(1, 5)
        i = -1
        users = self.ses.query(Users).filter_by(projid=rm).all()
        for i, user in enumerate(users):
            self.ses.delete(user)
        # self.ses.commit()
        return rm, i + 1

    def update(self):
        fr = rand(1, 5)
        to = random.sample(set(i for i in xrange(1, 5) if i != fr), 1)[0]  # Avoiding moving users into the same group
        res = self.ses.query(Users).filter_by(projid=fr).update({Users.projid: to})
        # self.ses.commit()
        return fr, to, res

    def delete(self):
        rm = rand(1, 5)
        while self.ses.query(Users).filter_by(projid=rm).count() == 0:  # Avoiding removing a group which has no users.
            rm = rand(1, 5)
        res = self.ses.query(Users).filter_by(projid=rm).delete()
        # self.ses.commit()
        return rm, res

    def db_dump(self, newest5=False):
        print('\n%s' % ''.join(map(cformat, FIELDS)))
        # Use slicing index is more pythonic way to use limit and offset.
        users = self.ses.query(Users).order_by(Users.userid.desc())[:5] if newest5 else \
            self.ses.query(Users).all()
        for user in users:
            print(user)
        self.ses.commit()

    def __getattr__(self, attr):
        """
        Use for drop/create, it's equivalent to call self.users.drop() or self.users.create()
        The usage is called delegation which delegate the missing attribute to another object in our instances.

        __getattr__() is only called whenever an attribute lookup fails.
        (This is as opposed to __getattribute__(), which is called, regardless.)
        """
        return getattr(self.users, attr)

    def finish(self):
        self.ses.connection().close()


def main():
    print('*** Connect to %r database' % DBNAME)
    db = 'mysql'
    if db not in DSNs:
        print('\nERROR: %r not supported, exit' % db)
        return
    try:
        model = SQLAlchemyTest(DSNs[db])
    except RuntimeError:
        print('\nERROR: %r not supported, exit' % db)
        return
    print('\n*** Create users table (drop old one if appl.)')
    model.drop(checkfirst=True)
    model.create()

    print('\n*** Insert names into table')
    model.insert()
    model.db_dump()

    print('\n*** Top 5 newest employees')
    model.db_dump(True)

    print('\n*** Move users to a random group')

    fr, to, num = model.update()
    print('\t(%d users moved) from (%d) to (%d)' % (num, fr, to))
    model.db_dump()

    print('\n*** Update_slow() costs time:%s' % timeit('model.update_slow()',
                                                       setup='from ushuffle_sad import SQLAlchemyTest,DSNs\n'
                                                             'db = "mysql"\nmodel = SQLAlchemyTest(DSNs[db])',
                                                       number=100))

    print('\n*** Update() costs time:%s' % timeit('model.update()',
                                                  setup='from ushuffle_sad import SQLAlchemyTest,DSNs\n'
                                                        'db = "mysql"\nmodel = SQLAlchemyTest(DSNs[db])',
                                                  number=100))

    print('\n*** Randomly delete group')
    rm, num = model.delete()
    print('\t(group #%d; %d users removed)' % (rm, num))
    model.db_dump()

    print('\n*** Drop users table')
    model.drop()
    print('\n*** Close cxns')
    model.finish()


if __name__ == '__main__':
    main()
