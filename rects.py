lst = [4, 7, 2, 5, 8, 4, 2, 6, 8, 1]
#lst = [1, 1, 1, 1]
#lst = [1, 2, 3, 4, 5, 6]

lst = [int(i) for i in input().split()]

def clear_list(lst):
    # Create a dictionary to count the occurrences of each element
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    # Iterate through the dictionary and remove elements that have a count less than 2
    for key, value in count_dict.items():
        if value < 2:
            lst.remove(key)

    return lst


last_4 = sorted(clear_list((lst)))[-4:]
#print(last_4)

if len(last_4) != 4:
    print(-1)
elif last_4[1] == last_4[-1]:
    print(last_4[1]**2)
else:
    print(last_4[1]*last_4[-1])
