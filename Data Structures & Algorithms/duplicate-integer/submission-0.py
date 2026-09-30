class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cleaned = set(nums)
        return not (len(cleaned)==len(nums))