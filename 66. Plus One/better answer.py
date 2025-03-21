
digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,0,4]
s=''
for i in digits:
    s+=str(i)    

s=str(int(s)+1)
s = [int(i) for i in s]
print(s)
