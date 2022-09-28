from pandas import DataFrame, read_csv

#VARIABLES
afastamentos:str = None
historico:str = None

HDA = f"""
▶OBJETO: 
________________________________________________________________________

→Trata-se de demanda para (re)estabelecimento Auxilio Doença/BPC

▶OBSERVAÇÕES:
________________________________________________________________________

→Solicita-se que dúvidas/esclarecimentos, quando presentes, sejam encaminhados via intimação de "Pedido de Laudo Complementar". Isso direciona o processo para caixa específica do sistema, agilizando o processo.

→Documentos de data posterior à avaliação não influirão em conclusão emitida, pois cabe ao autor reunir todos os elementos necessários até a realização da perícia. Novas evidências necessitarão novo procedimento pericial.

→Os dados e consequentes conclusões baseiam-se na estruturação do relato do periciando; a congruência entre o quadro atual (sintomas descritos;  exame estado mental; análise de linguagem corporal), com diagnósticos/descrições em documentos médicos e respostas esperadas para cada tratamento dentro de sua casuística.

▶RESUMO DE DADOS PREVIDENCIÁRIOS:
________________________________________________________________________

»A/Concessões por Incapacidade:
{afastamentos}

▶ANÁLISE
________________________________________________________________________

»Apresentação Atual:
{historico}
"""
#KEYS
ensino =  f["Unnamed: 3"]["r393"]
emprego = f["Unnamed: 3"]["r588"]
ult_atividade = f["Unnamed: 3"]["r591"]
motivo = f["Unnamed: 3"]["r594"]
anamnese = f["Unnamed: 3"]["r374"]
documentos = f["Unnamed: 3"]["r375"]
eem = f["Unnamed: 3"]["r376"]
DID = f["Unnamed: 3"]["r605"]

data = read_csv("ae.csv",delimiter=',',index_col=0)
frame = DataFrame(data)
f = DataFrame(data).to_dict()
print(f)
f["Unnamed: 3"].update({"r374":hist})




secframe = DataFrame(f).to_csv(header=False)
with open("ae.csv", "w+") as f:
    f.write(secframe)
