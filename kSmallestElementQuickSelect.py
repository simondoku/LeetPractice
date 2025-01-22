import random

def quickselect(arr, k):

    def partition(left, right, pivot_index):
        pivot_value = arr[pivot_index]
        #move the pointer to the end
        arr[pivot_index] = arr[right]
        arr[right] = arr[pivot_index]

        store_index = left

        #move elements smaller that the pivot to the left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1
            
        #move the pivot to its final place
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index
    

    
    