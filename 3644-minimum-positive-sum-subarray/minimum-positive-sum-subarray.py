class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        ans = float('inf')

        # Try every window size from l to r
        for k in range(l, r + 1):
            window_sum = sum(nums[:k])

            # Check first window
            if window_sum > 0:
                ans = min(ans, window_sum)

            # Slide the window
            for i in range(k, n):
                window_sum = window_sum+nums[i] - nums[i - k]
                if window_sum > 0:
                    ans = min(ans, window_sum)

        if ans!=float('inf'):
            return ans
        else:
            return -1
