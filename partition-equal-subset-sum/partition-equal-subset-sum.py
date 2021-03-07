class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        half=s//2
        if s%2==1:
            return False
        if max(nums)>half:
            return False
        else:
            nums=sorted(nums)
            dp=[[False for i in range(half+1)]for i in range(len(nums))]
            for i in range(len(nums)):
                for j in range(half+1):
                    if i==0 and j==0:
                        dp[i][j]=True
                    if i==0 and j!=0:
                        dp[i][j]=False
                    if i!=0 and j==0:
                        dp[i][j]=True
                    if i!=0 and j!=0:
                        if nums[i]>j:
                            dp[i][j]=False
                        dp[i][j]= dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[-1][-1]
    