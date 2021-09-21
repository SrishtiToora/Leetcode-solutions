# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur=head
        count=0
        while cur!=None:
            cur=cur.next
            count+=1
        print(count)
        ele=count-n
        if ele==0:
            return head.next
        if count==1 and n==1:
            return None
        
        i=0
        cur=head
        prev=None
        while i<ele:
            prev=cur
            cur=cur.next
            i+=1
        prev.next=cur.next
        return head
            