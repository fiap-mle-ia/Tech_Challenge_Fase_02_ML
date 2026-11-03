# Tech Challenge Fase 2: propensão de compra em e-commerce

Pipeline de Machine Learning que estima a **propensão de compra** de um usuário a partir do seu
comportamento de navegação em uma loja online. O foco do desafio é a **Engenharia de ML**:
código limpo, ambiente reproduzível com Poetry, dados versionados com DVC, experimentos
rastreados no MLflow e execução em Docker.

Projeto do **Grupo 28** da pós-graduação em Machine Learning Engineering da POSTECH (FIAP).

> 🚧 **Em construção.** As Etapas 1 e 2 estão montadas. As Etapas 3 e 4 entram nos próximos PRs.

## Dataset

[Online Shoppers Purchasing Intention](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset)
(UCI): **12.330 sessões**, 17 atributos de navegação e o alvo `Revenue`, que indica se a sessão
terminou em compra. Só **1.908 sessões (15,5%)** compraram, então as classes são desbalanceadas.

## Stack

| Ferramenta | Para quê |
|---|---|
| Python 3.14 + **Poetry** | Ambiente e dependências (`pyproject.toml` + `poetry.lock`) |
| **scikit-learn** | Pré-processamento e modelo de classificação |
| **MLflow** | Tracking de experimentos e Model Registry |
| **DVC** | Versionamento do dataset e pipeline reprodutível (`dvc.yaml`) |
| **Docker** | Execução do pipeline em contêiner |
| pytest + ruff | Testes e lint (rodam no GitHub Actions a cada PR) |

## Como rodar

Pré-requisitos: Python 3.14 e [Poetry 2.x](https://python-poetry.org/docs/#installation)
(por exemplo, `pipx install poetry`).

```bash
git clone https://github.com/fiap-mle-ia/Tech_Challenge_Fase_02_ML.git
cd Tech_Challenge_Fase_02_ML
cp .env.example .env
poetry install            # produção + desenvolvimento, nas versões do poetry.lock
poetry run pytest
poetry run ruff check .
```

Para instalar só as dependências de produção (como numa imagem Docker), use
`poetry install --only main`. As variáveis aceitas estão descritas no `.env.example`.

## Estrutura

```
├── configs/params.yaml        # seed, split e hiperparâmetros (lidos pelo DVC e pelo código)
├── data/raw/  data/processed/ # dados versionados pelo DVC (fora do Git)
├── models/                    # saídas do pipeline (DVC)
├── src/propensao_compra/
│   ├── settings.py            # variáveis do .env e leitura do params.yaml
│   ├── logging_setup.py       # logging único, com o nível vindo do LOG_LEVEL
│   ├── data/                  # ingestão e pré-processamento
│   ├── modeling/              # pipeline do scikit-learn, treino e avaliação
│   └── tracking/              # MLflow: tracking e Model Registry
├── tests/                     # inclui test_clean_code.py: funções ≤ 20 linhas e com type hints
├── notebooks/                 # exploração (EDA)
├── docs/                      # Model Card
└── .github/workflows/ci.yml   # ruff + pytest a cada PR
```

## Etapas e responsáveis

| Etapa | Entrega | Responsável |
|---|---|---|
| 1. Clean Code e estrutura | Pastas, ruff, type hints, teste de tamanho das funções | Leandro |
| 2. Ambiente e dependências | Poetry, `poetry.lock`, `.env.example`, CI | Leandro |
| 3a. DVC | `dvc init`, estágios `download` → `preprocess`, dataset versionado | Jônatas |
| 3b. Docker | Dockerfile via Poetry e `docker-compose.yml` com o servidor do MLflow | Matheus |
| 4a. Modelagem | Pipeline do scikit-learn, treino, avaliação e comparação de modelos | Gustavo |
| 4b. MLflow | Tracking das runs, Model Registry e promoção com o alias `champion` | Derek |
| 4c. Entrega | README final, Model Card e vídeo STAR | Todos |

Cada integrante abre um PR a partir de uma branch própria, com os testes do seu módulo.
A contribuição de cada um aparece no histórico de commits e no gráfico de
[contribuidores](https://github.com/fiap-mle-ia/Tech_Challenge_Fase_02_ML/graphs/contributors) do GitHub.

## Integrantes

| Nome | GitHub |
|---|---|
| Derek Seiji Lima Sadakane | [@Derek759](https://github.com/Derek759) |
| Gustavo Eidi Kono Masuno | [@gustavomasuno](https://github.com/gustavomasuno) |
| Jônatas Gomes Alves | [@jonatasgomes](https://github.com/jonatasgomes) |
| Leandro Kersting de Freitas | [@frekele](https://github.com/frekele) |
| Matheus de Souza Gonçalves | [@Mattheus-SG](https://github.com/Mattheus-SG) |
