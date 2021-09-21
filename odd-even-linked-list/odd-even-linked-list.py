# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        if head.next==None:
            return head
        if head.next.next==None:
            return head
        cur=head
        count=0
        prev=None
        while cur!=None:
            count+=1
            prev=cur
            cur=cur.next
        
        print(count)
        
        i=1
        temp=head
        start=head
        end=prev
        # print(start)
        # print(end)
        prev=None
        
        while i<=count:
            if i%2!=0:
                i+=1
                prev=temp
                temp=temp.next
            else:
                tempNode=ListNode(temp.val)
                end.next=tempNode
                start.next=temp.next
                
                start=start.next
                end=end.next
                i+=1
                temp=start
        return(head)
            
            
            
            