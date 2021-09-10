first_line = input()
k, l, r = first_line.split()
k = int(k)
l = int(l)
r = int(r)

arr = [[0 for i in range(l)] for j in range(k)]

first_strawberry = input()
second_strawberry = input()

spoiled1_row, spoiled1_column = first_strawberry.split()
spoiled1_row = int(spoiled1_row)
spoiled1_column = int(spoiled1_column)

if second_strawberry != "":
    spoiled2_row, spoiled2_column = second_strawberry.split()
    spoiled2_row = int(spoiled2_row)
    spoiled2_column = int(spoiled2_column)
else:
    spoiled2_row = spoiled1_row
    spoiled2_column = spoiled1_column

spoiled1_row = len(arr) - spoiled1_row
spoiled2_row = len(arr) - spoiled2_row

arr[spoiled1_row][spoiled1_column - 1] = 1;
arr[spoiled2_row][spoiled2_column - 1] = 1;


for days in range(1, r+1):
   
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == days:
                if i>0:
                    if arr[i-1][j] < days:
                        arr[i-1][j] = days+1
                if i<len(arr) - 1:
                    if arr[i+1][j] < days:
                        arr[i+1][j] = days+1
                if j>0:
                    if arr[i][j-1] < days:
                        arr[i][j-1] = days+1
                if j<len(arr[i]) - 1:
                    if arr[i][j+1] < days:
                        arr[i][j+1] = days+1
    for row in arr:
        print(row)
    print()

sum = 0           
for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        if (arr[i][j] == 0):
            sum+=1
    

print(sum)