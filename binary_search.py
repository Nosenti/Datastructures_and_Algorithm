arr = [1,2,3,4,5,6,7]
target = 4

def search_index():
    max = len(arr)-1
    min = 0
    while (min <= max):
        midpoint = int((max + min)/2)
        if  arr[midpoint] == target:
            return midpoint
        elif target > arr[midpoint]:
            min = midpoint + 1
        else:
            max = midpoint - 1
    return -1
print(search_index())