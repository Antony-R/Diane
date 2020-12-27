import json
cond = 1

try:
    with open('data.json','r') as f:
        data = json.load(f)
except:
    data = {}

while(cond):

    op = input("Enter the operation: create(c)/ edit(e)/ delete(d)/ get(g) - ")
    
    if op=='create' or op=='c':
        create_cond = 1
        while(create_cond):
            key = input("Enter the key: ")
            if key in data:
                print("Key name already exits. Enter some other key name ")
                continue
            value = input("Enter the value: ")
            data[key] = value
            create_cond = int(input("continue - 1, exit create - 0 - "))

    elif op=='edit' or op=='e':
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        del data[key]
        data[key] = value

    elif op=='delete' or op=='d':
        key = input("Enter the key: ")
        del data[key]

    elif op=='get' or op=='g':
        key = input("Enter the key: ")
        print(data[key])


    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

    cond = int(input("To continue enter 1, to exit enter 0 "))