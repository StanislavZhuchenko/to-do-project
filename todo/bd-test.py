import sqlite3

cur = sqlite3.connect('/Users/stanislav_zhucenko/PycharmProjects/thenewtodo/instance/tododb.sqlite')

# for row in cur.execute('''SELECT * FROM user'''):
#     print(row)

for row in cur.execute(
        "SELECT l.title, l.priority, l.user_id "
        "FROM list l "
        "JOIN user u ON l.user_id = u.id "
        "WHERE u.username = 'Admin' AND l.status = 'In progress' "
        "ORDER BY l.priority DESC"):
    print(row)


# cur.execute('''DELETE FROM user WHERE id == 3''')
# cur.commit()
# print(*cur.execute('''SELECT * FROM user''').fetchmany(3))

id = 12
cur_task = cur.execute(
        'SELECT * FROM list WHERE id = ?', (id, )
    ).fetchall()
print(cur_task)
