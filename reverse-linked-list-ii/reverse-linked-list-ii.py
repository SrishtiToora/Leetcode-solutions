# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count=1
        cur1=head
        while count<=right:
            cur1=cur1.next
            count+=1
        # print(cur1) cur 1 none
        
        if right-left==0:
            return head
        # if right-left==1 and count==2:
        #     prev=None
        #     cur,nextn=head,head
        #     nextn=nextn.next
        #     cur.next=prev
        #     prev=cur
        #     cur=nextn
        #     cur.next=prev
        #     return cur
        x=right-left+1
        
        
        count=1
        prev1=None
        cur2=head
        while count<left:
            prev1=cur2
            cur2=cur2.next
            count+=1
        
        
        # print(cur2)
        # print(prev1)
            
        cur,prev=cur2,None
        nextn=cur2
        # print(cur,prev,nextn)
        count=1
        while count<=x :
            
            nextn=nextn.next
            cur.next=prev
            prev=cur
            cur=nextn
            count+=1
        # print(count)
        print(prev)
        
        if cur2:
            cur2.next=cur1
        if prev1:
            prev1.next=prev
        elif prev1==None:
            return prev
        # print(prev1)
        
        
        # print(cur2)
        # print(head)
        return head
        
            
            
            
            
            
            
            