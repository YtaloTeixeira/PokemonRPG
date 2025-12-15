# Pokemon RPG 🎮

Um jogo de RPG baseado em Pokemon desenvolvido em Python, onde você pode capturar pokemons, batalhar contra inimigos e ganhar PokeCoins!

## 📋 Descrição

Este é um jogo de batalha Pokemon em modo texto onde você assume o papel de um treinador Pokemon. Você pode capturar diferentes tipos de Pokemon, batalhar contra inimigos e gerenciar seus PokeCoins. O jogo possui um sistema completo de save/load para salvar seu progresso.

## 🎯 Funcionalidades

- **Sistema de Save/Load**: Salve e carregue seu progresso usando pickle
- **Sistema de Exploração**: Explore o mundo e encontre Pokemon selvagens (30% de chance)
- **Sistema de Captura**: Capture Pokemon selvagens com 55% de chance de sucesso
- **Sistema de Batalha**: Batalhe contra inimigos aleatórios e seus Pokemon
- **Sistema de Dinheiro**: Ganhe ou perca PokeCoins nas batalhas
- **Escolha Inicial**: Escolha entre Pikachu, Charmander ou Squirtle no início
- **Pokedex**: Visualize todos os seus Pokemon capturados
- **Tipos de Pokemon**: Elétrico, Fogo, Água, Planta, Inseto, Venenoso e Pedra
- **Sistema de Níveis**: Cada Pokemon tem seu próprio nível que afeta ataque e HP
- **Menu Interativo**: Navegue por um menu completo de opções

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x instalado no sistema

### Executando o Jogo

1. Clone ou baixe o repositório
2. Navegue até o diretório do projeto:
   ```bash
   cd pokemonRPG
   ```
3. Execute o arquivo principal:
   ```bash
   python3 main.py
   ```

## 🎮 Como Jogar

### Primeiro Acesso

Na primeira vez que iniciar o jogo:
1. Digite seu nome quando solicitado
2. Você receberá **500 PokeCoins** iniciais
3. Escolha seu Pokemon inicial entre:
   - 1 - Pikachu (Elétrico)
   - 2 - Charmander (Fogo)
   - 3 - Squirtle (Água)
4. Enfrente seu primeiro adversário: Gary e seu Squirtle

### Jogo Salvo

Se você já tiver um jogo salvo, ele será carregado automaticamente mantendo:
- Seus Pokemon
- Seu saldo de PokeCoins
- Todo o seu progresso

### Menu Principal

Após a primeira batalha, você terá acesso ao menu interativo:
 e menu
├── personagem.py     # Classes de Pessoa, Player e Inimigo
├── pokemon.py        # Classes dos Pokemon e seus tipos
├── database.db       # Arquivo de save (gerado automaticamente)
├── .gitignore        # Arquivos ignorados pelo git
- 30% de chance de encontrar Pokemon selvagens
- Se encontrar, você pode tentar capturá-lo
- 55% de chance de captura bem-sucedida
- Pokemon podem escapar durante a captura

**2 - Batalhar**
- Enfrente inimigos aleatórios
- Inimigos podem ter de 1 a 6 Pokemon
- Escolha qual Pokemon usar na batalha
- Pokemon atacam alternadamente até a derrota

**3 - Abrir Pokedex**
- Visualize todos os seus Pokemon capturados
- Veja seu saldo atual de PokeCoins

**4 - Salvar jogo**
- Salve manualmente seu progresso
- Dados salvos no arquivo `database.db`

**0 - Sair do jogo**
- Encerre o jogo
- Lembre-se de salvar no Código

```python
# Criar um jogador
player = Player("Seu Nome")

# Capturar um Pokemon
player.capturar(PokemonEletrico("Pikachu"))

# Ver seus pokemons
player.mostraPokemons()

# Explorar o mundo
player.explorar()

# Batalhar contra um inimigo
inimigo = Inimigo()  # Inimigo aleatório
player.batalhar(inimigo)

# Ver seu saldo
player.mostrarDinheiro()

# Salvar o jogo
salvarJogo(player)

# Carregar o jogo
player = carregarJogo()
```

## 🔧 Personalização do Código

### Modificar main.py:
- Ajustar Pokemon iniciais disponíveis
- Mudar primeiro adversário (Gary)
- Alterar chances de encontrar Pokemon (padrão: 30%)
- Modificar tempo de espera das animações

### Modificar personagem.py:
- Alterar saldo inicial (padrão: 500)
- Mudar valores de ganhos/perdas em batalhas
- Ajustar chance de captura (padrão: 55%)
- Adicionar novos nomes de inimigos na lista NOMES

### Modificar pokemon.py:
- Criar novos tipos de Pokemon
- Ajustar fórmulas de ataque e HP
- Modificar variação de dano (padrão: até 20%)
- Alterar ataques e descrições

## 📝 Notas Importantes

- **Sistema de Save**: Utiliza pickle para serializar o objeto Player
- **Arquivo de Save**: `database.db` é gerado automaticamente
- **Dano Aleatório**: Variação de até 20% no dano de cada ataque
- **HP dos Pokemon**: Calculado como `nível × 15.5`
- **Ataque dos Pokemon**: Calculado como `nível × 5`
- **Chance de Exploração**: 30% de encontrar Pokemon ao explorar
- **Chance de Captura**: 55% de capturar Pokemon encontrado
- **Inimigos Aleatórios**: Podem ter de 1 a 6 Pokemon com níveis variados
- **Auto-Save**: O jogo salva automaticamente após explorações e batalha
- **Fogo**: Ataque Bola de Fogo
- **Água**: Ataque Encharcar
- **Planta**: Ataque Chicote de Vinha
- **Inseto**: Ataque Joaninha
- **Venenoso**: Ataque Cuspe
- **Pedra**: Ataque Pedregulho

### Exemplos de Pokemon:
- Pikachu (Elétrico)
- Charmander (Fogo)
- Squirtle (Água)
- Bulbasaur (Planta)
- Caterpie (Inseto)
- Ekans (Venenoso)
- Rhyhorn (Pedra)

## 🔧 Personalizações

Você pode modificar o arquivo `main.py` para:
- Alterar o nome do jogador
- Começar com Pokemon diferentes
- Criar inimigos com Pokemon específicos
- Ajustar valores de ganhos e perdas

## 🤝 Contribuições

Sinta-se livre para contribuir com melhorias, correções de bugs ou novas funcionalidades!

## Sobre o Projeto

Este projeto foi desenvolvido durante o curso **Python Orientado a Objetos e Automação**, ofertado pela **Solyd Offensive Security**.

Trata-se de um projeto de caráter educacional, com o objetivo de aplicar conceitos de Programação Orientada a Objetos e automação utilizando Python. O código está disponível de forma aberta e pode ser livremente modificado, adaptado e aprimorado para fins de estudo e aprendizado.

