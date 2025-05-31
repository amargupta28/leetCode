# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        temp =head
        post = head.next
        
        
        while temp and post:
            print(temp.val,post.val)
            temp.val, post.val = post.val,temp.val
            print(temp.val,post.val)
            if temp.next and temp.next.next:
                temp = temp.next.next
            if post.next and post.next.next:
                post= post.next.next
            else:
                break
        return head
        
        
