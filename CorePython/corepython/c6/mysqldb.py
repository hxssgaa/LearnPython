import MySQLdb

# Create pymysql database
cxn = MySQLdb.connect(user='root', passwd='686713', db='pymysql')
cur = cxn.cursor()
# cxn.query('CREATE DATABASE pymysql')
# cxn.query("GRANT ALL ON test.* to ''@'localhost'")
# cxn.commit()
# cxn.close()

# Create users table, and insert some data to the table.
# cur.execute('CREATE TABLE users(login VARCHAR(8), userid INT)')
cur.execute("INSERT INTO users VALUES('john', 7000)")
cur.execute("INSERT INTO users VALUES('jane', 7001)")
cur.execute("INSERT INTO users VALUES('bob', 7200)")

# Select data from the user table
print(cur.execute("SELECT * FROM users WHERE login LIKE 'j%'"))
for data in cur.fetchall():
    print('%s\t%s' % data)

# Updating some data from the user table
print(cur.execute("UPDATE users SET userid=7100 WHERE userid=7001"))
print(cur.execute("SELECT * FROM users"))
for data in cur.fetchall():
    print('%s\t%s' % data)

# Commit the result and close cursor and connection
cur.close()
cxn.commit()
cxn.close()
