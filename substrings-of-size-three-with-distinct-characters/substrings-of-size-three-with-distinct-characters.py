class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        s=list(s)
        k=3
        d={}
        count=0
        ans=0
        i,j=0,0
        while j<len(s):
            print(s[j])
            if s[j] in d:
                # print("1")
                d[s[j]]+=1
                if d[s[j]]==1:
                    # print("3")
                    count+=1
                if d[s[j]]==2:
                    count-=1
            elif s[j] not in d:
                # print("2")
                d[s[j]]=1
                if d[s[j]]==1:
                    # print("3")
                    count+=1
                if d[s[j]]==2:
                    count-=1
            print(d)
            print(count)
            
            if j-i+1<k:
                # print("4")
                j+=1
            elif j-i+1==k:
                # print("5")
                if count==3:
                    # print("6")
                    ans+=1
                d[s[i]]-=1
                if d[s[i]]==1:
                    count+=1
                elif d[s[i]]==0:
                    count-=1
                i+=1
                j+=1
            
            
        return ans
                