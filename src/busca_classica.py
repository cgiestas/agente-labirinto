import heapq
from collections import deque

# No BFS, a estrutura é uma lista FIFO!
class TenhoQueExplorar_BFS:
    def __init__(self):
        self.lista_interna = deque()
        
    def adicionar(self, novo_no):
        self.lista_interna.append(novo_no)
        
    def remover(self):
        return self.lista_interna.popleft()
    
    def esta_vazia(self):
        return len(self.lista_interna) == 0
    
    def __len__(self):
        return len(self.lista_interna)
    
# Na DFS, a estrutura é uma pilha!
class TenhoQueExplorar_DFS:
    def __init__(self):
        self.lista_interna = []
        
    def adicionar(self, novo_no):
        self.lista_interna.append(novo_no)
        
    def remover(self):
        return self.lista_interna.pop()
    
    def esta_vazia(self):
        return len(self.lista_interna) == 0
    
    def __len__(self):
        return len(self.lista_interna)
    
# Na busca gulosa, de custo uniforme e a*, a estrutura é uma fila de prioridades!
class TenhoQueExplorar_Prioridade:
    def __init__(self, criterio="total_f"):
        self.lista_interna = []
        self.criterio = criterio
        self.contador = 0 # Serve para desempate caso 2 nós tenham a mesma prioridade
        
    def adicionar(self, novo_no):
        self.contador += 1
        
        if self.criterio == "custo":
            prioridade = novo_no.custo_caminho
        elif self.criterio == "heuristica":
            prioridade = novo_no.heuristica
        else:
            prioridade = novo_no.f
            
        heapq.heappush(self.lista_interna, (prioridade, self.contador, novo_no))
    
    def remover(self):
        tupla_completa = heapq.heappop(self.lista_interna)
        return tupla_completa[2]
    
    def esta_vazia(self):
        return len(self.lista_interna) == 0
    
    def __len__(self):
        return len(self.lista_interna)
    
class No:
    def __init__(self, estado, pai=None, custo_caminho=0, heuristica=0):
        self.estado = estado         # Tupla (linha, coluna)
        self.pai = pai               # Aponta para o No anterior
        self.custo_caminho = custo_caminho  # g(n)
        self.heuristica = heuristica # h(n)
        self.f = custo_caminho + heuristica # f(n) usado no A*

def obter_sucessores(matriz, estado_atual):
    """Olha para cima, baixo, esquerda e direita e retorna as coordenadas livres."""
    linha, coluna = estado_atual
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Cima, Baixo, Esquerda, Direita
    sucessores = []
    
    max_linhas = len(matriz)
    max_colunas = len(matriz[0]) if max_linhas > 0 else 0

    for dl, dc in movimentos:
        n_linha, n_coluna = linha + dl, coluna + dc
        
        if 0 <= n_linha < max_linhas and 0 <= n_coluna < max_colunas:
            if matriz[n_linha][n_coluna] != '#':
                sucessores.append(((n_linha, n_coluna), 1)) 
                
    return sucessores

def calcular_manhattan(ponto_a, ponto_b):
    """Função heurística obrigatória para a busca Gulosa e A*"""
    return abs(ponto_a[0] - ponto_b[0]) + abs(ponto_a[1] - ponto_b[1])

def executar_busca_classica(dados_labirinto, lista_TenhoQueExplorar):
    matriz = dados_labirinto["matriz"]
    inicio = dados_labirinto["inicio"]
    objetivo = dados_labirinto["objetivo"] 
    
    no_inicial = No(
        estado=inicio, 
        pai=None, 
        custo_caminho=0, 
        heuristica=calcular_manhattan(inicio, objetivo)
    )
    
    lista_TenhoQueExplorar.adicionar(no_inicial)
    
    explorados = set()
    
    # Controle para otimização do BFS / evitar redundância na fronteira
    inseridos_fronteira = {inicio}
    
    # Métricas para o relatório
    nos_expandidos = 0
    nos_explorados = 1 # O inicial já foi gerado
    max_elementos_fronteira = len(lista_TenhoQueExplorar)
    
    while not lista_TenhoQueExplorar.esta_vazia():
        no_atual = lista_TenhoQueExplorar.remover()
        
        if no_atual.estado == objetivo:
            caminho = []
            no_aux = no_atual
            while no_aux is not None:
                caminho.append(no_aux.estado)
                no_aux = no_aux.pai
            caminho.reverse()
            
            return {
                "sucesso": True,
                "caminho": caminho,
                "custo": no_atual.custo_caminho,
                "passos": len(caminho) - 1,
                "expandidos": nos_expandidos,
                "explorados": nos_explorados,
                "fronteira_max": max_elementos_fronteira
            }

        if no_atual.estado not in explorados:
            explorados.add(no_atual.estado)
            nos_expandidos += 1
            
            for proximo_estado, custo_movimento in obter_sucessores(matriz, no_atual.estado):
                # Para algoritmos informados/UCS, avaliamos ao expandir. 
                # Para BFS/DFS puro, evitar reinserção poupa memória drástica.
                if proximo_estado not in explorados:
                    if isinstance(lista_TenhoQueExplorar, TenhoQueExplorar_BFS) and proximo_estado in inseridos_fronteira:
                        continue
                        
                    novo_g = no_atual.custo_caminho + custo_movimento
                    novo_h = calcular_manhattan(proximo_estado, objetivo)
                    
                    no_filho = No(
                        estado=proximo_estado,
                        pai=no_atual,
                        custo_caminho=novo_g,
                        heuristica=novo_h
                    )
                    
                    lista_TenhoQueExplorar.adicionar(no_filho)
                    inseridos_fronteira.add(proximo_estado)
                    nos_explorados += 1
                    
            # A medição correta do tamanho máximo deve ocorrer logo após as inserções da rodada
            if len(lista_TenhoQueExplorar) > max_elementos_fronteira:
                max_elementos_fronteira = len(lista_TenhoQueExplorar)
                    
    return {
        "sucesso": False, 
        "expandidos": nos_expandidos, 
        "explorados": nos_explorados, 
        "fronteira_max": max_elementos_fronteira
    }