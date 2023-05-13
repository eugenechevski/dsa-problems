class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            1. Define the subproblem: sorted subsequence
            2. Defien the state variables: 
            3. Find the recurrent connection:
        """ 
        dp = [1] * len(nums)
        LIS = 1
        for i in range(1, len(nums)):
            dp[i] = 1 + max([dp[j] for j in range(i) if nums[j] < nums[i]], default=0)
            LIS = max(LIS, dp[i])

        return LIS
        