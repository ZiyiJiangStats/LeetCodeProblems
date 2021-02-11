
"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 

Return the sum of the three integers. You may assume that each input would have exactly one solution.

"""

#Approach 1:  Two pointers 
"""
1. initialize diff (the minimum difference )
2. sort the array 
3. iterate through the array 

for current position i, set lo = i+1, hi= len(nums)-1     (two pointers) 

while lo < hi pointer 
calculate the  sum = nums[i] + nums[lo] + nums[hi] 
if |sum-target| < diff,  update diff = sum -target 
if sum < target, lo += 1
else , hi -=1 

4. return target - diff 
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff




#Approach 2:  Binary Search 
"""
we fix two numbers, and use a binary search to find the third complement number. 
This is less efficient than the two pointers approach, however, it could be more intuitive to come up with.


algo: 
1. initialize diff 
2. sort input array nums 
3. iterate through the array(outter loop). For each i, iterate through the array from j = i +1 (inner loop) 
    then complement = target - nums[i] - nums[j] 
    use binary search to find the complement 
4. return target - diff 
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                hi = bisect_right(nums, complement, j + 1)
                lo = hi - 1
                if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                    diff = complement - nums[hi]
                if lo > j and abs(complement - nums[lo]) < abs(diff):
                    diff = complement - nums[lo]
            if diff == 0:
                break
        return target - diff
      
      
      # Time complexity : O(n^2logn) 

