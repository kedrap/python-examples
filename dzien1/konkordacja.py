#file = open('/usr/lib/python3.2/LICENSE.txt')
#content = file.read()
#words = content.split()

out = {}
with open('/usr/lib/python3.2/LICENSE.txt') as f:
    for line in f:
        words = line.split()
        for word in words:
            word = word.lower().strip('.,!?')
            try:
                out[word] += 1
            except KeyError:
                out[word] = 1

rev = {}
for k, v in out.items():
    try:
        rev[v].append(k)
    except KeyError:
        rev[v] = [k]

for f in sorted(rev.keys()): #reverse=True):
    print(f, ":", rev[f])
