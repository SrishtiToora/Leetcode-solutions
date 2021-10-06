class Solution:
    def maximumUnits(self, box: List[List[int]], trucksize: int) -> int:
        s=0
        tot=0
        truck=0
        total=0
        for i in range(len(box)):
            s+=box[i][0]
            tot+=box[i][1]
        if s<=trucksize:
            for i in range(len(box)):
                truck+=box[i][0]
                total+=box[i][0]*box[i][1]
            return total
                 
        box=sorted(box,key=lambda x:x[1])
        box=box[::-1]
        
        i=0
        while truck<trucksize:
            if truck+box[i][0]>trucksize:
                total+=(trucksize-truck)*box[i][1]
                print(total)
                truck=trucksize  
            else:
                truck+=box[i][0]
                total+=box[i][0]*box[i][1]

            i+=1
        return total
        
            
        