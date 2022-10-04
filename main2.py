from pandas import read_excel
from pandas import DataFrame
#Scipy table frequency distribution 



exc = read_excel('data.xlsx', engine = 'openpyxl', names = ["B1", "B2", "B3", "B4", "B5","B6"],nrows=85)	# read excel file


freq = {
"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, 
"14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0,"23":0, "24":0, "25":0,
"26":0, "27":0, "28":0, "29":0, "30":0, "31":0, "32":0, "33":0, "34":0,"35":0, "36":0, "37":0,
"38":0, "39":0, "40":0, "41":0, "42":0, "43":0, "44":0, "45":0, "46":0,"47":0, "48":0, "49":0,
"50":0, "51":0, "52":0, "53":0, "54":0, "55":0, "56":0, "57":0, "58":0, "59":0, "60":0
        }

def Dez(key):
    data: dict = DataFrame(exc).to_dict("index")
    for i in range(key):
        sorteio = data[i]["B1"], data[i]["B2"], data[i]["B3"], data[i]["B4"], data[i]["B5"], data[i]["B6"]
        for j in range(6):
            freq[str(sorteio[j])] += 1
    return freq

from matplotlib import pyplot as plt
Dez(85)
x =[ x for x in range (1,60)]
y = [ freq[str(x)] for x in range (1,60)]
plt.plot(x,y)
plt.show()