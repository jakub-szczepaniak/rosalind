from itertools import zip_longest, permutations


class Node():
    def __init__(self, rosalind_id, data):
        self.id = rosalind_id
        self.data = data.strip()
        self.prefix = self.data[:3]
        self.sufix = self.data[-3:]

    def __repr__(self):
        return self.id

    def overlap(self, other):
        if other is None:
            return False
        return (self.sufix == other.prefix)


def grouper(iterable, size):
    args = [iter(iterable)] * size
    return zip_longest(*args)

def resolve(data_grid, result):
    if len(data_grid) > 0:
        first = data_grid.pop()
    else:
        return result
    for second in data_grid:
        if first.overlap(second):
            print("adding {} {}".format(first, second))
            result.add((first, second))
        elif second.overlap(first):
            result.add((second, first))
    return resolve(data_grid, result)
def main():
    data_grid = []
    rosalind_id = ''
    rosalind_string = ''

    with open('rosalind_grph.txt', 'r') as data:
        for line1, line2, line3 in zip_longest(*[data]*3):
            rosalind_id = line1.rstrip().lstrip('>')
            rosalind_string = line2.strip() + line3.strip()
            data_grid.append(Node(rosalind_id, rosalind_string))
    result = set()
    print("created data grid : {}".format(data_grid))
    print("calculating results")

    resolve(data_grid, result)
    # for permutation in data_grid:
    #     print(permutation)
    #     for first, second in grouper(permuation, 2):
    #         if first.overlap(second):
    #             result.add((first, second))
    print(len(result))
    with open('rosalind_grph.result.txt', 'w') as result_file:

        for first_id, second_id in result:
            result_file.write("{} {}\n".format(first_id, second_id))


if __name__ == "__main__":
    main()
