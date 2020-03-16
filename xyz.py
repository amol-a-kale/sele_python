contacts_list = [{'firstname': 'Tom', 'lastname': 'Cruise', 'email': 'tomcruise@hollywood.com'},
                 {'firstname': 'Bruce', 'lastname': 'Wayne', 'email': 'brucewayne@hollywood.com'},
                 {'firstname': 'Sherlocks', 'lastname': 'Homes', 'email': 'tonystark@hollywood.com'}]

for i in range(0, len(contacts_list)):
    print(contacts_list[i].values())
    value = list(contacts_list[i].values())
    #print(value[0],value[2])

