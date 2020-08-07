class Solution:
    def maxSubArray(nums) -> int:
        if nums is None:
            return 0
        ret = 0
        maxsum = nums[0] 
        for i in range(len(nums)):
            if ret <= 0:
                ret = nums[i]
            else:
                ret += nums[i]
            
            if ret > maxsum:
                maxsum = ret
        return maxsum

print(Solution.maxSubArray( [-2,1,-3,4,-1,2,1,-5,4]))