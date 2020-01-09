from optable import TransportationModel

df2 = TransportationModel.read_str(
"""
   name  D1  D2  D3  D4  supply
   S1    464 513 654 867  75
   S2    352 416 690 791 125
   S3    995 682 388 685 100
   demand 80  65  70  85
""")
print(df2)
tranmodel2 = TransportationModel(df2)
result2 = tranmodel2.solve()
print(result2)
