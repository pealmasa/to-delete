# studio-template

> Template base para novos projectos

---

## Pré-requisitos

- Python 3.12+
- PostgreSQL 16+
- [Node.js 24+ — se fullstack]

## Instalação

```bash
# Clonar o repositório
git clone <repo-url>
cd <repo>

# Instalar dependências Python
pip install -e ".[dev]"

# Copiar e configurar variáveis de ambiente
cp .env.example .env
# Editar .env com os valores reais
```

## Configuração

Todas as variáveis de ambiente estão documentadas em `.env.example`.
Variáveis obrigatórias para arrancar:

| Variável | Descrição |
|---|---|
| `SECRET_KEY` | Chave JWT — gerar com `openssl rand -hex 32` |
| `DATABASE_URL` | Connection string PostgreSQL |

## Utilização

```bash
# Dev server
uvicorn app.main:app --reload

# Testes
pytest

# Lint + format
ruff check . && ruff format .

# Type check
mypy .
```

## API

Documentação interactiva disponível em `/docs` (Swagger UI) e `/redoc` em desenvolvimento.

## CI/CD

O template inclui GitHub Actions para:
- **Lint & Type Check** — ruff + mypy
- **Tests & Coverage** — pytest com 80% cobertura mínima
- **Security Scan** — Semgrep SAST + pip-audit

Para adicionar environment variables ao CI ou configurar secrets:
**Ver:** [`docs/ci-environment-variables.md`](docs/ci-environment-variables.md)

## Arquitectura

```
app/
├── api/routes/v1/   # Endpoints HTTP
├── core/            # Config, DB, segurança
├── models/          # SQLAlchemy models
├── schemas/         # Pydantic schemas
├── services/        # Lógica de negócio
└── repositories/    # Acesso à base de dados
```
