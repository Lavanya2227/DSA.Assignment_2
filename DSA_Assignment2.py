#1.Implement Binary Search

def binary_search(arr,a,low,high):
   
    while low <= high:
        mid = low + (high-low)//2
        
        if arr[mid] == a:
            return mid
        
        elif arr[mid] > a:
            low = mid + 1
        
        else:
            high = mid - 1
    
    return -1

arr=[1,2,3,4,5,6,7,8,9,10]
print("The array given is: ",arr)
a = 5
index = binary_search(arr,a,0,len(arr)-1)
if index != -1:
    print("The index of the element is " + str(index))
else:
    print("Element Not found")  


 #2.Implement merge sort

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        mergesort(sub_array1)
        mergesort(sub_array2)

        i = j = k = 0
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

        while i < len (sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1
        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1
arr = [7,8,9,12,4,3,2,1]
mergesort(arr)
print(arr) 


#3.Implement Quick Sort

def Quicksort(arr):
            elements = len(arr)
            if elements < 2:
                      return arr
            current_position = 0
            for i in range(1,elements):
                    if arr[i] <= arr[0]:  
                      current_position += 1
                      temp = arr[i]
                      arr[i] = arr[current_position]
                      arr[current_position] = temp
            temp = arr[0]
            arr[0] = arr[current_position]
            arr[current_position] = temp
            left = Quicksort(arr[0:current_position])
            right = Quicksort(arr[current_position+1:elements])
            arr = left + [arr[current_position]] + right
            return arr
array_to_be_sorted = [4,27,3,1,6]
print("Original Array: ",array_to_be_sorted)
print("Sorted Array: ",Quicksort(array_to_be_sorted)) 


#4.Implement Insertion Sort

def insertionsort(arr):
    if (n := len(arr)) <= 1:
        return
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key <arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
arr = [6,8,9,3,5,2,10]
insertionsort(arr)
print(arr) 

#5.Write a program to sort list of strings (similar to that of dictionary)
 
  
lst = [{'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr'}]

# Using sort() function
lst.sort()
 
print(lst)                     


             
    



                       

