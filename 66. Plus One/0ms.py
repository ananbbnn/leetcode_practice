
digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,0,4]

output = 0
for i,num in enumerate(digits):
    output+=num*(10**(len(digits)-i-1))
    print(output)
output=str(int(output)+1)

output=[int(s) for s in output]

print(output)

    






