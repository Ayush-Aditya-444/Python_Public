print("2D Lists:-")
Matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(Matrix)
print(Matrix[2][2])
Matrix[0][2]=44
print(Matrix)
Matrix[0][2]=3
for x in Matrix:
    for y in x:
        print(y)