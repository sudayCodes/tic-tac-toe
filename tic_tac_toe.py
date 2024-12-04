import random
coord = [
    (0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2) #coordinates
]
grid = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]      # empty grid
print("Game starting.....")
print("Remember player-O computer-X")
print("carefully select the position")
try:
    for i in range(4):
        # 2 players plays one by one
        # human -O computer -X
        y1 = input("Enter x coord: ")
        x1 = input("Enter y coord: ")
        x2 = int(x1)-1
        y2 = int(y1)-1
        tup1 = (x2, y2)
        coord.remove(tup1)
        tup = random.choice(coord)
        grid[tup1[0]][tup1[1]]="O"
        grid[tup[0]][tup[1]]="X"
        coord.remove(tup) # removes already placed coordinate
        # Winner detection algorithm
        if grid[0][0] == grid[0][1] and grid[0][0] == grid[0][2] and grid[0][0]!=" ":
            a = grid[0][0]
            print("Player "+a+" Wins!!!")
            break
        elif grid[1][0] == grid[1][1] and grid[1][0] == grid[1][2] and grid[1][0]!=" ":
            a = grid[1][0]
            print("Player "+a+" Wins!!!")
            break
        elif grid[2][0] == grid[2][1] and grid[2][0] == grid[2][2] and grid[2][0]!=" ":
            a = grid[2][0]
            print("Player "+a+" Wins!!!")
            break
        elif grid[0][0] == grid[1][0] and grid[0][0] == grid[2][0] and grid[0][0]!=" ":
            a = grid[0][0]
            print("Player "+a+" Wins!!!")
            break
        elif grid[0][1] == grid[1][1] and grid[0][1] == grid[2][1] and grid[0][1]!=" ":
            a = grid[0][1]
            print("Player "+a+" Wins!!!")
            break
        elif grid[0][2] == grid[1][2] and grid[0][2] == grid[2][2] and grid[0][2]!=" ":
            a = grid[0][2]
            print("Player "+a+" Wins!!!")
            break
        elif grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and grid[0][0]!=" ":
            a = grid[0][0]
            print("Player "+a+" Wins!!!")
            break
        elif grid[2][0] == grid[1][1] and grid[2][0] == grid[0][2] and grid[2][0]!=" ":
            a = grid[2][0]
            print("Player "+a+" Wins!!!")
            break
        if i ==8:
            print("No player won, It's a draw")
        # printing the 3D grid 
        for i in range(7):
            if (i%2)==0:
                print(" ___ ___ ___")
            else:
                result =''
                j = (i-1)*0.5
                for k in range(3):
                    result += "|  "+ grid[int(j)][k]
                print(result+"|")
except:
    print("Invalid input, you lost!!")
