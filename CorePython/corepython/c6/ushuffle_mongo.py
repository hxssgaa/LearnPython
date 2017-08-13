"""
Example of using adapters of MongoDB
"""

from random import randrange as rand

from pymongo import MongoClient, errors

from ushuffle_sad import FIELDS, DBNAME, cformat, tformat, rand_name

COLLECTION = 'users'


class MongoTest(object):
    def __init__(self):
        try:
            client = MongoClient()
        except errors.ConnectionFailure:
            raise RuntimeError()
        self.db = client[DBNAME]
        self.users = self.db[COLLECTION]

    def insert(self):
        self.users.insert(
            dict(login=who, userid=uid, projid=rand(1, 5)) for who, uid in rand_name()
        )

    def update(self):
        fr = rand(1, 5)
        to = rand(1, 5)
        res = self.users.update_many({'projid': fr}, {'$set': {'projid': to}})
        return fr, to, res.modified_count

    def delete(self):
        rm = rand(1, 5)
        res = self.users.delete_many({'projid': rm})
        return rm, res.deleted_count

    def db_dump(self):
        print('\n%s' % ''.join(map(cformat, FIELDS)))
        for user in self.users.find():
            print(''.join(map(tformat, (user[k] for k in FIELDS))))


def main():
    print('*** Connect to %r database' % DBNAME)
    try:
        model = MongoTest()
    except RuntimeError:
        print('\nERROR: MongoDB server unreachable, exit')
        return

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
    model.db.drop_collection(COLLECTION)
    print('\n*** Close cxns')


if __name__ == '__main__':
    main()
