
# This program takes an array and a target number
# print the pairs of numbers which sum to the target number

def pair_sum():
    i = 0
    target = 5
    arr = [1,2,3,4,5,6,7,8,9]
    while(i<len(arr)):
        j = 1
        while (j < len(arr)-1):
            if arr[i]+arr[j]==target:
                print(arr[i],arr[j]);
            j += 1
        i+=1

print(pair_sum())
