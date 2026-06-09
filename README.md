# Agente Labirinto 🧩

Este projeto implementa agentes de busca para resolução de labirintos. Ele contém algoritmos de **busca clássica** e **busca local** desenvolvidos em Python, além de mapas de teste e um Jupyter Notebook para leitura e manipulação dos ambientes.

## 📁 Estrutura do Projeto

* `src/`: Contém os códigos-fonte dos algoritmos de busca (`busca_classica.py` e `busca_local.py`).
* `mapas/`: Arquivos de texto representando diferentes labirintos (`mapa1.txt`, `mapa2.txt`, `mapa3.txt`, `mapaGrande.txt`).
* `leitor_mapa.ipynb`: Jupyter Notebook contendo a lógica de leitura e visualização dos mapas.
* `requirements.txt`: Lista de dependências Python necessárias para rodar o projeto.
* `resultados_busca_local.csv`: Dados exportados com os resultados das execuções dos algoritmos.
* `uso_ia.md`: Documentação descrevendo o uso de ferramentas de IA durante o desenvolvimento.

## 🚀 Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

## 🛠️ Passos para Clonagem e Instalação

Siga o passo a passo abaixo para configurar o projeto no seu ambiente local:

### 1. Clonar o repositório
Abra o seu terminal (ou prompt de comando) e execute:

```git clone [https://github.com/cgiestas/agente-labirinto.git](https://github.com/cgiestas/agente-labirinto.git)```

### 2. Acessar a pasta do projeto
Entre no diretório que acabou de ser criado:

```cd agente-labirinto```
### 3. Criar e ativar um Ambiente Virtual (Recomendado)
Criar um ambiente virtual (venv) isola as dependências do projeto do resto do seu sistema.

No Linux / macOS:

```python3 -m venv venv```
```source venv/bin/activate```

No Windows:

```python -m venv venv```
```venv\Scripts\activate```

### 4. Instalar as dependências
Com o ambiente virtual ativado, instale os pacotes listados no arquivo requirements.txt:

```pip install -r requirements.txt```
## 💻 Como executar
Após a instalação bem-sucedida, você poderá rodar os scripts de busca disponíveis na pasta src/:

Para rodar a busca clássica:

```python src/busca_classica.py```
Para rodar a busca local:

```python src/busca_local.py```
Para abrir o Notebook de mapas:
Se desejar visualizar o leitor de mapas, inicie o Jupyter na raiz do projeto:

```jupyter notebook leitor_mapa.ipynb```
