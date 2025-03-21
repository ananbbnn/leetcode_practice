
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    count = 0
    for i in range(len(nums)-1):
        n1 = nums[i]
        for j in range(1,len(nums)-count):
            n2 = nums[j+count]
            if n1 + n2 == target:
                return [i,j+count]
        count += 1
        
        
        
        
print(twoSum(nums=[2,7,11,15],target=9))
print(twoSum(nums=[3,2,4],target=6))
print(twoSum(nums=[3,3],target=6))
print(twoSum(nums=[-1,-2,-3,-4,-5],target=-8))