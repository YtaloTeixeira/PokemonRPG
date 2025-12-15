import time
import pickle
from pokemon import *
from personagem import *


def escolhaInicial(player):
    print(
        "Olá {}! Escolha o Pokemon que irá te acompanhar nesta jornada!".format(player)
    )

    pikachu = PokemonEletrico("Pikachu", lvl=1)
    charmander = PokemonFogo("Charmander", lvl=1)
    squirtle = PokemonAgua("Squitle", lvl=1)

    print("1 - ", pikachu)
    print("2 - ", charmander)
    print("3 - ", squirtle)

    while True:
        escolha = input("Escolha seu Pokemon: ")

        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolhar uma opção válida!")

def salvarJogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!!")
    except Exception as e:
        print("Erro ao salvar o jogo")
        print(e)

def carregarJogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            return player
    except Exception as e:
        print("Erro ao tentar carregar o jogo!")


if __name__ == "__main__":
    print("------------------------")
    print("Bem-vindo ao PokemonRPG!")
    print("------------------------")

    player = carregarJogo()

    if not player:

        nome = input("Qual o seu nome: ")
        player = Player(nome)
        print("Olá {}, este é um mundo habitado por Pokemons. Sua missão é se tornar o maior Mestre Pokemon!".format(player))
        print("Explore, capture e batalhe!")
        player.mostrarDinheiro()

        if player.pokemons:
            print("Estes são seus Pokemons atuais: ")
            player.mostraPokemons()
        else:
            print("Você ainda não tem nenhum Pokemon. Vamos escolher o seu primeiro")
            escolhaInicial(player)

        print("Agora que já escolheu seu primeiro Pokemon. Enfrente seu primeiro inimigo!")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", lvl=1)])
        player.batalhar(gary)
        salvarJogo(player)

    while True:
        print("------------------------")
        print("O que quer fazer agora?")
        print("1 - Explorar mundo")
        print("2 - Batalhar")
        print("3 - Abrir Pokedex")
        print("4 - Salva jogo")
        print("0 - Sair do jogo")
        escolha = input("Digite sua escolha: ")

        if escolha == "1":
            print("Carregando mundo . . .")
            time.sleep(2)
            print("Preparando aventura . . .")
            time.sleep(2.5)
            print("Exploração iniciada!!!")
            time.sleep(4)
            print("Caçando Pokemons selvagens . . .")
            time.sleep(5)
            player.explorar()
            salvarJogo(player)
        elif escolha == "2":
            print("Preparando arena de batalha . . .")
            time.sleep(2)
            print("Arena pronta! Escolhendo seu adversário . . .")
            time.sleep(2)
            inimigo = Inimigo()
            print("Você irá batalhar contra {}".format(inimigo))
            time.sleep(1)
            player.batalhar(inimigo)
            salvarJogo(player)
        elif escolha == "3":
            player.mostraPokemons()

            player.mostrarDinheiro()
        elif escolha == "4":
            print("Salvando jogo . . .")
            time.sleep(1)
            print("Mantenha o terminal aberto!!!")
            time.sleep(3)
            salvarJogo(player)
        elif escolha == "0":
            print("Saindo do jogo . . .")
            time.sleep(0.8)
            break
        else:
            print("Escolha inválida!")
