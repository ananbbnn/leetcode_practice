

def missingNumber(nums):
    
    sort = sorted(nums)
    
    if sort[0] != 0:
        return 0
    elif sort[-1] != len(sort):
        return len(sort)
    else:
        for i in range(len(sort)-1):
            if sort[i+1] - sort[i] == 1:
                pass
            else:
                return i+1





print(missingNumber([3,0,1]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))
print(missingNumber([1]))