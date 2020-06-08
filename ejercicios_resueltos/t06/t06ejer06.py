class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return "{} => {}".format(self.name, self.value)

class Box:
    def add(self, *items):
        raise NotImplementedError()

    def empty(self):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

    def items(self):
        raise NotImplementedError()


class ListBox(Box):
    def __init__(self):
        self._items = []

    def add(self, *items):
        self._items.extend(items)

    def empty(self):
        items = self._items
        self._items = []
        return items

    def count(self):
        return len(self._items)

    def items(self):
        return self._items


class DictBox(Box):
    def __init__(self):
        self._items = {}

    def add(self, *items):
        self._items.update(dict((i.name, i) for i in items))

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def count(self):
        return len(self._items)

    def items(self):
        return self._items



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