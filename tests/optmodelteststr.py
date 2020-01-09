from optable import OptModel

df2 = OptModel.read_str(
"""
name   x1 x2  sense rhs
# objective:
obj     3  5    max
# subject to:
#x1lower 1  0    = 2
plant1  1  0    <=   4
plant2  0  2    <=  12
plant3  3  2    <=  18
""")
lpmodel2 = OptModel(df2)
print(lpmodel2)
result2 = lpmodel2.solve()
print(result2)
