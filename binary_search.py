def binary_search(list,target):
    first=0
    last=len(list)-1#index begin at zero

    while first<=last:
        midpoint=(first+last)//2 #//for floor div (round down vlaues
        if list[midpoint]==target:
            return midpoint
        elif list[midpoint]<target:
            first=midpoint+1
        else:
            last=midpoint-1
    return None

def verify(index):
    if index is not None:
        print("target found at index ",index)
    else:
        print('target not found in the list')

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #list has to be sorted in the case of binary search
result=binary_search(numbers, 12)
verify(result)
