def equalize_array(nums):
    min_diff = float('inf')
    moves = []

    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        if diff < min_diff and nums[i] != 0 and not (diff in moves):
            moves.append((i, i + 1, diff))

    if not moves:
        return nums

    for move in moves:
        nums[move[0]] -= move[2]
        nums[move[1]] -= move[2]

    return nums

array = [6,7,1,4,2]
testarray = [6,7,1,4,2]
equalized_array = equalize_array(array)

print(equalized_array)