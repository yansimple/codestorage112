import shelve
db = shelve.open('db_item.txt')
print('db is open')

items = list(db.keys())
print(items)

print(db['1'])


db.close
