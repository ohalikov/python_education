def ChangeDict(D):
    D['A'] = 100
    D['C'] = 200
    print('ChangeDict.D = ', D)


DD = {'A': 5, 'B': 10, 'C': 20}

print('DD = ', DD)

ChangeDict(DD)

print('DD = ', DD)
