import streamlit as st
from analisador_atendimento import processar_atendimento

st.set_page_config(page_title="IA de Triagem - Financiamento", page_icon="🏦")

st.title("🏦 Sistema Inteligente de Triagem e Análise de Sentimento")
st.markdown("Esse protótipo utiliza **NLP (Processamento de Linguagem Natural)** para classificar interações de clientes e direcionar o fluxo de atendimento de forma automatizada.")

# Caixa de texto para o usuário testar
entrada_usuario = st.text_area(
    "Digite uma simulação de mensagem do cliente (ex: dúvida, reclamação, elogio):",
    placeholder="Ex: Estou tentando pagar minha parcela mas o sistema dá erro o tempo todo!"
)

if st.button("Analisar Chamado"):
    if entrada_usuario.strip() != "":
        com_spinner = st.spinner("Analisando sentimento e calculando prioridade...")
        with com_spinner:
            res = processar_atendimento(entrada_usuario)
            
            col1, col2 = st.columns(2)
            with col1:
                if res['sentimento'] == 'positivo':
                    st.success(f"**Sentimento:** Positivo 🟢")
                else:
                    st.error(f"**Sentimento:** Negativo 🔴")
                st.info(f"**Confiança do Modelo:** {res['confianca']}")
            
            with col2:
                st.warning(f"**Ação Recomendada:**\n{res['acao_recomendada']}")
    else:
        st.warning("Por favor, digite algum texto para analisar.")