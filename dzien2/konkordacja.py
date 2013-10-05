freq = {}

with open('/usr/lib/python3.3/LICENSE.txt') as f:
    for line in f:
        words = line.split()
        for word in words:
            word = word.lower().strip('.,!?')
            try:
                freq[word] += 1
            except KeyError:
                freq[word] = 1

    rev = {}
    for k, v in freq.items():
        try:
            rev[v].append(k.lower())
        except KeyError:
            rev[v] = [k.lower()]

    for f in sorted(rev.keys(), reverse=True):
        print(f, ":", rev[f])




#file = open('/usr/lib/python3.3/LICENSE.txt')
#content = file.read()
#words = content.split()
#
#out = {}
#for word in words:
#    word = word.lower().strip('.,!?')
#    #out[word] = out.get(word,0)+1
#    try:
#        out[word] +=1
#    except KeyError:
#        out[word] = 1
#
#rev = {}
#for k,v in out.items():
#    try:
#        rev[v].append(k.lower())
#    except KeyError:
#        rev[v] = [k.lower()]
#
#
#for f in sorted(rev.keys(), reverse=True):
#    print(f, ":", rev[f])
