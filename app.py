import streamlit as st  # Importa o Streamlit para criar a interface web
import pandas as pd  # Importa o Pandas para trabalhar com tabelas e dados

# para rodar use streamlit run app.py

# Configuração de Página
st.set_page_config(page_title="Controle Financeiro", page_icon="💰", layout="wide")  # Configura título, ícone e largura da página

ARQUIVO_MOVIMENTACOES = "dados/movimentacoes.csv"  # Define o caminho do arquivo CSV

df = pd.read_csv(ARQUIVO_MOVIMENTACOES)  # Lê o arquivo CSV e transforma em um DataFrame
df["data"] = pd.to_datetime(df["data"], format="mixed")  # Converte a coluna data para o formato de data


# Cálculos financeiros

total_receitas = df.loc[df["tipo"] == "Receita", "valor"].sum()  # Filtra receitas e soma os valores

total_despesas = df.loc[df["tipo"] == "Despesa", "valor"].sum()  # Filtra despesas e soma os valores

saldo = total_receitas - total_despesas  # Calcula o saldo subtraindo despesas das receitas


# Título
st.title("💰 Sistema de Controle Financeiro Pessoal")  # Mostra o título principal na tela
st.write("Acompanhe suas receitas, despesas e saldo de forma simples")  # Mostra um texto explicativo

col1, col2, col3 = st.columns(3)  # Divide a tela em três colunas

with col1:
    st.metric("💰 Saldo", f"R$ {saldo:,.2f}")  # Mostra o saldo na primeira coluna

with col2:
    st.metric("📈 Receitas", f"R$ {total_receitas:,.2f}")  # Mostra o total de receitas na segunda coluna

with col3:
    st.metric("📉 Despesas", f"R$ {total_despesas:,.2f}")  # Mostra o total de despesas na terceira coluna

# Gráfico de receitas x despesas

st.divider()  # Cria uma linha divisória na página

st.subheader("📊 Resumo financeiro")  # Cria o subtítulo da seção do gráfico

dados_grafico = pd.DataFrame({  # Cria um DataFrame para os dados do gráfico
    "Tipo": ["Receitas", "Despesas"],  # Define os tipos que aparecerão no gráfico
    "Valor": [total_receitas, total_despesas]  # Define os valores de receitas e despesas
})

st.bar_chart(dados_grafico, x="Tipo", y="Valor")  # Cria um gráfico de barras


# Gastos por categoria

st.subheader("💸 Gastos por categoria")  # Cria o subtítulo da seção

despesas = df[df["tipo"] == "Despesa"]  # Filtra o DataFrame deixando somente as despesas

gastos_categoria = despesas.groupby("categoria")["valor"].sum()  # Agrupa as despesas por categoria e soma os valores

st.bar_chart(gastos_categoria)  # Mostra um gráfico com os gastos por categoria

# Cadastro de Movimentação

st.header("➕ Nova movimentação")  # Cria o título da seção de cadastro

with st.form("form_movimentacao"):  # Cria um formulário para cadastrar uma movimentação

    tipo = st.selectbox("Tipo de movimentação", ["Receita", "Despesa"])  # Permite escolher entre Receita e Despesa

    descricao = st.text_input("Descrição", placeholder="Ex.: Salário, supermercado, aluguel...")  # Cria um campo para informar a descrição

    valor = st.number_input("Valor", min_value=0.01, step=0.01, format="%.2f")  # Cria um campo numérico para informar o valor

    categoria = st.selectbox(  # Cria uma caixa de seleção para escolher a categoria
        "Categoria",  # Define o nome do campo
        [  # Lista as categorias disponíveis
            "Alimentação",  # Categoria de alimentação
            "Moradia",  # Categoria de moradia
            "Transporte",  # Categoria de transporte
            "Saúde",  # Categoria de saúde
            "Educação",  # Categoria de educação
            "Lazer",  # Categoria de lazer
            "Trabalho",  # Categoria de trabalho
            "Outros"  # Categoria para outros gastos
        ]
    )
    
    data = st.date_input("Data")  # Cria um campo para selecionar a data
    cadastrar = st.form_submit_button("Cadastrar movimentação")  # Cria o botão para enviar o formulário


# Lista de Movimentação 

st.divider()  # Cria uma linha divisória na página

st.header("📋 Movimentações")  # Cria o título da lista de movimentações

if df.empty:  # Verifica se o DataFrame está vazio

    st.info("Nenhuma movimentação cadastrada.")  # Mostra uma mensagem caso não existam movimentações

else:  # Executa este bloco caso existam movimentações

    filtro_tipo = st.selectbox("Filtrar por tipo", ["Todos", "Receita", "Despesa"])  # Cria um filtro por tipo de movimentação

    filtro_categoria = st.selectbox("Filtrar por tipo", ["Todas"] + sorted(df["categoria"].unique().tolist()))  # Cria um filtro com as categorias existentes

    data_inicial = st.date_input("Data inicial", value=df["data"].min().date())  # Define a data inicial do filtro

    data_final = st.date_input("Data final", value=df["data"].max().date())  # Define a data final do filtro

    df_filtrado = df.copy()  # Cria uma cópia do DataFrame original para aplicar os filtros

    if filtro_tipo != "Todos":  # Verifica se foi escolhido um tipo específico
        df_filtrado = df_filtrado[df_filtrado["tipo"] == filtro_tipo]  # Mantém somente o tipo selecionado

    if filtro_categoria != "Todas":  # Verifica se foi escolhida uma categoria específica
        df_filtrado = df_filtrado[df_filtrado["categoria"] == filtro_categoria]  # Mantém somente a categoria selecionada

    df_filtrado = df_filtrado[  # Filtra o DataFrame de acordo com o período escolhido
        (df_filtrado["data"].dt.date >= data_inicial) &  # Verifica se a data é maior ou igual à data inicial
        (df_filtrado["data"].dt.date <= data_final)  # Verifica se a data é menor ou igual à data final
    ]

    st.dataframe(df_filtrado, use_container_width=True)  # Mostra na tela a tabela com os dados filtrados

# Processamento do Formulário

if cadastrar:  # Verifica se o botão de cadastro foi pressionado
    if not descricao.strip():  # Verifica se a descrição está vazia
        st.error("Informe uma descrição.")  # Mostra uma mensagem de erro
    else:  # Executa caso a descrição esteja preenchida

        novo_id = len(df) + 1  # Cria um novo ID baseado na quantidade de registros

        nova_movimentacao = {  # Cria um dicionário com os dados da nova movimentação
            "id": novo_id,  # Armazena o ID
            "data": data,  # Armazena a data
            "descricao": descricao,  # Armazena a descrição
            "categoria": categoria,  # Armazena a categoria
            "tipo": tipo,  # Armazena se é Receita ou Despesa
            "valor": valor  # Armazena o valor
        }

        df = pd.concat([df, pd.DataFrame([nova_movimentacao])], ignore_index=True)  # Adiciona a nova movimentação ao DataFrame

        df.to_csv(ARQUIVO_MOVIMENTACOES, index=False)  # Salva o DataFrame atualizado no arquivo CSV

        st.success("Movimentação cadastrada com sucesso!")  # Mostra uma mensagem de sucesso
