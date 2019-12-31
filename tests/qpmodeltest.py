import optable

c = [3, 2]
cqm = [[1,0], [2,3]]
A = [[1,1],[1,0],[0,1]]
sense = ['=', '>=', '<=']
b = [1, 0.2, 0.7]
x0 = [.5, .5]
qp = optable.QpModel('max', c, cqm, A, sense, b, x0)
result = qp.solve()
print(result)

