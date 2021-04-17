# CES22_PlantsVsZombies
Recreating the game Plants vs Zombies

## SETUP

### Criar Ambiente virtual no python
  ```
  python3 -m venv venv
  ```

### Acessar Ambiente virtual no Windows
  ```
  cd venv/Scripts/
  ./activate
  ```

### Acessar Ambiente virtual no Ubuntu
  ```
  source venv/bin/activate
  ```

### Instalação de dependências do projeto (Listadas no arquivo requirements.txt)
  ```
  pip install -r requirements.txt
  ```
#### Lembre-se de entrar no ambiente virtual antes de instalar as dependências

### Instalação de novas dependências
  ```
  pip install <nome_da_dependencia>
  ```
#### Atualizar o arquivo requirements.txt (Dentro do ambiente Virtual)
  ```
  pip freeze > requirements.txt
  ```

## O JOGO
O jogo é baseado no famoso jogo "Plants Vs Zombies", porém modificado para uma realizade de pandemia da Covid-19, onde as plantas são os médicos e profissionais da saúde, defendendo a população do vírus, de suas variantes e de outras pessoas contagiadas, estes substituindo o papel dos zumbis.

### Personagens

#### Defensores:
Os defensores do jogo são:
- Médicos
- Máscaras
- Álcool e Gel
- Enfermeiros

#### Atacantes:
Os atacantes do jogo são:
- Vírus da Covid-19
- Variantes da Covid-19
- Pessoas Contagiadas

## INICIAR A APLICAÇÃO/JOGO

- Para iniciar o jogo, rode o arquivo main.py.