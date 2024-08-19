def mergeTwoLists(list1,list2):
    lista3=list1+list2
    newlist=[]
    while len(lista3)>0:
        caja=None
        for i in lista3:
            if caja==None or i<caja:
                caja=i
        newlist.append(caja)
        lista3.remove(caja)
    return newlist

print(mergeTwoLists([],[5,4,6]))
