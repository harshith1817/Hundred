n=3
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# for _ in range(n):
#     row=list(map(int,input().split()))
#     matrix.append(row)

for i in range(n):
    matrix[i][i],matrix[i][n-1-i]=matrix[i][n-1-i],matrix[i][i]

for row in matrix:
    print(" ".join(map(str,row)))