# Desafio: Prompt Engineering - Rocketseat

Este repositório contém a resolução do desafio de Prompt Engineering.

## Questão 1: Ray Tracing
**Técnica utilizada:** Atribuição de Papel e Cadeia de Pensamento (Chain-of-Thought).
**Prompt:** Atue como um especialista em computação gráfica. Explique, passo a passo, o processo matemático e físico que o algoritmo de Ray Tracing utiliza para calcular a cor final de um único pixel, considerando a interseção do raio, fontes de luz e propriedades do material (reflexão/refração).
**Resposta gerada:** 

O Ray Tracing simula o comportamento físico da luz, mas de forma inversa: em vez de seguir os raios do sol até o olho, seguimos o caminho do olho até a cena.
1. Geração do Raio Primário (Eye Ray)

O processo começa na "câmera" (o olho do observador). Para cada pixel da tela, traçamos um vetor que parte da origem da câmera e passa pelo centro do pixel no plano da imagem, projetando-se para dentro da cena 3D.

    Matemática: O raio é definido por uma equação paramétrica: P(t)=O+tD, onde O é a origem, D é a direção do vetor e t é a distância.

2. Teste de Interseção

O algoritmo percorre os objetos da cena (esferas, triângulos, malhas) para encontrar qual deles o raio atinge primeiro.

    Cálculo: Resolve-se um sistema de equações entre a reta do raio e a superfície do objeto. Se for uma esfera, por exemplo, usamos a fórmula quadrática para encontrar o menor valor de t positivo.

3. Cálculo das Normais e Propriedades da Superfície

Ao atingir um ponto P, precisamos saber para onde a superfície está "olhando". Calculamos o vetor normal (n) naquele ponto exato. Esse vetor é crucial para determinar como a luz vai bater e refletir.
4. Iluminação Direta e Sombras (Shadow Rays)

Neste ponto, o algoritmo lança um novo raio (chamado shadow ray) em direção a cada fonte de luz da cena.

    Se o raio atingir algo antes da luz: O pixel está em sombra.

    Se o caminho estiver livre: Calculamos a contribuição da luz usando modelos como o de Phong ou Lambert, que levam em conta o ângulo entre a luz e a normal (cosθ).

5. Reflexão e Refração (Raios Secundários)

Dependendo do material do objeto, novos raios são gerados:

    Reflexão: Se o objeto for metálico ou espelhado, um raio é refletido seguindo a lei da reflexão (ângulo de incidência = ângulo de reflexão).

    Refração (Transparência): Se for vidro ou água, o raio entra no objeto, mas muda de direção devido ao Índice de Refração (Lei de Snell).

6. Acúmulo e Cor Final

A cor final do pixel é a soma ponderada de todas essas interações:
Cor=Ambiente+Difusa+Especular+(Cor Refletida×Refletividade)

Esse processo é repetido recursivamente até que o raio saia da cena ou atinja um limite de "pulos".

## Questão 2: Decomposição Numérica
**Técnica utilizada:** Especificação de Formato e Delimitação de Escopo.
**Prompt:** Realize a decomposição numérica completa do número 142.981. Apresente o resultado detalhando as ordens e classes (centena de milhar, dezena de milhar, etc.) e também na forma expandida (soma das multiplicações por potências de 10).
**Resposta gerada:** 

1. Identificação por Classes e Ordens

Na matemática, os números são organizados em grupos de três algarismos chamados classes, e cada posição individual é uma ordem.

    Classe dos Milhares:

        1 - 6ª Ordem: Centena de milhar

        4 - 5ª Ordem: Dezena de milhar

        2 - 4ª Ordem: Unidade de milhar

    Classe das Unidades Simples:

        9 - 3ª Ordem: Centena

        8 - 2ª Ordem: Dezena

        1 - 1ª Ordem: Unidade

2. Decomposição Aditiva (Soma de Valores Posicionais)

Esta forma demonstra o valor real que cada algarismo representa dependendo de sua posição:
100.000+40.000+2.000+900+80+1
3. Decomposição por Potências de 10 (Forma Expandida)

Como o nosso sistema é decimal (base 10), cada ordem à esquerda vale 10 vezes mais que a anterior. A decomposição multiplicativa é:
(1×105)+(4×104)+(2×103)+(9×102)+(8×101)+(1×100)

## Questão 3: Análise Comparativa e Contextual
**Técnica utilizada:** (Cruzamento de Literatura com Filosofia Política).
**Prompt:** Analise os personagens da série 'As Crônicas de Gelo e Fogo' sob a ótica da filosofia política de Nicolau Maquiavel em 'O Príncipe'. Identifique pelo menos três personagens cujas ações demonstram o pragmatismo maquiavélico e justifique com exemplos da obra.
**Resposta gerada:**

Na obra de Maquiavel, o governante ideal deve possuir virtù (capacidade e astúcia) para dominar a fortuna (imprevistos), priorizando a estabilidade do poder sobre a moral tradicional. Em Westeros, três personagens exemplificam esse pragmatismo:

    Tywin Lannister: Personifica a máxima de que "é melhor ser temido do que amado". Ao orquestrar o Casamento Vermelho, ele usou uma crueldade pontual (embora imoral) para encerrar uma guerra e consolidar o poder de sua Casa, o que Maquiavel classifica como crueldade "bem usada".

    Petyr 'Mindinho' Baelish: Domina a arte de ser "o leão e a raposa". Sem força militar própria, ele usa a astúcia para manipular a economia e as alianças. Ele entende que a aparência de virtude é mais útil que a própria virtude, servindo a si mesmo enquanto finge ser útil ao reino.

    Daenerys Targaryen: Demonstra a transição do desejo de ser amada para a necessidade de ser temida. Sua decisão de punir severamente os Mestres em Meereen mostra o abandono do idealismo em favor da ordem imposta pelo terror necessário, conforme sugerido em O Príncipe.

## Questão 4: Endpoint FastAPI
**Técnica utilizada:** Contexto Estruturado e Atribuição de Regras de Negócio
**Prompt:** Aja como um desenvolvedor backend sênior. Crie um endpoint utilizando o framework FastAPI em Python que receba um método POST.

    Defina um modelo Pydantic chamado 'Item' com: nome (string, máx 25 caracteres), valor (float) e data (date, que deve ser menor ou igual à data atual).

    Implemente a validação customizada para a data usando a biblioteca 'datetime'.

    No endpoint, após a validação bem-sucedida, adicione um campo 'uuid' gerado dinamicamente usando a biblioteca nativa 'uuid'.

    Retorne o JSON completo do objeto enriquecido. Comente o código explicando a lógica.

**Resposta gerada:**

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from datetime import date
import uuid

app = FastAPI()

# Definição do modelo Pydantic com regras de validação
class Item(BaseModel):
    # nome: string com limite de 25 caracteres
    nome: str = Field(..., max_length=25)
    # valor: número decimal
    valor: float
    # data: objeto do tipo date
    data: date

    # Validação customizada: a data não pode ser futura
    @validator('data')
    def data_nao_pode_ser_futura(cls, v):
        if v > date.today():
            raise ValueError('A data deve ser menor ou igual à data atual')
        return v

@app.post("/items/")
async def create_item(item: Item):
    # Converte o modelo pydantic para um dicionário Python
    item_dict = item.dict()
    
    # Gera um UUID v4 dinamicamente e adiciona ao dicionário
    item_dict["uuid"] = str(uuid.uuid4())
    
    # Retorna o JSON completo conforme solicitado
    return item_dict
