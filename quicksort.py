import random

MAX = 100

def gen_list(amount: int, v: list):
    vals = list(v)
    for i in range (amount):
        try:
           vals.append(random.randint(1, MAX))
        except:       
            pass 
    return vals

def part_index(arr: list, low: int, high: int):
    pivot_i = low
    pivot = arr[pivot_i]
    while low < high:
        while low < len(arr) and arr[low] <= pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if (low < high):
            arr[low], arr[high] = arr[high], arr[low]
    arr[high], arr[pivot_i] = arr[pivot_i], arr[high]
    return high
    

def quick_sort(arr: list, low: int, high: int):
    try:
        if (low < high):
            Partition = part_index(arr, low, high)
            quick_sort(arr, low, Partition - 1)
            quick_sort(arr, Partition + 1, high)
        else:
            return "Error, not enough elements to sort!"       
    except Exception as e:
        return e

array = gen_list(int(input("Enter Value:\n")), [])
print(f'\n{array}\n\n')
quick_sort(array, 0, len(array) - 1)
print(array)
