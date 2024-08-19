def bubbleSort(numbers):
    listanueva=[]
    while len(numbers)>0:
        box=None
        for i in numbers:
            if box==None or i<box:
                box=i
        listanueva.append(box)
        numbers.remove(box)
    return listanueva

print(bubbleSort([1,4,2,5,12,7]))
