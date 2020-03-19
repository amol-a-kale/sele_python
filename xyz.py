list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john',2.23]

# comparing value of two list
for item in list:
    for item1 in tinylist:
        if item == item1:
            print(item)