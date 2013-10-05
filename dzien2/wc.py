res = {'lc': 0, 'wc': 0, 'cc': 0}

with open('/usr/lib/python3.3/LICENSE.txt', 'br') as file:
    for line in file:
        res['lc'] += 1
        res['wc'] += len(line.split())
        res['cc'] += len(line)

#with open('/usr/lib/python3.3/LICENSE.txt') as file:
#    for line in file:
#        lc += 1;
#
#        words = line.split()
#        for word in words:
#            word = word.lower().strip('.,!?')
#            wc += 1
#
#            for char in word:
#                q = char.encode('utf-8')
#                print(q)
#                cc += 1

print('lines={lc}, words={wc}, chars={cc}'.format(**res))
