import pickle

a = ('ala', 'ma kota')
print(a)

file = open('pickle.txt', 'w')
p = pickle.dumps(a, file)



exit(1)

#import csv
#
#
#r = csv.reader()


import re

r = re.compile(r'(\w*)\.(\w*)\@(.+)')
with open('hosts.txt') as file:
    for line in file:
        m = r.search(line.strip())
        if m:
            firstName, lastName, domain = m.groups()
            print('{fn:>10} {ln:<10} @ {dn}'.format(fn = firstName, ln = lastName, dn = domain))


#with open('hosts.txt') as file:
#    for line in file:
#        user, domain = line.strip().split('@')
#        firstName, lastName = user.strip().split('.')
#
#        print('{fn:>10} {ln:<10} @ {dn}'.format(fn = firstName, ln = lastName, dn = domain))


#with open('hosts.txt') as file:
#    for line in file:
#        parts1 = line.strip().split('@')
#        user = parts1[0]
#        domain = parts1[1]
#
#        parts2 = user.split('.')
#        firstName = parts2[0]
#        lastName = parts2[1]
#
#        print('{fn} {ln} @ {dn}'.format(fn = firstName, ln = lastName, dn = domain))
