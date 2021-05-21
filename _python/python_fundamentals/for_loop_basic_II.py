# 1 Biggie Size
def biggie_size(arr):
    for i in range(0,len(arr)):
        if arr[i]>=0:
            arr[i]="big"
    return arr        
print (biggie_size([-1, 3, 5, -5]))

# 2 Count Positives
def count_positives(arr):
    count=0
    for i in range (len(arr)):
        if arr[i]>=0:
            count+=1
    arr[len(arr)-1]=count
    return arr 
print(count_positives([-1,1,1,1]))     

# Sum Total
def  sum_total(arr):
    sum=0
    for i in range (len(arr)):
        sum += arr[i]
    return sum
print(sum_total([1,2,3,4]))

# Average 
def average(arr):
    x=sum_total(arr)
    count=0
    for i in range (len(arr)):
        count+=1
    return x/count
print (average([1,2,3,4]))

# Length 
def Length (arr):
    return len(arr)
print(Length([]))

# Minimum 
def minimum (arr):
    min=arr[0]
    if len(arr)==0:
        return False
    else:
        for i in range (len(arr)):
            if arr[i]<min:
                min=arr[i]
        return min        
print (minimum([37,2,1,-9]))

# Maximum 
def maximum (arr):
    max=arr[0]
    if len(arr)==0:
        return False
    else:
        for i in range (len(arr)):
            if arr[i]>max:
                max=arr[i]
        return max        
print (maximum([37,2,1,-9]))

# Ultimate Analysis 
def ultimate_analysis (arr):
    dictionary={
        "sumtotal":sum_total(arr),
        "average":average(arr),
        "minimum":minimum(arr),
        "maximum":maximum(arr),
        "length":Length(arr)    
    }
    return dictionary
print(ultimate_analysis([37,2,1,-9]))    

# Reverse List 
def reverse_list(arr):
    for i in range (0,int(len(arr)/2)):
        arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
    return arr
print(reverse_list([37,2,1,-9]))



