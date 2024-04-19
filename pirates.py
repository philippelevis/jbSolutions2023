def movesrt(array,x,y,amount):
    array[x][0] = array[x][0]-amount
    array[y][0] = array[y][0]+amount

def move(array,x,y,amount):
    array[x] = array[x]-amount
    array[y] = array[y]+amount

array = [6, 7, 1, 4, 2]

sorted_array = []

for i in range(0,len(array)):
    sorted_array.append([array[i],i])
sorted_array.sort(key=lambda x: -x[0])

print(sorted_array)

moves = []

#print(sorted_array)

def getaveragesrt(array):
    sum = 0
    for i in range(0,len(array)):
        sum += array[i][0]
    return sum/len(array)

def execute_moves(array, moves):
    for mov in moves:
        move(array,mov[0],mov[1],mov[2])
    return array

def getnonequalsrt(array, target,start):
    for i in range(start,len(array)):
        if array[i][0] != target:
            return i
    return len(array)

def main():
    #get the target average amount in each slot
    target = getaveragesrt(sorted_array)
    for i in range(0,len(sorted_array)):
        if sorted_array[i][0] != target:
            #save the index so we dont execute the same move twice
            trgindex = getnonequalsrt(sorted_array, target,i+1)
            #add the move to moves
            moves.append([sorted_array[i][1],sorted_array[trgindex][1],sorted_array[i][0]-target])
            #move in the sorted array to represent the situation
            movesrt(sorted_array,i,trgindex,sorted_array[i][0]-target)

main()
print(moves)
print(sorted_array)

print(execute_moves(array,moves))