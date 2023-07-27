from collections import defaultdict

def numDuplicates(name, price, weight):
    groups = defaultdict(int)

    for n, p, w in zip(name, price, weight):
        group = (n, p, w)
        groups[group] += 1
    print(groups)
    duplicate_counts = 0
    for count in groups.values():
        if count > 1:
            duplicate_counts = count - 1

    return duplicate_counts

# Example usage
names = ['ball', 'box', 'ball', 'ball', 'box']
prices = [2, 2, 2, 2, 2]
weights = [1, 2, 1, 1, 3]

result = numDuplicates(names, prices, weights)
print(result)
