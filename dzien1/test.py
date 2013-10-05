#print(1,2,3)

def quniversal (*args, **kwargs):
    print(args, kwargs)


quniversal("ola", "Ala")
quniversal("ola", "Ala", a=123, data=32343)
