import copy

# abstract class bag


class Bag:
    def add(self, x):
        """for adding any number of items to the bag"""
        pass

    def empty(self):
        """for taking all the items out of the bag and returning them as a list"""
        pass

    def count(self):
        """for counting the items which are currently in the bag"""
        pass

    def show(self):
        """for showing the items which are currently in the bag"""
        pass

# class Item


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# class ListBag


class ListBag(Bag):
    def __init__(self):
        self.bag_items = []

    def add(self, x):
        self.bag_items.append(x)

    def empty(self):
        t = copy.deepcopy(self.bag_items)
        self.bag_items.clear()
        return t

    def count(self):
        return len(self.bag_items)

    def show(self):
        return self.bag_items

# class DictBag


class DictBag(Bag):
    def __init__(self):
        self.bag_items = {}

    def add(self, x):
        self.bag_items[x.name] = x.value

    def empty(self):
        t = [Item(k, v) for k, v in self.bag_items.items()]
        self.bag_items.clear()
        return t

    def count(self):
        return len(self.bag_items)

    def show(self):
        return self.bag_items.items()


def repack_bags(bags):
    tot_items = []

    for i in bags:
        tot_items.extend(i.empty())

    for i in range(len(tot_items)):
        bags[i % len(bags)].add(tot_items[i])


def main():
    k = 0
    bags = [ListBag()]

    for i in range(20):
        bags[-1].add(Item(f'item{k}', k))
        k += 1

    bags.append(ListBag())
    for i in range(9):
        bags[-1].add(Item(f'item{k}', k))
        k += 1

    bags.append(DictBag())
    for i in range(5):
        bags[-1].add(Item(f'item{k}', k))
        k += 1

    repack_bags(bags)

    for i in range(len(bags)):
        print(f'Bag {i+1}: ', bags[i].count())


if __name__ == '__main__':
    main()
