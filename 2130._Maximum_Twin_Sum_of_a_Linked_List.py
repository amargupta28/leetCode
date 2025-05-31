# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        temp=head
        arr=[]
        while temp:
            arr.append(temp.val)
            temp=temp.next
        
        i=0
        l=len(arr)-1
        maxCount=0
        while i < l:
            count=arr[i]+arr[l]
            if count > maxCount:
                maxCount=count
            i+=1
            l-=1
        return maxCount
            
            
        
        
