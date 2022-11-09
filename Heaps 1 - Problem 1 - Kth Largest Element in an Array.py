"""
FAANMG Problem #83 {Medium} 

215. Kth Largest Element in an Array


Time complexity : O(n log k)
Space complexity : O(k)


Did this code successfully run on Leetcode : Yes


@name: Rahul Govindkumar_RN27JUL2022
""" 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        for i in range(len(nums)): # Takes k time
            heapq.heappush(heap,nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
                
        return heap[0]