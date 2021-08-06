# Nicholas Grosso
# Coding practice for Standford Alg course

def merger(arr):
    if len(arr) > 1:
        center = len(arr) // 2
        left = arr[:center]
        right = arr[center:]
        #Sort left side
        merger(left)
        #Sort right side
        merger(right)
        #i will be for left array, j for right array, and k for arr
        i = j = k = 0
        #Set data into left and right arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1

arr = [52, 12, 1, 18, 22, 6]
print("Array before was")
print(arr)
merger(arr)
print("Array after being merged is")
print(arr)