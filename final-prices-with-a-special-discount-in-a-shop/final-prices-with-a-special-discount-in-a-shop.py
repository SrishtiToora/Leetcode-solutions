class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l=[]
        stack=[]
        for i in reversed(range(len(prices))):
            if len(stack)==0:
                l.append(prices[i])
                stack.append(prices[i])
            else:
                if stack[-1]<prices[i]:
                    l.append(prices[i]-stack[-1])
                    stack.append(prices[i])
                else:
                    while len(stack)>0 and stack[-1]>prices[i]:
                        stack.pop(-1)
                    if len(stack)==0:
                        l.append(prices[i])
                        stack.append(prices[i])
                    else:
                        l.append(prices[i]-stack[-1])
                        stack.append(prices[i])
        return l[::-1]
            