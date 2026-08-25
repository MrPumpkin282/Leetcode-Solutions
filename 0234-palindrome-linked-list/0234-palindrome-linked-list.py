# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        x = []
        count = 0
        while curr != None:
            x.append(curr.val)
            curr = curr.next
        for i in range(0,len(x)):
            if x[i] == x[len(x)-i-1]:
                count += 1
            else:
                return False
        if count == len(x):
            return True


        