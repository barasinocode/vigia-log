# Vigia Log

Sistema de análise de logs de autenticação com foco em detecção de atividades suspeitas, classificação de risco e identificação de padrões associados a possíveis incidentes de segurança.

## Objetivo

O Vigia Log foi desenvolvido para analisar eventos de autenticação e identificar comportamentos potencialmente suspeitos.

O projeto busca demonstrar conhecimentos em:

* Python
* Pandas
* análise de dados
* lógica de detecção
* Cybersecurity
* Git e GitHub
* visualização de dados

## Como funciona

O fluxo atual do projeto é:

```text
Logs CSV
   ↓
Limpeza e tratamento
   ↓
Análise dos eventos
   ↓
Aplicação de regras de detecção
   ↓
Cálculo de risco
   ↓
Geração de arquivo processado
   ↓
Análise exploratória
```

## Regras de detecção

Atualmente o Vigia Log possui regras para identificar:

### Tentativa de força bruta

Quando um mesmo endereço IP acumula várias falhas de autenticação, o evento recebe uma pontuação de risco maior.

### Múltiplas contas por IP

Quando um mesmo IP tenta acessar várias contas diferentes, o comportamento é sinalizado como suspeito.

### Possível comprometimento de conta

Quando ocorrem várias falhas consecutivas seguidas por um login bem-sucedido para o mesmo usuário e IP, o evento é marcado como possível comprometimento.

### Login em horário incomum

Eventos realizados em horários considerados atípicos também recebem pontuação adicional.

## Classificação de risco

Os eventos são classificados de acordo com um `risk_score`.

```text
LOW     → baixo risco
MEDIUM  → risco intermediário
HIGH    → alto risco
```

A pontuação considera fatores como:

* falha de autenticação;
* horário incomum;
* quantidade de tentativas falhas;
* quantidade de contas acessadas por um mesmo IP;
* possível login comprometido.

## Resultados atuais

Na versão atual do conjunto de testes:

```text
Total de eventos: 18
Falhas de login: 14

Eventos HIGH: 6
Eventos MEDIUM: 6
Eventos LOW: 6
```

Alertas detectados:

```text
Força bruta: 5
Múltiplas contas por IP: 4
Possível comprometimento: 1
```

IPs com maior quantidade de falhas:

```text
185.22.13.10   → 5 falhas
203.0.113.50   → 4 falhas
198.51.100.25  → 3 falhas
92.100.15.80   → 2 falhas
```

## Estrutura do projeto

```text
vigia-log/
│
├── data/
│   ├── raw/
│   │   └── login_logs.csv
│   │
│   └── processed/
│       └── security_events.csv
│
├── notebooks/
│   └── analysis.py
│
├── src/
│   ├── main.py
│   ├── data_cleaning.py
│   └── detection_rules.py
│
├── sql/
│   ├── create_tables.sql
│   └── queries.sql
│
├── dashboard/
│
├── docs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Tecnologias

* Python
* Pandas
* Matplotlib
* SQL
* Git
* GitHub

## Como executar

Clone o repositório:

```bash
git clone https://github.com/barasinocode/vigia-log.git
```

Entre na pasta:

```bash
cd vigia-log
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

No Windows, ative com:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Execute a análise principal:

```bash
python src\main.py
```

Depois execute a análise exploratória:

```bash
python notebooks\analysis.py
```

## Próximas etapas

* aprimorar a análise exploratória;
* gerar gráficos automaticamente;
* integrar PostgreSQL;
* criar consultas SQL para análise dos eventos;
* desenvolver dashboard;
* evoluir a arquitetura para AWS;
* documentar métricas e resultados no portfólio.

## Status

Projeto em desenvolvimento.

A versão atual já realiza tratamento de logs, aplicação de regras de segurança, classificação de risco e geração de resultados para análise.
