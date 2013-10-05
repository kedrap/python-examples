try:
    #1/0
    a
except (ZeroDivisionError, NameError) as err:
    print(err)
else:
    print('no exceptions')
finally:
    print('Always')
