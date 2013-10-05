with open('//home/developer/Pulpit/hosts.txt') as f:
    for line in f:
        host = line.split('@')
        name = host[0].split('.')
        print(name[0], name[1], host[1])
        name, host = line.split('@')
        imie, nazwisko = name.split('.')

        print("{:>10} {:>10} {:>20}".format(imie,
                                            nazwisko,
                                            host))
