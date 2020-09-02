import shelve
key = input(':')
key = str(key)
databese = shelve.open('db_item.txt')
print('db is open')
if key in databese.keys():
    print("already in db")
    element = input("element name :")
    databese[key] = element
    element = databese[key]
    databese.close()
    databese = shelve.open('db_item.txt','r')
    print(element)

else:
    print(key,' add in db')
    element = input("element name :")
    databese[key] = element
    element = databese[key]
    databese.close()
    databese = shelve.open('db_item.txt','r')
    print(element)
    databese.close()
databese = shelve.open('db_item.txt')
databese.keys() = items
items = databese.keys()
print(items)
databese.close()

print("end")