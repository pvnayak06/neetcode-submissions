class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Case 1: Found the target
            if nums[mid] == target:
                return mid
            
            # Case 2: Target is larger -> look in the right half
            elif nums[mid] < target:
                left = mid + 1
                
            # Case 3: Target is smaller -> look in the left half
            else:
                right = mid - 1
                
        # Target was not found in the array
        return -1