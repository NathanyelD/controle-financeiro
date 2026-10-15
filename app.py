
import streamlit as st  # Importa o Streamlit para criar a interface web
import pandas as pd  # Importa o Pandas para trabalhar com tabelas e dados
import os  # Importa o módulo para criar pastas e verificar arquivos

# Para rodar use streamlit run app.py

# Configuração de Página
st.set_page_config(page_title="Controle Financeiro", page_icon="💰", layout="wide")  # Configura título, ícone e largura da página

ARQUIVO_MOVIMENTACOES = "dados/movimentacoes.csv"  # Define o caminho do arquivo CSV

os.makedirs("dados", exist_ok=True)  # Cria a pasta dados caso ela não exista

if os.path.exists(ARQUIVO_MOVIMENTACOES):  # Verifica se o arquivo CSV existe
    df = pd.read_csv(ARQUIVO_MOVIMENTACOES)  # Lê o arquivo CSV existente
else:  # Executa caso o arquivo CSV não exista
    df = pd.DataFrame(columns=["id", "data", "descricao", "categoria", "tipo", "valor"])  # Cria uma tabela vazia com as colunas necessárias
    df.to_csv(ARQUIVO_MOVIMENTACOES, index=False)  # Salva a tabela vazia no arquivo CSV

# Preparação dos dados
for coluna in ["id", "data", "descricao", "categoria", "tipo", "valor"]:  # Percorre todas as colunas necessárias
    if coluna not in df.columns:  # Verifica se alguma coluna está faltando
        df[coluna] = pd.NA  # Cria a coluna que estiver faltando

df = df[["id", "data", "descricao", "categoria", "tipo", "valor"]]  # Organiza as colunas na ordem correta
df["data"] = pd.to_datetime(df["data"], errors="coerce", format="mixed")  # Converte a coluna data para o formato de data
df["valor"] = pd.to_numeric(df["valor"], errors="coerce").fillna(0)  # Converte os valores para números e substitui valores inválidos por zero

# Cálculos financeiros
total_receitas = df.loc[df["tipo"] == "Receita", "valor"].sum()  # Filtra receitas e soma os valores
total_despesas = df.loc[df["tipo"] == "Despesa", "valor"].sum()  # Filtra despesas e soma os valores
saldo = total_receitas - total_despesas  # Calcula o saldo subtraindo despesas das receitas

# Título
st.title("💰 Sistema de Controle Financeiro Pessoal")  # Mostra o título principal na tela
st.write("Acompanhe suas receitas, despesas e saldo de forma simples")  # Mostra um texto explicativo

col1, col2, col3 = st.columns(3)  # Divide a tela em três colunas

with col1:  # Define o conteúdo da primeira coluna
    st.metric("💰 Saldo", f"R$ {saldo:,.2f}")  # Mostra o saldo na primeira coluna

with col2:  # Define o conteúdo da segunda coluna
    st.metric("📈 Receitas", f"R$ {total_receitas:,.2f}")  # Mostra o total de receitas na segunda coluna

with col3:  # Define o conteúdo da terceira coluna
    st.metric("📉 Despesas", f"R$ {total_despesas:,.2f}")  # Mostra o total de despesas na terceira coluna

# Gráfico de receitas x despesas
st.divider()  # Cria uma linha divisória na página
st.subheader("📊 Resumo financeiro")  # Cria o subtítulo da seção do gráfico

dados_grafico = pd.DataFrame({"Tipo": ["Receitas", "Despesas"], "Valor": [total_receitas, total_despesas]})  # Cria uma tabela com os totais de receitas e despesas
st.bar_chart(dados_grafico, x="Tipo", y="Valor")  # Cria um gráfico de barras

# Gastos por categoria
st.subheader("💸 Gastos por categoria")  # Cria o subtítulo da seção
despesas = df[df["tipo"] == "Despesa"]  # Filtra o DataFrame deixando somente as despesas

if despesas.empty:  # Verifica se existem despesas cadastradas
    st.info("Nenhuma despesa cadastrada.")  # Mostra uma mensagem caso não existam despesas
else:  # Executa caso existam despesas cadastradas
    gastos_categoria = despesas.groupby("categoria")["valor"].sum()  # Agrupa as despesas por categoria e soma os valores
    st.bar_chart(gastos_categoria)  # Mostra um gráfico com os gastos por categoria

# Cadastro de Movimentação
st.header("➕ Nova movimentação")  # Cria o título da seção de cadastro

with st.form("form_movimentacao"):  # Cria um formulário para cadastrar uma movimentação
    tipo = st.selectbox("Tipo de movimentação", ["Receita", "Despesa"])  # Permite escolher entre Receita e Despesa
    descricao = st.text_input("Descrição", placeholder="Ex.: Salário, supermercado, aluguel...")  # Cria um campo para informar a descrição
    valor = st.number_input("Valor", min_value=0.01, step=0.01, format="%.2f")  # Cria um campo numérico para informar o valor
    categoria = st.selectbox("Categoria", ["Alimentação", "Moradia", "Transporte", "Saúde", "Educação", "Lazer", "Trabalho", "Outros"])  # Permite escolher a categoria
    data = st.date_input("Data")  # Cria um campo para selecionar a data
    cadastrar = st.form_submit_button("Cadastrar movimentação")  # Cria o botão para enviar o formulário

# Processamento do Formulário
if cadastrar:  # Verifica se o botão de cadastro foi pressionado
    if not descricao.strip():  # Verifica se a descrição está vazia
        st.error("Informe uma descrição.")  # Mostra uma mensagem de erro
    else:  # Executa caso a descrição esteja preenchida
        ids_validos = pd.to_numeric(df["id"], errors="coerce").dropna()  # Obtém os IDs existentes e remove valores vazios
        novo_id = int(ids_validos.max()) + 1 if not ids_validos.empty else 1  # Cria um novo ID sem repetir os existentes
        nova_movimentacao = pd.DataFrame([{"id": novo_id, "data": data, "descricao": descricao.strip(), "categoria": categoria, "tipo": tipo, "valor": valor}])  # Cria uma tabela com os dados da nova movimentação
        df = pd.concat([df, nova_movimentacao], ignore_index=True)  # Adiciona a nova movimentação ao DataFrame
        df.to_csv(ARQUIVO_MOVIMENTACOES, index=False)  # Salva as movimentações atualizadas no arquivo CSV
        st.success("Movimentação cadastrada com sucesso!")  # Mostra uma mensagem de sucesso
        st.rerun()  # Atualiza a página para mostrar os dados novos

# Lista de Movimentações
st.divider()  # Cria uma linha divisória na página
st.header("📋 Movimentações")  # Cria o título da lista de movimentações

if df.empty:  # Verifica se o DataFrame está vazio
    st.info("Nenhuma movimentação cadastrada.")  # Mostra uma mensagem caso não existam movimentações
else:  # Executa caso existam movimentações
    filtro_tipo = st.selectbox("Filtrar por tipo", ["Todos", "Receita", "Despesa"])  # Cria um filtro por tipo de movimentação
    filtro_categoria = st.selectbox("Filtrar por categoria", ["Todas"] + sorted(df["categoria"].dropna().unique().tolist()))  # Cria um filtro com as categorias existentes
    datas_validas = df["data"].dropna()  # Seleciona as datas válidas para os filtros

    if datas_validas.empty:  # Verifica se existem datas válidas
        df_filtrado = df.copy()  # Cria uma cópia dos dados sem aplicar filtros de data
    else:  # Executa caso existam datas válidas
        col_data1, col_data2 = st.columns(2)  # Divide a área de datas em duas colunas

        with col_data1:  # Define o conteúdo da primeira coluna de datas
            data_inicial = st.date_input("Data inicial", value=datas_validas.min().date())  # Permite escolher a data inicial do filtro

        with col_data2:  # Define o conteúdo da segunda coluna de datas
            data_final = st.date_input("Data final", value=datas_validas.max().date())  # Permite escolher a data final do filtro

        df_filtrado = df.copy()  # Cria uma cópia do DataFrame original para aplicar os filtros

        if data_inicial <= data_final:  # Verifica se a data inicial não é posterior à data final
            df_filtrado = df_filtrado[(df_filtrado["data"].dt.date >= data_inicial) & (df_filtrado["data"].dt.date <= data_final)]  # Filtra as movimentações pelo período escolhido
        else:  # Executa caso a data inicial seja posterior à data final
            st.error("A data inicial não pode ser maior que a data final.")  # Mostra uma mensagem de erro
            df_filtrado = df_filtrado.iloc[0:0]  # Deixa a tabela vazia até as datas serem corrigidas

    if filtro_tipo != "Todos":  # Verifica se foi escolhido um tipo específico
        df_filtrado = df_filtrado[df_filtrado["tipo"] == filtro_tipo]  # Mantém somente o tipo selecionado

    if filtro_categoria != "Todas":  # Verifica se foi escolhida uma categoria específica
        df_filtrado = df_filtrado[df_filtrado["categoria"] == filtro_categoria]  # Mantém somente a categoria selecionada

    st.dataframe(df_filtrado, use_container_width=True, hide_index=True)  # Mostra na tela a tabela com os dados filtrados
