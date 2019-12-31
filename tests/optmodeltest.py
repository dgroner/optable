import pandas as pd
import optable

df = optable.OptModel.read_csv("lpmodel.txt")
print(df.fillna(""))
lpmodel = optable.OptModel(df)
result = lpmodel.solve()
print(result.status)
print("x:\n" , result.x, sep='')
print("slack:\n" , result.slack, sep='')

