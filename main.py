from pandas import DataFrame, read_csv

afastasmento = """SE AFASTO A VIDA INTEIRA """
Historico = """
AQUI TESTADO O HISTORICO DENTRO DO PROGRAMA """
hist = f"""
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

»Afastamentos/Concessões por Incapacidade:
{afastamentos}

▶ANÁLISE
________________________________________________________________________

»Apresentação Atual:
{historico}
"""

data = read_csv("ae.csv",delimiter=',',index_col=0, header=4)
f = DataFrame(data).to_dict()

f["Value"].update({"r374":hist})


ensino =  f["Value"]["r393"]
emprego = f["Value"]["r588"]
ult_atividade = f["Value"]["r591"]
motivo = f["Value"]["r594"]
anamnese = f["Value"]["r374"]
documentos = f["Value"]["r375"]
eem = f["Value"]["r376"]
DID = f["Value"]["r605"]
print(anamnese)