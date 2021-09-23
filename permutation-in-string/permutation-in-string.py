class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=list(s1)
        s2=list(s2)
        print(s2)
        
        k=len(s1)
        d={}
        for i in range(k):
            if s1[i] in d:
                d[s1[i]]+=1
            else:
                d[s1[i]]=1
        i,j=0,0
        # print(d)
        count=len(d)
        while j<len(s2):
            # print(s2[i:j+1])
            # print(j)
            # print(s2[j])
            if s2[j] in d:
                d[s2[j]]-=1
                if d[s2[j]]==0:
                    count-=1
            # print(d)
            # print(count)
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                # print(s2[j])
                # print(d)
                # print(count)
                if count==0:
                    
                    return True
                if s2[i] in d:
                    # print(s2[i])
                    d[s2[i]]+=1
                    if d[s2[i]]==1:
                        count+=1    
                i+=1
                j+=1 
            # print(count)
        return False
                        