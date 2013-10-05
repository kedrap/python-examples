import re

with open('//home/developer/Pulpit/hosts.txt') as f:
    for line in f:

        r = re.compile(r'(\w+)\.(\w+)@(.+)')
        m = r.match(line)
        if m:
            imie, nazwisko, host = m.groups()
            print("{:>10} {:>10} {:>20}".format(imie,
                                                nazwisko,
                                                host))
