
old = [1,2,3,4,5,6,7,8]
k = 3
def rotate_array():
    i = 0
    new_list = old.copy()
    while i < len(old):
        next_index = (i + k) % len(old)
        new_list[next_index] = old[i]
        i = i + 1

    return new_list

print(rotate_array())