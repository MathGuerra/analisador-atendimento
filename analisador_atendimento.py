import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, confusion_matrix

# Combinamos problemas comuns do atendimento com sentimentos para criar uma base robusta
frases_positivas = [
    "Atendimento excelente, resolveram meu problema de crédito rapidamente.",
    "O atendente foi super educado e me explicou todas as taxas com clareza.",
    "Consegui liberar o limite do meu financiamento muito rápido.",
    "A resolução foi simples e objetiva, estou muito satisfeito com o serviço.",
    "Obrigado pela paciência em explicar o contrato, ótimo suporte.",
    "Sistema muito rápido, renegociei minha dívida sem estresse.",
    "Aprovado meu crédito em tempo recorde, excelente dinâmica.",
    "Suporte nota 10, tiraram todas as minhas dúvidas sobre juros."
] * 15  # Multiplicando para gerar volume (120 linhas)

frases_negativas = [
    "O sistema caiu de novo e não consigo pagar minha parcela do financiamento!",
    "Estou há 40 minutos na linha esperando uma resposta sobre a renegociação.",
    "Achei um absurdo a cobrança de juros desse mês, quero reavaliar isso agora.",
    "Péssima experiência, o suporte não resolveu o bloqueio do meu sistema.",
    "Não aguento mais ligar e a ligação cair no meio do suporte.",
    "Juros abusivos, atendimento péssimo e ninguém resolve meu bloqueio.",
    "Estou tentando cancelar o serviço há horas e os atendentes só transferem.",
    "O aplicativo dá erro toda vez que tento acessar minha conta de financiamento."
] * 15  # Multiplicando para gerar volume (120 linhas)

df = pd.DataFrame({
    'texto': frases_positivas + frases_negativas,
    'sentimento': ['positivo']*len(frases_positivas) + ['negativo']*len(frases_negativas)
})

# 2. TREINAMENTO E AVALIAÇÃO ESTATÍSTICA
X_train, X_test, y_train, y_test = train_test_split(df['texto'], df['sentimento'], test_size=0.3, random_state=42)
modelo = make_pipeline(TfidfVectorizer(), MultinomialNB())
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

print("--- RELATÓRIO DE DESEMPENHO DO MODELO ---")
print(classification_report(y_test, y_pred))

print("\n--- MATRIZ DE CONFUSÃO ---")
print(confusion_matrix(y_test, y_pred))

# 3. MÓDULO DE TRIAGEM INTELIGENTE (O toque de criatividade e negócio)
def processar_atendimento(texto_cliente):
    sentimento = modelo.predict([texto_cliente])[0]
    probabilidade = np.max(modelo.predict_proba([texto_cliente]))
    
    palavras_risco = ["cancelar", "absurdo", "procon", "juros", "bloqueio", "caiu"]
    risco_alerta = any(palavra in texto_cliente.lower() for palavra in palavras_risco)
    
    if sentimento == 'negativo' and risco_alerta:
        acao = " [ALERTA] Prioridade Alta: Encaminhar para Retenção/Ouvidoria"
    elif sentimento == 'negativo':
        acao = " [ATENÇÃO] Fila de Suporte Especializado"
    else:
        acao = " [NORMAL] Fluxo Padrão / Pós-venda"
        
    return {
        'sentimento': sentimento,
        'confianca': f"{probabilidade:.2%}",
        'acao_recomendada': acao
    }

# Testando com um caso real
teste = "O app caiu de novo na hora de pagar a parcela, se cobrar juros vou cancelar!"
resultado = processar_atendimento(teste)
print(f"\nTeste de Triagem: {teste}")
print(f"Resultado: {resultado}")