import streamlit as st
import pandas as pd


# Configuração de Página
st.set_page_config(page_title="Controle Financeiro", page_icon="💰", layout="wide")

ARQUIVO_MOVIMENTACOES = "dados/movimentacoes.csv"

df = pd.read_csv(ARQUIVO_MOVIMENTACOES)
df["data"] = pd.to_datetime(df["data"])


# Título
st.title("💰 Sistema de Controle Financeiro Pessoal")
st.write("Acompanhe suas receitas, despesas e saldo de forma simples")  

# Cadastro de Movimentação

st.header("➕ Nova movimentação")

with st.form("form_movimentacao"):

    tipo = st.selectbox("Tipo de movimentação", ["Receita", "Despesa"])

    descricao = st.text_input("Descrição", placeholder="Ex.: Salário, supermercado, aluguel...")

    valor = st.number_input("Valor", min_value=0.01, step=0.01, format="%.2f")

    categoria = st.selectbox(
        "Categoria",
        [
            "Alimentação",
            "Moradia",
            "Transporte",
            "Saúde",
            "Educação",
            "Lazer",
            "Trabalho",
            "Outros"
        ]
    )
    
    data = st.date_input("Data")
    cadastrar = st.form_submit_button("Cadastrar movimentação")


# Lista de Movimentação 

st.divider()

st.header("📋 Movimentações")

if df.empty:

    st.info("Nenhuma movimentação cadastrada.")

else:

    st.dataframe(df, use_container_width=True)

# Processamento do Formulário

if cadastrar:
    if not descricao.strip():
        st.error("Informe uma descrição.")
    else:

        novo_id = len(df) + 1

        nova_movimentacao = {
            "id": novo_id,
            "data": data,
            "descricao": descricao,
            "categoria": categoria,
            "tipo": tipo,
            "valor": valor
        }

        df = pd.concat([df, pd.DataFrame([nova_movimentacao])], ignore_index=True)

        df.to_csv(ARQUIVO_MOVIMENTACOES, index=False)

        st.success("Movimentação cadastrada com sucesso!")