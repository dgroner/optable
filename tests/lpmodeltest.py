import optable

p_c = [3, 5]
p_A = [[1,0],[0,2], [3,2], [1, 0]]
p_sense = ['<=', '<=', '<=', '']
p_b = [4, 12, 18, 3]
lpm = optable.LpModel("max", p_c, p_A, p_sense, p_b,
                       method='simplex', bounds=(0, None))
#print(lpm._isMax, lpm._c, lpm._bub)
#print(lpm._Aub)
result = lpm.solve()
print(result)

