# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        if head.next is None:
            return True

        cur=head
        count=1
        while cur.next!=None:
            cur=cur.next
            count+=1
        if count==2:
            if head.val==head.next.val:
                return True
            else:
                return False
        
            
        mid=count//2
        num=1
        cur=head
        prev1=None
        while num<=mid:
            prev1=cur
            cur=cur.next
            num+=1
        #print(cur)
        
        cur1,nextn=cur,cur
        prev=None
        while nextn!=None:
            nextn=cur1.next
            cur1.next=prev
            prev=cur1
            cur1=nextn
        prev1.next=prev
        # print(prev1)
        head2=prev1.next
        head1=head
      
        i=0
        cura=head1
        curb=head2
        # print(cura)
        # print(curb)
        # print(mid)
        while i<mid:

            if cura.val!=curb.val:
                
                return False
            cura=cura.next
            curb=curb.next
            i+=1

        return True
            
            
            
            
        
            
        
        
        
        
        
        
        
        