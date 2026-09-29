class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxim = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                maxim = max(maxim, count)
                count = 0

        return max(maxim, count)
