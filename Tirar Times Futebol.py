import random

tamanho_time = int(input("Quantas pessoas irão jogar? "))

jogadores = []

for pessoas in range(1, tamanho_time + 1):
    print(f"Digite os dados do jogador {pessoas}")
    nome = input("Digite o nome: ")
    estrelas = float(input("Qual a quantidade de estrelas do jogador (1 a 5): "))
    posicao = int(input("Digite em qual posição atua o jogador (0 - zagueiro, 1 - atacante): "))
    jogador = {
        "nome": nome,
        "estrelas": estrelas,
        "posicao": posicao
    }
    jogadores.append(jogador)

num_times = int(input("Digite o número de times: "))

random.shuffle(jogadores)

jogadores_totais = len(jogadores)
estrelas_totais_times = sum(jogador["estrelas"] for jogador in jogadores)
media_estrelas = estrelas_totais_times / jogadores_totais 
jogadores_por_times, jogadores_restantes = divmod(jogadores_totais, num_times)

times = [[] for _ in range(num_times)]

dados_jogador = 0
for i in range(num_times):
    estrelas_time = 0
    for _ in range(jogadores_por_times):
        jogador = jogadores[dados_jogador]
        estrelas_time += jogador["estrelas"]
        times[i].append(jogador)
        dados_jogador += 1

    
    while estrelas_time / len(times[i]) < media_estrelas and jogadores_restantes > 0:
        jogador = jogadores[dados_jogador]
        estrelas_time += jogador["estrelas"]
        times[i].append(jogador)
        dados_jogador += 1
        jogadores_restantes -= 1

for i in range(jogadores_restantes):
    times[i].append(jogadores[dados_jogador])
    dados_jogador += 1

for i, time in enumerate(times):
    print("Time", i+1)
    for jogador in time:
        print(jogador["nome"])
    print()
