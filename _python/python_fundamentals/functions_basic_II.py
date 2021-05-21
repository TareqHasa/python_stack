def count_down (num):
    x=list()
    for i in range(num,-1,-1):
        x.append(i)
    return x
print(count_down(5))  # 1


def print_and_return (arr):
    print (arr[0])
    return arr[1]
print_and_return([1,2])


def first_plus_length(arr):
    return arr[0]+len(arr)

print (first_plus_length([1,2,3,4,5]))  


def values_greater_than_second (arr):
    print(len(arr))
    count=0
    newarr=list()
    if len(arr)<2:
        return False
    for i in range (0,len(arr)-1,1):
        if arr[i]>arr[i+1]:
            count+=1
            newarr.append(arr[i])
    print(count)        
    return newarr
print(values_greater_than_second([5,2,3,2,1,4]))


def length_and_value(size,value):
    x=[]
    for i in range (0,size):
        x.append(value)
    return x
print(length_and_value(4,7))
print(length_and_value(6,2))