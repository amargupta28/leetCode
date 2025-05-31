# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap=[]
        for idx,itm in enumerate(lists):
            if itm:  heappush(heap, (itm.val,idx))
        dummy=output = ListNode()
        while heap:
            val,idx=heappop(heap)
            output.next = ListNode(val)
            if lists[idx].next:
                heappush(heap,(lists[idx].next.val,idx))
                lists[idx]=lists[idx].next
            output=output.next
        return dummy.next
                
