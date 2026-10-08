class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        right_max = 0
        left = 0
        right = len(height)-1
        total_water = 0

        while left < right:
            if left_max <= right_max:
                curr_water = left_max-height[left]
                if curr_water > 0:
                    total_water += curr_water
                left_max = max(left_max, height[left])
                if left_max <= right_max:
                    left += 1
            else:
                curr_water = right_max-height[right]
                if curr_water > 0:
                    total_water += curr_water
                right_max = max(right_max, height[right])
                if right_max < left_max:
                    right -= 1
        
        return total_water