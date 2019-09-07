class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        pre, back = 0, len(height) - 1

        while pre < back:
            max_area = max(max_area, min(height[pre], height[back]) * (back - pre))

            if height[pre] < height[back]: pre += 1
            else: back -= 1

        return max_area