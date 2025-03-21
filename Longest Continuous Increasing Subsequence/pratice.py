

def longest_continuous_increasing_subsequence(nums = [2,2,2,2,2]):
    x = nums[0]
    count = 1
    output = 0
    for num in nums:
        if num > x:
            count+=1
            if count > output:
                output = count
        else:
            count = 1
            if count > output:
                output = count
        x = num
    return output 
        


print(longest_continuous_increasing_subsequence())
