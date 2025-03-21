grid = [[0,1,0],
        [0,1,0],
        [1,1,1],
        [0,0,0]]

n1 = range(len(grid))
n2 = range(len(grid[0]))
h_grid = []

for i in n2:
    ls=[]
    for j in n1:
        ls.append(grid[j][i])
    h_grid.append(ls)

output = 0
total = 0
w_check = []
for i in n1:
    total += sum(grid[i])
    if sum(grid[i]) == 1:
        w_check.append([i,grid[i].index(1)])
h_check = []
for i in n2:
    if sum(h_grid[i]) == 1:
        h_check.append([h_grid[i].index(1),i])

print(list(set(*w_check).intersection(*h_check)))
        

#print(h_grid)
#print(w_check) 
#print(h_check)       
#print(total)   


'''
for ls1 in w_check:
    for ls2 in h_check:
        if ls1 == ls2:
            total -= 1
'''



