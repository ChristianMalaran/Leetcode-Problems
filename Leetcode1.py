def twoSum(nums, target):
        
    dic = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in dic:
            return dic[comp],i
        dic[nums[i]]=i
        
nums = [0,1,2,3,4]
print(twoSum(nums, 6))