from pandas import DataFrame, read_csv

data = read_csv("ae.csv",delimiter=',',index_col=0, header=4)
f = DataFrame(data).to_dict()
ensino =  f["Value"]["r393"]
emprego = f["Value"]["r588"]
ult_atividade = f["Value"]["r591"]
motivo = f["Value"]["r594"]
anamnese = f["Value"]["r374"]
documentos = f["Value"]["r375"]
eem = f["Value"]["r376"]

print(documentos)