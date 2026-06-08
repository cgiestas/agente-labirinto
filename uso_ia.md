# Auditoria de Uso de Inteligência Artificial (IA)

**Disciplina:** Inteligência Artificial (CSI457)  
**Trabalho Prático 1:** Agente Inteligente em Labirinto  
**Grupo:** Christiane Barros Giestas Soares, Ian Batista Nogueira e Talles Henrique Furtunato Lima 


---

## 1. Declaração Geral

Declaramos que ferramentas de Inteligência Artificial Generativa (como ChatGPT, Gemini, GitHub Copilot, etc.) **foram utilizadas** durante o desenvolvimento deste trabalho, conforme detalhado nas seções a seguir.


## 2. Ferramentas Utilizadas
* **[Gemini Pro e Flash]** 
* **[ChatGPT - Plano gratuito]**

## 3. Propósito e Escopo do Uso
As ferramentas de IA foram utilizadas para as seguintes finalidades:
- Geração de trechos de código e pseudocódigo.
- Auxílio na depuração (debugging) de erros.
- Esclarecimento de conceitos teóricos sobre os algoritmos de busca.
- Revisão ortográfica, gramatical e estruturação do relatório técnico.
- Criação de matrizes de teste/mapas adicionais.


## 4. Histórico de Interações (Exemplos de Prompts)
Abaixo destacamos os principais *prompts* utilizados que tiveram impacto direto no código ou na análise do projeto:

| Ferramenta | Exemplo de Prompt Utilizado | Como o resultado foi aplicado no trabalho |
| :--- | :--- | :--- |
| *Gemini* | *"Escreva um pseudocódigo que implemente as 5 buscas clássicas, por favor"* | *Foi sugerida um pseudocódigo que implementa a estrutura do nó, a fronteira e o algoritmo versátil da busca clássica. Ele foi usado como base para a escrita do primeiro rascunho, que depois foi enviado para a IA para maior refinamento.* |
| *ChatGPT* | *"Quais as diferenças práticas entre o Hill-Climbing clássico e o Simulated Annealing para evitar ótimos locais?"* | *A explicação teórica serviu como base para a redação do item 8 (Análise Crítica) do relatório.* |
| *[Sua IA]* | *[Seu Prompt]* | *[Sua Aplicação]* |

## 5. Exemplos de trechos de códigos gerados pela IA

Prompt 1 - Pseudocódigo
>Funcao Busca_Classica(problema_falso):
    
    // 1. Inicializa o nó raiz com o estado inicial do "contrato"
    no_inicial = Criar_No(
        estado = problema_falso.get_estado_inicial(), 
        pai = Nulo, 
        custo_caminho = 0,
        heuristica = problema_falso.heuristica(problema_falso.get_estado_inicial())
    )
    
    // 2. Inicializa a Fronteira e o Conjunto de Explorados
    fronteira = Inicializar_Estrutura_De_Dados() // <-- AQUI MUDA PARA CADA BUSCA!
    Inserir no_inicial na fronteira
    
    explorados = Conjunto_Vazio()
    
    // Inicialização das métricas obrigatórias
    nos_expandidos = 0
    max_fronteira = 1
    
    // 3. Loop principal da busca
    Enquanto fronteira NAO estiver vazia:
        
        // Atualiza a métrica de tamanho máximo da fronteira
        max_fronteira = Maior_Valor(max_fronteira, Tamanho(fronteira))
        
        // Retira o próximo nó de acordo com a regra do algoritmo
        no_atual = Remover_Da_Fronteira(fronteira)
        
        // Teste de objetivo usando o método do "contrato"
        Se problema_falso.teste_objetivo(no_atual.estado) é Verdadeiro:
            Retornar Sucesso(Caminho = Reconstruir_Caminho(no_atual), Metricas = [nos_expandidos, max_fronteira])
            
        // Adiciona o estado atual aos explorados para evitar loops
        Adicionar no_atual.estado em explorados
        nos_expandidos = nos_expandidos + 1
        
        // 4. Expansão dos nós filhos (Sucessores)
        Para cada (proximo_estado, custo_movimento) em problema_falso.get_sucessores(no_atual.estado):
            
            Se proximo_estado NAO está em explorados E NAO está na fronteira:
                
                // Calcula os custos para o novo nó
                novo_g = no_atual.custo_caminho + custo_movimento
                novo_h = problema_falso.heuristica(proximo_estado)
                
                no_filho = Criar_No(
                    estado = proximo_estado,
                    pai = no_atual,
                    custo_caminho = novo_g,
                    heuristica = novo_h,
                    f = novo_g + novo_h
                )
                
                Inserir no_filho na fronteira
                
    Retornar Falha // Se a fronteira esvaziar e não achar o objetivo

Prompt 2 - Integração do interpretador de mapas ao código de busca clássica 
>*"meu colega fez o interpretador. como posso integrar ele no meu código? estou enferrujada no python. vc pode corrigir o código que eu já fiz, por favor?"*
```
class BuscaClassica(labirinto, lista_TenhoQueExplorar):
    def __innit__(self, no_inicial):
        #implementar depois de ter o interpretador
        pass
    
    lista_TenhoQueExplorar.adicionar(no_inicial)
    explorados = [0]
    expandidos = 0
    max_elementos_fronteira = 1
    
    while lista_TenhoQueExplorar.esta_vazia() == false:
        no_atual = lista_TenhoQueExplorar.remover()
        if labirinto.objetivo(no_atual) == true:
            return (caminho = reconstruir(no_atual)) #add metricas
        if no_atual is not explorados: #como comparar pra ver se está ou não?
            explorados =+ no_atual
            expandidos = expandidos +1
```


Código corrigido pela IA:

```
class No:
    def __init__(self, estado, pai=None, custo_caminho=0, heuristica=0):
        self.estado = estado         # Tupla (linha, coluna)
        self.pai = pai               # Aponta para o No anterior
        self.custo_caminho = custo_caminho  # g(n)
        self.heuristica = heuristica # h(n)
        self.f = custo_caminho + heuristica # f(n) usado no A*

def obter_sucessores(matriz, estado_atual):
    """
    Olha para cima, baixo, esquerda e direita e retorna 
    as coordenadas livres (que não são parede '#') e o custo (1).
    """
    linha, coluna = estado_atual
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Cima, Baixo, Esquerda, Direita
    sucessores = []
    
    # Descobre o limite máximo do labirinto
    max_linhas = len(matriz)
    max_colunas = len(matriz[0]) if max_linhas > 0 else 0

    for dl, dc in movimentos:
        n_linha, n_coluna = linha + dl, coluna + dc
        
        # Garante que o movimento está dentro dos limites da matriz
        if 0 <= n_linha < max_linhas and 0 <= n_coluna < max_colunas:
            # Se a célula não for uma parede, o agente pode passar
            if matriz[n_linha][n_coluna] != '#':
                sucessores.append(((n_linha, n_coluna), 1)) # Retorna ((l, c), custo)
                
    return sucessores

def calcular_manhattan(ponto_a, ponto_b):
    """Função heurística obrigatória para a busca Gulosa e A*"""
    return abs(ponto_a[0] - ponto_b[0]) + abs(ponto_a[1] - ponto_b[1])
```

            
## 6. Validação e Revisão Humana (Auditoria)
Como o grupo garantiu a corretude do material gerado pela IA? Descreva o processo de revisão:

> *Todo o código sugerido pelas inteligências artificiais foi lido, compreendido e testado individualmente pela equipe. Realizamos adequações para que as variáveis seguissem o padrão de nomenclatura do nosso projeto e testamos os algoritmos nos mapas obrigatórios (mapa1.txt e mapa2.txt) para garantir a consistência das saídas em CSV. O texto gerado para o relatório foi revisado e cruzado com as definições apresentadas nos materiais da disciplina para evitar alucinações teóricas.*

---

