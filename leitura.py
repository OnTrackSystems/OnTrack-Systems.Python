import pandas as pd
import time
from datetime import datetime, timedelta

df = pd.read_csv("coletaGeralOTS.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])


hora_atual = datetime.now()



print('\n' * 5)  
print("Bem-vindo(a) ao prompt de monitoramento de hardware.")
def escolhaRecurso():
    print("\n1 CPU;")
    print("2 RAM;")
    print("3 Disco;")
    print("4 Rede;")
    print("5 Todos.")
    escolha = input("\nSelecione uma opção acima: ")
    return escolha

def perguntar():
    print("\n1 Ver os dados de x minutos atrás;")
    print("2 Ver os dados em um determinado período tempo;")
    print("3 Sair.")
    resposta = input("\nSelecione uma opção acima: ")
    return resposta



while True:

    def filtroGeral(filtro, inicio, ePeriodo):
        inicioContagem = inicio

        if ePeriodo == True:
            for i in range(len(df["timestamp"])):
                if df["timestamp"][i] >= (inicio - timedelta(seconds=1)):
                    inicioContagem = i
                    break

        escolha = escolhaRecurso()

        if int(escolha) == 1:
            for x in range(inicioContagem, len(filtro["timestamp"])):
   
                #Abaixo existe duas formas de exibição. Se estiver em linux comente o primeiro e descomente o segundo
                print(f"{filtro["timestamp"][x]} Uso de CPU: {filtro["CPU"][x]}%")
                # print(f"{filtro["timestamp"][x]} Uso de CPU: {filtro["CPU"][x]}% || tempo de I/O: {filtro["tempoI/O"][x]} Segundos")
                
        elif int(escolha) == 2:
            for x in range(inicioContagem, len(filtro["timestamp"])):
                print(f"{filtro["timestamp"][x]} Uso de RAM: {filtro["RAM"][x]} GB")
        elif int(escolha) == 3:
            for x in range(inicioContagem, len(filtro["timestamp"])):
                print(f"{filtro["timestamp"][x]} Uso de disco: {filtro["Disco"][x]} GB")
        elif int(escolha) == 4:
            for x in range(inicioContagem, len(filtro["timestamp"])):
                print(f"{filtro["timestamp"][x]} Pacotes enviados: {filtro["PacotesEnv"][x]} || Pacotes recebidos: {filtro["PacotesRec"][x]}")
        elif int(escolha) == 5:
            for x in range(inicioContagem, len(filtro["timestamp"])):

                #Abaixo existe duas formas de exibição. Se estiver em linux comente o primeiro e descomente o segundo
                print(f"{filtro["timestamp"][x]} Uso da CPU: {filtro["CPU"][x]}% || RAM: {filtro["RAM"][x]} Gb || Disco usado: {filtro["Disco"][x]} Gb || Pacotes Enviados: {filtro["PacotesEnv"][x]} || Pacotes Recebidos: {filtro["PacotesRec"][x]}")
                # print(f"{filtro["timestamp"][x]} Uso da CPU: {filtro["CPU"][x]}% || tempo de I/O: {filtro["tempoI/O"][x]} Segundos || RAM: {filtro["RAM"][x]} Gb || Disco usado: {filtro["Disco"][x]} Gb || Pacotes Enviados: {filtro["PacotesEnv"][x]} || Pacotes Recebidos: {filtro["PacotesRec"][x]}")
    
        else:
            print("Digite um valor válido!")
            escolhaRecurso()



    def periodoTempo():
        momentoMin_str = input("\nDigite a data/hora minima que deseja nesse formato: (dia/mes/ano hora:minuto): \n")
        momentoMin = datetime.strptime(momentoMin_str, "%d/%m/%Y %H:%M")
        momentoMax_str = input("Digite a data/hora máxima que deseja nesse formato: (dia/mes/ano hora:minuto): \n")
        momentoMax = datetime.strptime(momentoMax_str, "%d/%m/%Y %H:%M")

        filtroPeriodo = df[(df["timestamp"] >= momentoMin) & (df["timestamp"] <= momentoMax)]
        filtroGeral(filtroPeriodo, momentoMin, True)
        time.sleep(2)
        

        


    def minutosAtras():
        minutosAtras = input("\nEscolha de quantos minutos atrás deseja ver: \n")
        ultimosMinX = hora_atual - timedelta(minutes=int(minutosAtras))
        filtroMin = df[df["timestamp"] >= ultimosMinX]
        filtroGeral(filtroMin, 0, False)
        time.sleep(2)




    resposta = perguntar()        
    if int(resposta) == 1:
        minutosAtras()
    elif int(resposta) == 2:
        periodoTempo()
    elif int(resposta) == 3:
        print("Obrigado. Encerrando...")
        time.sleep(1)
        break
    else:
        print("Opção inválida!")
    
        


   
