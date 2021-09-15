class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        MaxL,CurL =0,0
        for w in range(len(arr)):
            if w>=2 and ((arr[w-2]<arr[w-1]>arr[w]) or (arr[w-2]>arr[w-1]<arr[w])):
                CurL+=1
            elif w>=1 and arr[w-1]!=arr[w]:
                CurL=2
            else:
                CurL =1
            MaxL = max(MaxL,CurL)
        
        return MaxL
            