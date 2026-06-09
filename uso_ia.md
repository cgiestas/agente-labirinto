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
| *Gemini* | *"Preciso que você me ajude a fazer o codigo das buscas locais, você vai me informar o pseudo codigo das buscas em linguagem natural, sem codigo, e eu vou codar as buscas em python."* | *Foi sugerida um pseudocódigo que com passo a passo para codar os algoritmos de busca local* |
| *Gemini* | *me ajuda a fazer a parte visual do robô caminhando pelo labirinto no notebook. quero que mostre ele andando passo a passo e atualizando o mapa na tela pro professor ver o rastro que ele deixou e o que ele já descobriu* | *A ferramenta auxiliou na implementação do sistema de atualização visual em tempo real dentro do Jupyter Notebook utilizando funções de limpeza de console (IPython.display.clear_output). Ela estruturou a lógica de símbolos do mapa, convertendo as matrizes de dados em caracteres visuais limpos e legíveis, inserindo um pequeno atraso de tempo (time.sleep) entre cada movimento do robô. Isso gerou o efeito de animação fluida que permitiu ao grupo e ao professor assistirem ao processo exato de exploração e tomada de decisão do agente online durante a apresentação do trabalho* |

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

Pseudocodigo gerado para auxilio da criação do código em python:

Conforme combinado, zero código de Python aqui. Vou te passar a receita do bolo (o pseudo-código) para você exercitar a lógica e transcrever para a sintaxe do Python.1. Preparação (O Mock e a Vizinhança)Antes de rodar a busca, você precisa de três ferramentas básicas:O Dicionário Falso: Crie uma estrutura de dados que guarde distâncias fixas entre pares de pontos. Exemplo: De 'A' para 'C1' custa 10, de 'C1' para 'C2' custa 5, de 'C2' para 'B' custa 8.A Função de Custo: Ela recebe uma lista (a sua solução atual, por exemplo: A -> C2 -> C1 -> B). A função deve ler essa lista, buscar os valores no seu dicionário falso, somar tudo e retornar o custo total dessa rota.A Função de Vizinhança: Ela recebe a lista da solução atual e sorteia duas posições aleatórias (ignorando o início 'A' e o fim 'B'). Em seguida, inverte os elementos dessas posições e retorna essa nova lista embaralhada. Esse é o seu "vizinho".2. Lógica do Hill-Climbing (Subida de Encosta)Este algoritmo é "guloso" e ansioso: ele só dá um passo se for para melhorar imediatamente.Passo 1: Gere uma solução inicial aleatória e calcule o custo total dela usando sua Função de Custo. Guarde isso como sua solucao_atual e custo_atual.Passo 2: Inicie um loop que vai rodar um número máximo de vezes (ex: 1000 iterações), para evitar que rode infinitamente.Passo 3: Dentro do loop, use a Função de Vizinhança para gerar uma nova rota a partir da solucao_atual. Calcule o custo desse vizinho.Passo 4: Compare. O custo do vizinho é menor que o custo_atual? Se sim, jogue fora a solução antiga e adote o vizinho como a nova solucao_atual. Se não for menor, ignore o vizinho.Passo 5: Repita o ciclo. Ao final do loop, retorne a melhor solução que você encontrou.3. Lógica do Simulated Annealing (Têmpera Simulada)Este algoritmo é mais inteligente porque aceita errar no começo para não ficar preso em falsos atalhos (mínimos locais).Passo 1: Assim como no anterior, gere uma solucao_atual aleatória e calcule seu custo_atual.Passo 2: Defina uma temperatura inicial alta (ex: temperatura = 100.0) e uma taxa de resfriamento (ex: taxa = 0.99).Passo 3: Inicie um loop que roda enquanto a temperatura for maior que zero (ou um limite mínimo como 0.01).Passo 4: Gere um vizinho e calcule o custo dele. Ache a diferença entre o custo do vizinho e o custo atual.Passo 5: Se o vizinho for melhor (custo menor), aceite-o imediatamente como a nova solucao_atual.Passo 6 (O Pulo do Gato): Se o vizinho for pior (custo maior), você não o descarta direto. Você calcula uma probabilidade matemática de aceitação baseada na fórmula $P = e^{-\frac{\Delta C}{T}}$ (onde $\Delta C$ é a diferença de custo e $T$ é a temperatura atual). Sorteie um número aleatório entre 0 e 1; se esse número for menor que $P$, você aceita a solução pior.Passo 7: Multiplique a temperatura pela taxa de resfriamento para "esfriar" o sistema. Repita até a temperatura acabar.
            
## 6. Validação e Revisão Humana (Auditoria)
Como o grupo garantiu a corretude do material gerado pela IA? Descreva o processo de revisão:

> *Todo o código sugerido pelas inteligências artificiais foi lido, compreendido e testado individualmente pela equipe. Realizamos adequações para que as variáveis seguissem o padrão de nomenclatura do nosso projeto e testamos os algoritmos nos mapas obrigatórios (mapa1.txt e mapa2.txt) para garantir a consistência das saídas em CSV. O texto gerado para o relatório foi revisado e cruzado com as definições apresentadas nos materiais da disciplina para evitar alucinações teóricas.*

## 7. Erros da IA

Durante a Integração da Busca classíca e busca local, implementando visualmente no Notebook Jupyter houve um problema de váriavel criada no Notebook Jupyter que não comunicava com a variavel local no arquivo em python da busca local. Tentamos utilizar o Gemini para corrigir este problema durante cerca de 2h, fazendo diversos testes e debugs no Jupyter e no código, após uma série de modificações não terem surtido efeito, optamos por voltar a estaca 0 do problema, quando notamos ele no codigo, sem as orientações propostas pelo Gemini e consultar o ChatGPt para avaliar o problema, após a primeira avaliação do GPT, ele nos deu 90% de certeza que o problema seria esse problema da variavel local não ser atualizada. Após correção no código vinculando as 2 variáveis no jupyter, o problema foi resolvido, em cerca de 10 minutos utilizando o ChatGPT

Enquanto realizávamos o debug da busca clássica, ao tentar importar o mapa 1 que está localizado em outra pasta fora da pasta src, a inteligência artificial Gemini sugeriu que fossem criadas variáveis para armazenar o caminho da pasta, o que seria redundante, uma vez que para um projeto de pequena escala, consideramos mais fácil atribuir o nome do mapa diretamente a variável labirinto_teste. Portanto, essa sugestão foi rejeitada.

---

