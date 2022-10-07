#python code to demonstrate the use of linear search
def linear_search(list,target):
    #returns the index position of target if found else returns none
    for i in range(0,len(list)):#len(method has constant time complexity)
        if list[i]==target:
           return i
    return None
#averification function
def verify(index):
    if index is not  None:
        print("target found at index ",index)
    else:
        print('target not found in the list')


numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=linear_search(numbers, 12)
verify(result)


print('#############')
newResult=linear_search(numbers,6)
verify(newResult)

###########new test using a list
print('$$$$$$$$$$$$$$$$')
def lnr_search(list,target_val):#names-name of string list
    for index in range(0,len(list)):
        if list[index]==target_val:
            return index
    return None #none is a keyword in python

def search_verification(index): #alternative for verify
    pass
    if index is not None:
        print(f"found  at index :", index)
    else:
        print('target not found.')


strList=['james','Allen','Moore','Ross','Derrick','Thomas']

solution=lnr_search(strList, 'Ross')
search_verification(solution)#finds the index of the solution




