counts = dict()
fhandle = open('mbox-short.txt')
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    words = words[2]
    counts[words] = counts.get(words,0) + 1
print(counts)
