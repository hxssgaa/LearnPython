"""
Example of using explicit(Classical) form in SqlAlchemy

Remember that sessions and explicit operations are not tied together.
This is auto-commit, non-transactional.
"""

from os.path import dirname
from random import randrange as rand

from sqlalchemy import create_engine, exc, orm, MetaData, Table, Column, String, Integer

from ushuffle_sad import FIELDS, DBNAME, cformat, tformat, rand_name, NAMELEN

DSNs = {  # Database Source Names
    'mysql': 'mysql://root:686713@localhost/%s' % DBNAME
}


class SQLAlchemyTest(object):
    def __init__(self, dsn):
        try:
            eng = create_engine(dsn)  # echo=True for debugging purposes.
        except ImportError:
            raise RuntimeError()

        try:
            self.cxn = eng.connect()
        except exc.OperationalError:
            eng = create_engine(dirname(dsn))
            eng.execute('CREATE DATABASE %s' % DBNAME).close()
            eng = create_engine(dsn)

        metadata = MetaData()
        self.eng = metadata.bind = eng
        try:
            users = Table('users', metadata, autoload=True)
        except exc.NoSuchTableError:
            users = Table('users', metadata,
                          Column('login', String(NAMELEN)),
                          Column('userid', Integer),
                          Column('projid', Integer),
                          )
        self.users = users

    def insert(self):
        d = [dict(zip(FIELDS, [who, uid, rand(1, 5)])) for who, uid in rand_name()]
        return self.users.insert().execute(*d).rowcount

    def update(self):
        users = self.users
        fr = rand(1, 5)
        to = rand(1, 5)
        return fr, to, users.update(users.c.projid == fr).execute(projid=to).rowcount

    def delete(self):
        users = self.users
        rm = rand(1, 5)
        return rm, users.delete(users.c.projid == rm).execute().rowcount

    def db_dump(self):
        print('\n%s' % ''.join(map(cformat, FIELDS)))
        users = self.users.select().execute()
        for user in users.fetchall():
            print(''.join(map(tformat, (user.login, user.userid, user.projid))))

    def __getattr__(self, attr):
        """
        Use for drop/create, it's equivalent to call self.users.drop() or self.users.create()
        The usage is called delegation which delegate the missing attribute to another object in our instances.

        __getattr__() is only called whenever an attribute lookup fails.
        (This is as opposed to __getattribute__(), which is called, regardless.)
        """
        return getattr(self.users, attr)

    def finish(self):
        self.cxn.close()


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

    print('\n*** Move users to a random group')
    fr, to, num = model.update()
    print('\t(%d users moved) from (%d) to (%d)' % (num, fr, to))
    model.db_dump()

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
