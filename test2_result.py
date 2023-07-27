def numDuplicates(name, price, weight):
 # Write your code here
    s = set()
    for i in range(len(name)):
        s.add(name[i] + ' ' + str(price[i]) + ' ' +str(weight[i]))
        print(s)
    return len(name) - len(s)




names = ['ball', 'box', 'ball', 'ball', 'box']
prices = [2, 2, 2, 2, 2]
weights = [1, 2, 1, 1, 3]

result = numDuplicates(names, prices, weights)
print(result)