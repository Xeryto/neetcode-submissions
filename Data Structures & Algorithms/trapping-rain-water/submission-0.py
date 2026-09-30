class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [height[0]]
        postfix = [height[-1]]

        ans = []

        for i in range(1, len(height)):
            prefix.append(max(prefix[-1], height[i]))
            postfix = [max(postfix[0], height[len(height)-1-i])]+postfix
        
        for i in range(1,len(height)-1):
            ans.append(max(min(prefix[i-1], postfix[i+1]) - height[i], 0))

        return sum(ans)
