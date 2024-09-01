def bottles(x):
    bottles=x
    for i in range(bottles):
        print(str(bottles)+' of beer on the wall')
        print(str(bottles)+' bottles of beer,')
        print('Take one down,')
        print('Pass it around,')
        print(str(bottles-1)+' bottles of beer on the wall,')
        bottles-=1
    print('No more bottles of beer on the wall!')   
bottles(4)  
