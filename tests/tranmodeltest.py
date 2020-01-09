import pandas as pd
import optable

df = optable.TransportationModel.read_csv("tranmodel.txt")
print(df.fillna(""))
tranmodel = optable.TransportationModel(df)
result = tranmodel.solve()
print(result.status)
print(result.objective)
print(result.xmatrix)
