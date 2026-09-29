# 🎨 Visão da Interface

O **Controle Financeiro** não será apenas uma tela para cadastrar receitas e despesas. A ideia é construir uma interface que funcione como um **painel financeiro pessoal**, permitindo visualizar rapidamente a situação financeira e, ao mesmo tempo, acessar os detalhes das movimentações.

A interface deve ser **simples, moderna e organizada**, evitando excesso de informações na tela.

---

## 🖥️ Tela principal — Dashboard

Ao abrir o sistema, o usuário será recebido por um **Dashboard**, que funcionará como a página inicial do Controle Financeiro.

A primeira coisa que o usuário deverá conseguir entender é:

> **"Como está minha vida financeira neste momento?"**

Para isso, a parte superior da tela terá alguns cards com os principais indicadores.

### 💰 Saldo atual

Um card de destaque mostrando:

```text
SALDO ATUAL

R$ 2.450,00
```

O saldo será calculado através da diferença entre todas as receitas e despesas registradas.

---

### 📈 Receitas

Card mostrando quanto entrou no período selecionado:

```text
RECEITAS

+ R$ 4.200,00
```

---

### 📉 Despesas

Card mostrando quanto foi gasto:

```text
DESPESAS

- R$ 1.750,00
```

---

### 📊 Resumo

Um quarto card poderá apresentar alguma informação complementar, como:

```text
MOVIMENTAÇÕES

32
```

ou futuramente:

```text
ECONOMIA DO MÊS

58%
```

---

# 📊 Gráficos

Abaixo dos indicadores, o sistema terá uma área dedicada à visualização dos dados.

A ideia é que o usuário consiga entender seus gastos **sem precisar analisar uma tabela inteira**.

### Receitas x Despesas

Um gráfico poderá comparar o total recebido e o total gasto em determinado período.

```text
        Receitas       Despesas

R$ 4000 ████████████████████
R$ 3000 ███████████████
R$ 2000 ██████████
R$ 1000 █████
```

---

### Gastos por categoria

Outro gráfico mostrará onde o dinheiro está sendo gasto.

Exemplo:

```text
🍔 Alimentação     35%
🚗 Transporte      20%
🎮 Lazer           15%
🏠 Moradia         20%
📚 Educação        10%
```

Isso permitirá identificar rapidamente quais categorias representam a maior parte das despesas.

---

# 📋 Movimentações recentes

Na parte inferior do Dashboard haverá uma tabela com as movimentações mais recentes.

Exemplo:

| Data       | Descrição | Categoria   | Tipo    |         Valor |
| ---------- | --------- | ----------- | ------- | ------------: |
| 29/09/2026 | Salário   | Trabalho    | Receita | + R$ 2.500,00 |
| 28/09/2026 | Mercado   | Alimentação | Despesa |   - R$ 180,00 |
| 27/09/2026 | Uber      | Transporte  | Despesa |    - R$ 25,00 |

As receitas e despesas deverão ser visualmente diferenciadas para facilitar a leitura.

---

# ➕ Nova movimentação

O usuário poderá adicionar uma nova movimentação através de um botão de destaque:

```text
+ Nova movimentação
```

Ao clicar, será aberto um formulário.

### Campos

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

O sistema deverá validar os dados antes de salvar.

Por exemplo:

* O valor não pode ser negativo.
* A descrição não deve ficar vazia.
* Uma categoria deve ser selecionada.
* A data deve ser válida.

---

# 🔎 Filtros

O usuário também poderá filtrar suas movimentações.

Exemplo:

```text
Período
[ Setembro de 2026 ▼ ]

Tipo
[ Todos ▼ ]

Categoria
[ Todas ▼ ]
```

Com isso, o Dashboard deverá atualizar os valores e gráficos de acordo com os filtros selecionados.

---

# 📑 Página de movimentações

Além do Dashboard, o sistema terá uma página dedicada exclusivamente às movimentações.

Nela será possível visualizar **todas as transações cadastradas**.

A tabela poderá conter:

```text
Data
Descrição
Categoria
Tipo
Valor
Ações
```

Nas ações, o usuário poderá futuramente:

```text
✏️ Editar
🗑️ Excluir
```

---

# 🧭 Navegação

A interface poderá utilizar uma barra lateral para facilitar a navegação.

```text
┌──────────────────────┐
│ 💰 Controle Financeiro│
│                      │
│ 🏠 Dashboard         │
│ 💸 Movimentações     │
│ 📊 Relatórios        │
│ ⚙️ Configurações     │
│                      │
└──────────────────────┘
```

### Dashboard

Página inicial com:

* Saldo
* Receitas
* Despesas
* Gráficos
* Movimentações recentes

### Movimentações

Página para:

* Visualizar todas as movimentações
* Adicionar movimentações
* Editar registros
* Excluir registros
* Filtrar dados

### Relatórios

Página destinada à análise financeira.

Poderá apresentar:

* Gastos por categoria
* Comparação mensal
* Evolução do saldo
* Total de receitas
* Total de despesas

### Configurações

Área para configurações do sistema.

Funcionalidades futuras poderão incluir:

* Categorias personalizadas
* Preferências da interface
* Exportação dos dados
* Configurações da conta

---

# 🎨 Identidade visual

A interface deverá seguir uma identidade visual **moderna e limpa**, utilizando poucos elementos visuais, mas com boa hierarquia.

A prioridade é que o usuário consiga olhar para a tela e entender sua situação financeira rapidamente.

### Princípios

* Interface limpa
* Pouco texto desnecessário
* Cards para informações importantes
* Gráficos simples de interpretar
* Tabelas organizadas
* Botões claros
* Navegação intuitiva
* Design responsivo

---

# 🚀 Evolução planejada

O projeto será desenvolvido gradualmente.

### Versão 0.1 — Base

* Cadastro de receitas
* Cadastro de despesas
* Categorias
* Datas
* Armazenamento dos dados

### Versão 0.2 — Dashboard

* Saldo atual
* Total de receitas
* Total de despesas
* Movimentações recentes

### Versão 0.3 — Análise

* Gráficos
* Filtros
* Relatórios
* Resumo mensal

### Versão 0.4 — Gerenciamento

* Editar movimentações
* Excluir movimentações
* Categorias personalizadas
* Melhor gerenciamento dos dados

### Versão 1.0 — Sistema completo

A versão 1.0 terá como objetivo entregar uma experiência completa de controle financeiro pessoal, reunindo:

**Dashboard + Movimentações + Relatórios + Filtros + Gerenciamento + Persistência de dados.**

---

## 💡 Ideia principal

O objetivo não é simplesmente criar um programa que registre:

> "Gastei R$ 50."

O objetivo é transformar esses registros em **informação útil**.

O usuário deve conseguir abrir o sistema e descobrir rapidamente:

> **Quanto tenho?**
> **Quanto entrou?**
> **Quanto saiu?**
> **Onde estou gastando?**
> **Como estou evoluindo ao longo do tempo?**

Essa é a ideia central do **Controle Financeiro**.
