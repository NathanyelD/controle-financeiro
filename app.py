import streamlit as st
import pandas as pd


# Configuração de Página
st.set_page_config(page_title="Controle Financeiro", page_icon="💰", layout="wide")

ARQUIVO_MOVIMENTACOES = "dados/movimentacoes.csv"

df = pd.read_csv(ARQUIVO_MOVIMENTACOES)
df["data"] = pd.to_datetime(df["data"], format="mixed")

# Cálculos financeiros

total_receitas = df.loc[df["tipo"] == "Receita", "valor"].sum()

total_despesas = df.loc[df["tipo"] == "Despesa", "valor"].sum()

saldo = total_receitas - total_despesas


# Título
st.title("💰 Sistema de Controle Financeiro Pessoal")
st.write("Acompanhe suas receitas, despesas e saldo de forma simples")  

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Saldo", f"R$ {saldo:,.2f}")

with col2:
    st.metric("📈 Receitas", f"R$ {total_receitas:,.2f}")

with col3:
    st.metric("📉 Despesas", f"R$ {total_despesas:,.2f}")

# Gráfico de receitas x despesas

st.divider()

st.subheader("📊 Resumo financeiro")

dados_grafico = pd.DataFrame({
    "Tipo": ["Receitas", "Despesas"],
    "Valor": [total_receitas, total_despesas]
})

st.bar_chart(dados_grafico, x="Tipo", y="Valor")


# Gastos por categoria

st.subheader("💸 Gastos por categoria")

despesas = df[df["tipo"] == "Despesa"]

gastos_categoria = despesas.groupby("categoria")["valor"].sum()

st.bar_chart(gastos_categoria)

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