# 💰 Controle Financeiro

<p align="center">
  <strong>Transformando registros financeiros em informação útil.</strong>
</p>

<p align="center">
  Um sistema de controle financeiro pessoal desenvolvido para centralizar movimentações, visualizar indicadores e compreender a evolução financeira ao longo do tempo.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow" alt="Status">
  <img src="https://img.shields.io/badge/Python-3.14-blue" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.64-red" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pandas-3.0-green" alt="Pandas">
</p>

---

## 📌 Sobre o projeto

O **Controle Financeiro** nasceu com uma proposta simples:

> **Não apenas registrar dinheiro, mas transformar esses registros em informação.**

A aplicação está sendo construída como um **painel financeiro pessoal**, permitindo registrar receitas e despesas, acompanhar o saldo, analisar gastos por categoria e visualizar a evolução das movimentações.

A ideia é evitar uma experiência baseada apenas em tabelas e números soltos.

Em vez disso, o sistema busca responder rapidamente às principais perguntas relacionadas à vida financeira:

* 💰 Quanto tenho?
* 📈 Quanto entrou?
* 📉 Quanto saiu?
* 💸 Onde estou gastando?
* 📊 Como minha situação financeira está evoluindo?

O projeto está sendo desenvolvido de forma incremental, evoluindo de uma aplicação básica de registro para uma solução completa de acompanhamento financeiro pessoal.

---

# 🎨 Visão da Interface

A interface será construída seguindo três princípios fundamentais:

> **Clareza · Simplicidade · Informação**

O usuário não deve precisar interpretar uma grande quantidade de informações para entender sua situação financeira.

A aplicação será organizada em diferentes níveis de informação, começando pelos indicadores mais importantes e avançando para gráficos, movimentações e análises detalhadas.

---

# 🖥️ Dashboard

O **Dashboard** será o ponto central da aplicação.

Ao acessar o sistema, o usuário deverá conseguir compreender sua situação financeira atual em poucos segundos.

A estrutura será composta por:

```text
┌─────────────────────────────────────────────────────────────┐
│ 💰 Controle Financeiro                                     │
│                                                             │
│  Saldo                 Receitas              Despesas       │
│  R$ 2.450,00           R$ 4.200,00           R$ 1.750,00   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📊 Receitas x Despesas                                    │
│                                                             │
│  ████████████████████                                      │
│  ███████████████                                           │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  💸 Gastos por categoria                                   │
│                                                             │
│  Alimentação   █████████████████                           │
│  Moradia       ██████████                                  │
│  Transporte    ███████                                     │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📋 Movimentações recentes                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

A prioridade será sempre apresentar primeiro aquilo que possui maior relevância para a compreensão financeira.

---

## 💰 Saldo Atual

O saldo será um dos principais indicadores da aplicação.

```text
SALDO ATUAL

R$ 2.450,00
```

Seu cálculo será baseado na diferença entre receitas e despesas:

```text
Saldo = Total de Receitas - Total de Despesas
```

---

## 📈 Receitas

Representará o total de valores recebidos no período analisado.

```text
RECEITAS

+ R$ 4.200,00
```

---

## 📉 Despesas

Representará o total de valores gastos no período analisado.

```text
DESPESAS

- R$ 1.750,00
```

---

## 📊 Indicador complementar

Um espaço adicional poderá ser utilizado para apresentar informações complementares.

Por exemplo:

```text
MOVIMENTAÇÕES

32
```

ou futuramente:

```text
ECONOMIA DO MÊS

58%
```

Esse indicador poderá evoluir conforme novas funcionalidades forem implementadas.

---

# 📊 Visualização de Dados

Números isolados nem sempre são suficientes para compreender um cenário financeiro.

Por isso, o sistema contará com gráficos capazes de transformar os registros em uma representação visual mais fácil de interpretar.

---

## 📈 Receitas × Despesas

O gráfico permitirá comparar os valores recebidos e gastos em determinado período.

```text
        Receitas                  Despesas

R$ 4000 ████████████████████
R$ 3000 ███████████████
R$ 2000 ██████████
R$ 1000 █████
```

A finalidade é permitir uma percepção imediata da relação entre entradas e saídas.

---

## 💸 Gastos por Categoria

O sistema também apresentará a distribuição das despesas entre as categorias.

Exemplo:

```text
🍔 Alimentação      35%
🏠 Moradia          20%
🚗 Transporte       20%
🎮 Lazer            15%
📚 Educação         10%
```

Essa visualização permitirá identificar rapidamente onde está concentrada a maior parte dos gastos.

---

# 📋 Movimentações

As movimentações serão apresentadas de forma estruturada e organizada.

Exemplo:

| Data       | Descrição | Categoria   | Tipo    |             Valor |
| ---------- | --------- | ----------- | ------- | ----------------: |
| 29/09/2026 | Salário   | Trabalho    | Receita | **+ R$ 2.500,00** |
| 28/09/2026 | Mercado   | Alimentação | Despesa |   **- R$ 180,00** |
| 27/09/2026 | Uber      | Transporte  | Despesa |    **- R$ 25,00** |

A diferenciação entre receitas e despesas deverá tornar a leitura rápida e intuitiva.

---

# ➕ Nova Movimentação

O cadastro de uma nova movimentação será realizado através de uma ação de destaque:

```text
+ Nova movimentação
```

O formulário deverá conter:

```text
Tipo
[ Receita ▼ ]

Descrição
[ __________________________ ]

Valor
[ R$ _______________________ ]

Categoria
[ Alimentação ▼ ]

Data
[ 29/09/2026 ]

        [ Cancelar ] [ Salvar ]
```

Antes de armazenar uma movimentação, o sistema deverá validar as informações fornecidas.

### Validações previstas

* Valor não negativo
* Descrição obrigatória
* Categoria válida
* Data válida
* Dados compatíveis com o formato esperado pelo sistema

---

# 🔎 Filtros

Para facilitar a análise, as movimentações poderão ser filtradas por diferentes critérios.

```text
Período
[ Setembro de 2026 ▼ ]

Tipo
[ Todos ▼ ]

Categoria
[ Todas ▼ ]
```

Os filtros deverão permitir analisar subconjuntos específicos dos dados.

Por exemplo:

> Todas as despesas de Alimentação realizadas durante setembro.

Quando aplicável, os indicadores e gráficos do Dashboard deverão refletir os dados filtrados.

---

# 📑 Página de Movimentações

Além do Dashboard, o sistema contará com uma página dedicada ao gerenciamento completo das movimentações.

A estrutura prevista será:

```text
┌────────────┬──────────────┬────────────┬─────────┬────────────┐
│ Data       │ Descrição    │ Categoria  │ Tipo    │ Valor      │
├────────────┼──────────────┼────────────┼─────────┼────────────┤
│ 29/09/2026 │ Salário      │ Trabalho   │ Receita │ + R$ 2.500 │
│ 28/09/2026 │ Mercado      │ Alimentação│ Despesa │ - R$ 180   │
│ 27/09/2026 │ Uber         │ Transporte │ Despesa │ - R$ 25    │
└────────────┴──────────────┴────────────┴─────────┴────────────┘
```

Futuramente, cada registro poderá possuir ações como:

```text
✏️ Editar
🗑️ Excluir
```

---

# 🧭 Navegação

A aplicação poderá utilizar uma navegação lateral para separar as diferentes áreas do sistema.

```text
╭────────────────────────╮
│ 💰 Controle Financeiro │
│                        │
│ 🏠 Dashboard           │
│ 💸 Movimentações       │
│ 📊 Relatórios          │
│ ⚙️ Configurações       │
│                        │
╰────────────────────────╯
```

### 🏠 Dashboard

Visão geral da situação financeira:

* Saldo
* Receitas
* Despesas
* Gráficos
* Movimentações recentes

### 💸 Movimentações

Gerenciamento dos registros:

* Visualização
* Cadastro
* Edição
* Exclusão
* Filtros

### 📊 Relatórios

Área destinada à análise financeira:

* Gastos por categoria
* Comparação mensal
* Evolução do saldo
* Total de receitas
* Total de despesas

### ⚙️ Configurações

Área destinada às configurações do sistema:

* Categorias personalizadas
* Preferências da interface
* Exportação dos dados
* Configurações da conta

---

# 🎨 Identidade Visual

A identidade visual seguirá uma abordagem **minimalista, moderna e funcional**.

O objetivo não é utilizar o máximo de elementos visuais possível, mas utilizar cada elemento com uma finalidade clara.

### Princípios

| Princípio         | Objetivo                                               |
| ----------------- | ------------------------------------------------------ |
| 🧹 Clareza        | Evitar informações desnecessárias                      |
| 📐 Hierarquia     | Destacar o que é mais importante                       |
| 📊 Visualização   | Transformar dados em informação                        |
| 🧭 Navegação      | Facilitar o acesso às funcionalidades                  |
| 📱 Responsividade | Adaptar a interface aos diferentes tamanhos de tela    |
| ⚡ Objetividade    | Reduzir o esforço necessário para interpretar os dados |

A interface deverá priorizar **usabilidade, consistência e legibilidade**.

---

# 🛠️ Tecnologias

A aplicação está sendo desenvolvida utilizando:

| Tecnologia       | Utilização                      |
| ---------------- | ------------------------------- |
| 🐍 **Python**    | Linguagem principal             |
| 🎈 **Streamlit** | Interface da aplicação          |
| 🐼 **Pandas**    | Manipulação e análise dos dados |
| 📄 **CSV**       | Persistência inicial dos dados  |
| 🔀 **Git**       | Controle de versão              |
| 🐙 **GitHub**    | Hospedagem do código            |

---

# 🚀 Roadmap

O desenvolvimento seguirá uma estratégia incremental.

## `v0.1` — Base

Fundação do sistema.

* [x] Cadastro de receitas
* [x] Cadastro de despesas
* [x] Categorias
* [x] Datas
* [x] Armazenamento dos dados

## `v0.2` — Dashboard

Construção da primeira camada de visualização.

* [x] Saldo atual
* [x] Total de receitas
* [x] Total de despesas
* [x] Movimentações recentes

## `v0.3` — Análise

Expansão dos recursos analíticos.

* [x] Gráficos
* [x] Filtros
* [ ] Relatórios
* [ ] Resumo mensal

## `v0.4` — Gerenciamento

Aprimoramento da manipulação dos registros.

* [ ] Editar movimentações
* [ ] Excluir movimentações
* [ ] Categorias personalizadas
* [ ] Melhor gerenciamento dos dados

## `v1.0` — Sistema completo

A primeira versão completa deverá reunir:

```text
Dashboard
     │
     ├── Movimentações
     ├── Relatórios
     ├── Filtros
     ├── Gerenciamento
     └── Persistência de dados
```

O objetivo é entregar uma experiência completa de **controle financeiro pessoal**, mantendo uma interface simples e orientada à informação.

---

# 💡 Filosofia do Projeto

O **Controle Financeiro** parte de uma ideia simples:

> **Dados financeiros só são realmente úteis quando conseguem gerar informação compreensível.**

Registrar:

```text
"Gastei R$ 50."
```

é apenas armazenar um dado.

Entender:

```text
"Quanto gastei?"
"Onde gastei?"
"Quanto entrou?"
"Quanto sobrou?"
"Como meu comportamento financeiro está evoluindo?"
```

é transformar esse dado em informação.

É exatamente essa transformação que orienta o desenvolvimento do projeto.

---

# 🎯 Objetivo

Construir uma aplicação que permita ao usuário **registrar, visualizar, filtrar e analisar suas movimentações financeiras**, evoluindo progressivamente de um simples sistema de registros para um painel completo de acompanhamento financeiro pessoal.

> **Controle Financeiro — registre seus dados. Entenda seus números. Acompanhe sua evolução.**

---

<p align="center">
  Desenvolvido com Python, Streamlit e Pandas.
</p>
