# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack=[]
        temp =head
        while temp:
            stack.append(temp)
            temp=temp.next
        if len(stack) > 0:
            head=temp=stack.pop()
            while len(stack) >0:
                temp.next=stack.pop()
                temp=temp.next
            temp.next=None
        return head
