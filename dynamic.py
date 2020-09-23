class Dynamic:
    def lenthOflist(self, nums):
        if not nums:
            return 0
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)#update the count in dp[i]
        return max(dp)

nums=[10,9,2,5,3,7,101,18]
dynamic = Dynamic()
result = dynamic.lenthOflist(nums)
print(result)