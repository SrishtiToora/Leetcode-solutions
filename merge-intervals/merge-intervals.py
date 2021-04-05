class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        while (1):
            for i in range(len(intervals)-1):
                if intervals[i][1]>=intervals[i+1][0] and intervals[i][1]<=intervals[i+1][1]:
                    x=intervals.pop(i)
                    y=intervals.pop(i)
                    l=(x[0],y[1])
                    intervals.insert(i,l)
                    break
                elif intervals[i][1]>=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1]:
                    intervals.pop(i+1)
                    break
                #elif intervals[i][1]==intervals[i+1][0]:
                 #   x=intervals.pop(i)
                  #  y=intervals.pop(i)
                   # l=(x[0],y[1])
                    #intervals.insert(i,l)
                    #break
            else:
                break
        return intervals
        
                
        