counts = dict()
fhandle = open('words.txt')
for word in fhandle:
    words = word.split()
    print(words)
    for line in words:
        counts[line] = counts.get(line,0) + 1
    
