import pandas as pd
import time
from datetime import datetime, timedelta

df = pd.read_csv("ScriptCapturaLCP.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])


hora_atual = datetime.now()






print("\nBem-vindo(a) ao mini prompt de monitoramento de hardware.\n")


#ainda em produção!!!!
while True:
    def dadosHora():
        ultima_hora = hora_atual - timedelta(hours=1)
        filtroHora = df[df["timestamp"] >= ultima_hora]
        for x in range(len(filtroHora["timestamp"])):
            print(f"{filtroHora["timestamp"][x]} \nUsuário: {filtroHora["usuario"][x]} \nUso da CPU: {filtroHora["CPU"][x]}% \nRAM: {filtroHora["RAM"][x]} Gb \nDisco usado: {filtroHora["Disco"][x]} Gb \nPacotes Enviados: {filtroHora["PacotesEnv"][x]} \nPacotes Recebidos: {filtroHora["PacotesRec"][x]}\n")
        time.sleep(2)
    

    def periodoTempo():
        momentoMin_str = input("Digite a data/hora minima que deseja nesse formato: (dia/mes/ano hora:minuto): \n")
        momentoMin = datetime.strptime(momentoMin_str, "%d/%m/%Y %H:%M")

        momentoMax_str = input("Digite a data/hora máxima que deseja nesse formato: (dia/mes/ano hora:minuto): \n")
        momentoMax = datetime.strptime(momentoMax_str, "%d/%m/%Y %H:%M")


        filtroPeriodo = df[(df["timestamp"] >= momentoMin) & (df["timestamp"] <= momentoMax)]
        print(f"\nData/Hora: {filtroPeriodo['timestamp']} \nUsuário: {filtroPeriodo["usuario"]} \nUso da CPU: {filtroPeriodo["CPU"]}% \nRAM: {filtroPeriodo["RAM"]} Gb \nDisco usado: {filtroPeriodo["Disco"]} Gb \nPacotes Enviados: {filtroPeriodo["PacotesEnv"]} \nPacotes Recebidos: {filtroPeriodo["PacotesRec"]}\n")
        time.sleep(2)


    def minutosAtras():
        minutosAtras = input("Escolha de quantos minutos atrás deseja ver: \n")
        ultimosMinX = hora_atual - timedelta(minutes=int(minutosAtras))
        filtroMin = df[df["timestamp"] >= ultimosMinX]
        print(f"\nData/Hora: {filtroMin['timestamp']} \nUsuário: {filtroMin["usuario"]} \nUso da CPU: {filtroMin["CPU"]}% \nRAM: {filtroMin["RAM"]} Gb \nDisco usado: {filtroMin["Disco"]} Gb \nPacotes Enviados: {filtroMin["PacotesEnv"]} \nPacotes Recebidos: {filtroMin["PacotesRec"]}\n")
        time.sleep(2)


    print("\n1 Ver a média dos dados de até uma hora atrás;")
    print("2 Ver os dados em um determinado período tempo;")
    print("3 Ver os dados de x minutos atrás;")
    print("4 Sair.")

    resposta = input("\nSelecione uma opção acima: ")
    if int(resposta) == 1:
        dadosHora()
    elif int(resposta) == 2:
        periodoTempo()
    elif int(resposta) == 3:
        minutosAtras()
    elif int(resposta) == 4:
        print("Obrigado. Encerrando...")
        time.sleep(1)
        break
    
         
        


    





