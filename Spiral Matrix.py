# import numpy as np
matrix = [[1,2,3],[4,5,6]]
# n=3
# m=3
# top = 0
# bottom = m-1 
# right = n-1
# left = 0 
# dir =0
# ans = []
# while(top<=bottom and left<= right):
#     if dir ==0:
#         for i in range(right):
#             print(i)
#             print(matrix[top,i])
#             top+=1
#     elif dir ==1:
#         for i in range(bottom):
#             print(matrix[i,right])
#             right-=1        
#     elif dir ==2:
#         for i in range(2,-1,-1):
#             print(matrix[bottom,i])
#             bottom-=1        
#     elif dir ==3:
#         for i in range(2,-1,-1):
#             print(matrix[i,left])
#             left+=1        
#     dir  =(dir+1)%4       

# print(ans)    

def spiral(matrix):
    if not matrix:
        return[]

    top = 0
    bottom = len(matrix)
    left = 0
    right = len(matrix[0])    
    ans = []

    while( top<=bottom and left<=right ):
        for i in range(left,right):
            ans.append(matrix[top][i])
        for j in range(top+1,bottom-1):
            ans.append(matrix[j][right-1])
        if bottom != top+1:
            for i in range(right-1,left-1,-1):
                ans.append(matrix[bottom-1][i])
        if left != right-1:
            for j in range(bottom-2,top,-1):
                ans.append(matrix[j][left])
        top +=1
        bottom-=1
        left +=1   
        right -=1
    return ans                    

# print(dum(matrix))
matrixa = matrix[0]+ matrix[1][::-1]


print(matrixa)