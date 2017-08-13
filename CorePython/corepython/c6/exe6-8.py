from os.path import dirname
from twisted.web import server, resource
from twisted.internet import reactor, endpoints
from sqlalchemy import Column, Integer, String, create_engine, exc, orm
from sqlalchemy.ext.declarative import declarative_base

PORT = 8080
DBNAME = 'pymysql'
FIELDS = ('login', 'userid', 'projid')
DSNs = {  # Database Source Names
    'mysql': 'mysql://root:686713@localhost/%s' % DBNAME
}


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    login = Column(String(64))
    userid = Column(Integer, primary_key=True)
    projid = Column(Integer)


class UserService(object):
    def __init__(self, dsn):
        try:
            eng = create_engine(dsn)  # echo=True for debugging purposes.
        except ImportError:
            raise RuntimeError()

        try:
            eng.connect()
        except exc.OperationalError:
            eng = create_engine(dirname(dsn))
            eng.execute('CREATE DATABASE %s' % DBNAME).close()
            eng = create_engine(dsn)

        Session = orm.sessionmaker(bind=eng)
        self.ses = Session()
        self.users = Users.__table__
        self.eng = self.users.metadata.bind = eng

    def get_users(self):
        return self.ses.query(Users).all()


class UserTableResource(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        return get_user_table_html()


def get_user_table_inner_html(users):
    return "<tr>%s</tr>%s" % (''.join("<th>%s</th>" % f for f in FIELDS),
                              ''.join("<tr><td>%s</td><td>%d</td><td>%d</td></tr>" % (u.login, u.userid, u.projid)
                                      for u in users))


def get_user_table_html():
    user_service = UserService(DSNs['mysql'])
    users = user_service.get_users()
    return "<html><table border=\"1\" cellspacing=\"0\">%s</table></html>" % get_user_table_inner_html(users)

site = server.Site(UserTableResource())
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8080)
endpoint.listen(site)
reactor.run()
