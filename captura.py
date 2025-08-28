import psutil as ps
import pandas as pd
import time
from datetime import datetime


dados = {
    "timestamp": [],
    "usuario": [],
    "CPU": [],
    #descomente a linha abaixo se estiver no linux
    # "tempoI/O": [],
    "RAM": [],
    "Disco": [],
    "PacotesEnv": [],
    "PacotesRec": []
}


def obter_uso():
    cpu = ps.cpu_times(percpu=False)
    cpuPercent = ps.cpu_percent(interval=1)
    RAM = ps.virtual_memory()
    disco = ps.disk_usage('/')
    rede = ps.net_io_counters(pernic=False, nowrap=True)
    usuario = ps.users()
    user = usuario[0].name
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')




    dados["timestamp"].append(timestamp)
    dados["usuario"].append(user)
    dados["CPU"].append(cpuPercent)
    dados["RAM"].append(round(RAM.used / 1024 ** 3))
    dados["Disco"].append(round(disco.used / 1024 ** 3))
    dados["PacotesEnv"].append(rede.packets_sent)
    dados["PacotesRec"].append(rede.packets_recv)
    
    #Descomente a linha abaixo se estiver em um linux
    # dados["tempoI/O"].append(cpu.iowait)



def salvar_csv():
    df = pd.DataFrame(dados)
    df.to_csv("coletaGeralOTS.csv", encoding="utf-8", index=False)



def monitoramento():
    try:
        while True:
            obter_uso()

            #Abaixo existe duas formas de exibição. Se estiver em linux comente o primeiro e descomente o segundo
            print(f"\nData/Hora: {dados['timestamp'][-1]} \nUsuário: {dados["usuario"][-1]} \nUso da CPU: {dados["CPU"][-1]}% \nRAM: {dados["RAM"][-1]} Gb \nDisco usado: {dados["Disco"][-1]} Gb \nPacotes Enviados: {dados["PacotesEnv"][-1]} \nPacotes Recebidos: {dados["PacotesRec"][-1]}\n")
            # print(f"Data/Hora: {dados['timestamp'][-1]} \nUsuário: {dados["usuario"][-1]} \nUso da CPU: {dados["CPU"][-1]}% \nTempo de I/O: {dados["tempoI/O"][-1]}s \nRAM: {dados["RAM"][-1]} Gb \nDisco usado: {dados["Disco"][-1]} Gb \nPacotes Enviados: {dados["PacotesEnv"][-1]} \nPacotes Recebidos: {dados["PacotesRec"][-1]}")

            salvar_csv()
            time.sleep(5)

    except KeyboardInterrupt:
        resposta = input(str("\nVocê deseja parar o monitoramento? (s/n): ")).strip().lower()
        if resposta == 's':
            print("\nMonitoramento finalizado.")
        elif resposta == 'n':
            print("\nO monitoramento continuará.")
            monitoramento()
        else:
            print("\nOpção inválida. Monitoramento continuará.")
            monitoramento()
monitoramento()
