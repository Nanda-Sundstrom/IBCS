with open('test.txt') as f:
    for line in f:
       print([len(word) for word in line.split()])
       