def productExceptSelf(nums):

    length = len(nums)
    left = [1]*len(nums)
    right =[1]*len(nums)

    for i in range(1, length):
        left[i] = left[i-1] * nums[i-1]

    for j in range(length-2,-1,-1):
        right[j] = right[j+1] * nums[j+1]
    
    for k in range (0,length):
        nums[k] = right[k] * left[k]
        print(nums[k])

    return nums