nested_list1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

nested_list2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

class FlatIteratoPresent:
    def __init__(self, lst):
        self.lst = sum(lst, [])
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.lst):
            raise StopIteration
        else:
            return self.lst[self.index]

def flat_generator_present(my_list):
    for lists in my_list:
        for item in lists:
            yield item

for item in FlatIteratoPresent(nested_list1):
    print(item)
flat_list = [item for item in FlatIteratoPresent(nested_list1)]
print(flat_list)

for item in flat_generator_present(nested_list2):
    print(item)

