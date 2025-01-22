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
    
    left, right = 0, len(arr) - 1
    while True:
        if left == right:
            return arr[left]
        pivot_index = random.randint(left, right)

        pivot_index = partition(left, right, pivot_index)

        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            left = pivot_index + 1

        else:
            right = pivot_index - 1



    
    