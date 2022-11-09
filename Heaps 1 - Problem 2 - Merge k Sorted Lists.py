"""
FAANMG Problem #82 {Hard} 

23. Merge k Sorted Lists


Time complexity : O(n log(k))
Space complexity : O(k)


Did this code successfully run on Leetcode : Yes


@name: Rahul Govindkumar_RN27JUL2022
""" 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = tail = ListNode(0)

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                print(heap)

        while heap:
            node = heapq.heappop(heap)
            node = node[2]
            tail.next = node
       
            tail = tail.next
            
            if node.next:
                i += 1
                heapq.heappush(heap, (node.next.val, i, node.next))

        return head.next