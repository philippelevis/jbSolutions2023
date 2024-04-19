a = 15 #int(input())
b = 15 #int(input())
c = b

def clear_last_non_zero_bit(num):
    # Get the binary representation of the number
    binary_num = bin(num)[2:]
    #print(binary_num)
    # Find the last non-zero bit from the right
    last_non_zero_bit_index = binary_num.rfind('1')
    # If there's no non-zero bit, return the original number
    if last_non_zero_bit_index == -1:
        return num
    # Create a new binary string with the last non-zero bit set to 0
    new_binary_num = binary_num[:last_non_zero_bit_index] + '0'*(len(binary_num)-last_non_zero_bit_index)
    #print(new_binary_num)
    # Convert the new binary string back to an integer
    result = int(new_binary_num, 2)

    return result

while c > a:
    #get the next number, by clearing the last non-zero bit
    d = clear_last_non_zero_bit(c)
    if d in range(a,b+1):
        #if in range, continue
        c = d
    else:
        #if not in range, break, useless to continue
        break

print(c)