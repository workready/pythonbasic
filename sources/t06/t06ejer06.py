class Item:
    pass    # Tu codigo aqui. Estos son los elementos a guardar en las cajas


class Box:
    pass    # Tu codigo aqui. Esta clase va a actuar como abstracta


class ListBox(Box):
    pass    # Tu codigo aqui


class DictBox(Box):
    pass    # Tu codigo aqui


# Esto prueba las clases
i1 = Item("Item 1", 1)
i2 = Item("Item 2", 2)
i3 = Item("Item 3", 3)

listbox = ListBox()
dictbox = DictBox()

listbox.add(i1, i2, i3)
dictbox.add(i1)
dictbox.add(i2)
dictbox.add(i3)

assert(listbox.count() == 3)
assert(dictbox.count() == 3)

for i in listbox.items():
    print(i)

for k, item in dictbox.items().items():
    print(i)

listbox.empty()
dictbox.empty()

assert(listbox.count() == 0)
assert(dictbox.count() == 0)

for i in listbox.items():
    print(i)
    
for k, item in dictbox.items().items():
    print(i)