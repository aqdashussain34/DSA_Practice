class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum= sum(nums[:k])
        max_sum=window_sum
        for right in range(k,len(nums)):
            window_sum= nums[right]+window_sum # sum of k+1 elements
            window_sum= window_sum - nums[right-k] #sum of k elements(by subtracting prior element from the sum recieved in line 6)
            max_sum= max(max_sum, window_sum)
        return max_sum/k