#another version of the b.s
def recursive_binary_search(list,target):
    if len(list)==0:
        return False
    else:
        midpoint=(len(list)//2)
        if list[midpoint]==target:
            return True
        else:
            if list[midpoint]<target: #case less
                return recursive_binary_search(list[midpoint+1:],target)#the list has been sliced
            else:
                return recursive_binary_search(list[:midpoint],target) #slices from the beginning to the middle

def  verify(result):
    print("target found:",result)

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=recursive_binary_search(numbers,6)
verify(result)

