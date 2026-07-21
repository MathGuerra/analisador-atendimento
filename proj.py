import pandas as pd

# Frases simulando interações reais em linha de frente
dados = {
    'texto': [
        "O sistema caiu de novo e não consigo pagar minha parcela do financiamento!",
        "Atendimento excelente, resolveram meu problema de crédito em cinco minutos.",
        "Estou há 40 minutos na linha esperando uma resposta sobre a renegociação.",
        "O atendente foi super educado e me explicou todas as taxas com clareza.",
        "Achei um absurdo a cobrança de juros desse mês, quero reavaliar isso agora.",
        "Consegui liberar o limite do meu crédito rápido, muito boa a dinâmica.",
        "Péssima experiência, o suporte não resolveu o bloqueio do sistema.",
        "Obrigado pela paciência em explicar o contrato de financiamento.",
        "Não aguento mais ligar e a ligação cair no meio do suporte.",
        "A resolução foi simples e objetiva, estou muito satisfeito com o serviço."
    ],
    'sentimento': ['negativo', 'positivo', 'negativo', 'positivo', 'negativo', 'positivo', 'negativo', 'positivo', 'negativo', 'positivo']
}

df = pd.DataFrame(dados)
print(df.head())

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Divisão dos dados em treino (70%) e teste (30%)
X_train, X_test, y_train, y_test = train_test_split(
    df['texto'], df['sentimento'], test_size=0.3, random_state=42
)

# Criação de um pipeline encadeando a vetorização de texto e o classificador
modelo = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Treinamento com os dados de treino
modelo.fit(X_train, y_train)

# Teste prático com uma nova frase inédita
nova_frase = ["Estou esperando uma solução para a minha taxa de juros há horas!"]
previsao = modelo.predict(nova_frase)

print(f"Frase analisada: {nova_frase[0]}")
print(f"Sentimento previsto: {previsao[0]}")
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Divisão dos dados em treino (70%) e teste (30%)
X_train, X_test, y_train, y_test = train_test_split(
    df['texto'], df['sentimento'], test_size=0.3, random_state=42
)

# Criação de um pipeline encadeando a vetorização de texto e o classificador
modelo = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Treinamento com os dados de treino
modelo.fit(X_train, y_train)

# Teste prático com uma nova frase inédita
nova_frase = ["Estou esperando uma solução para a minha taxa de juros há horas!"]
previsao = modelo.predict(nova_frase)

print(f"Frase analisada: {nova_frase[0]}")
print(f"Sentimento previsto: {previsao[0]}")