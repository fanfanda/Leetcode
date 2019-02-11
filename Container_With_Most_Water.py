class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        i, j, max_area = 0, len(height) - 1, 0
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] > height[j]: 
                j -= 1
            else:
                i += 1
        return max_area

t = Solution()
print(t.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))