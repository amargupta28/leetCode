# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=[]
        temp=list1
        head=None
        tail=None
        while temp:
            l1.append(temp.val)
            temp=temp.next
        temp=list2
        while temp:
            l1.append(temp.val)
            temp=temp.next
            
        for itm in sorted(l1):
            node= ListNode(itm)
            if head is None:
                head=node
                tail=node
            else:
                tail.next=node
                tail=node
        return head
            
        
