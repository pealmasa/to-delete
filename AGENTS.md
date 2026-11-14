# AGENTS.md — [NOME DO PROJECTO]

> **Estado:** Template — preencher via skill `onboard-new-project` após onboarding.
> **Gerado em:** [DATA]
> **Preenchido por:** Alex (onboard-new-project)

---

## Visão do Projecto

[VISÃO DO PRODUTO — o que é, para quem, qual o objectivo desta fase]

---

## Stack

- **Backend:** [linguagem e versão]
- **Framework:** [framework]
- **Base de dados:** [BD e versão]
- **Frontend:** [se aplicável]
- **Outros:** [serviços externos relevantes]

---

## Comandos Essenciais

```bash
# Instalar dependências
pip install -e ".[dev]"        # Python
pnpm install                   # Node (se aplicável)

# Correr testes
pytest                         # Python
pnpm test                      # Node

# Lint e formatação
ruff check . && ruff format .  # Python
pnpm lint                      # Node

# Type check
mypy .                         # Python
pnpm typecheck                 # Node

# Dev server
uvicorn app.main:app --reload  # FastAPI
pnpm dev                       # Next.js
```

---

## Convenções de Código

Os agentes seguem `studio-best-practices/` por defeito.
Documentar aqui apenas desvios específicos deste projecto — ex: naming conventions diferentes, regras de lint customizadas, padrões de código específicos.

---

## Agentes e Tiers

| Label | Agente | Tipo de tarefa |
|---|---|---|
| `tier:senior` | Alex (Dev Senior) | Features complexas, arquitectura, LLM integration |
| `tier:junior` | Zara (Dev Junior) | CRUD simples, small fixes, boilerplate |
| `security` | Sam (Security) | Revisão de PRs com auth/dados sensíveis |
| — | Rita (QA) | Testes e2e — activada pelo CTO quando necessário |
| — | Dani (DevOps) | Infra/CI — activada pelo CTO quando necessário |
| — | Gil (Docs) | Documentação — activada após features merged |

---

## Fluxo de PR

1. CTO cria Issue com label `tier:senior` ou `tier:junior`
2. CTO trigga o agente via Copilot Coding Agent ou Copilot CLI
3. Agente cria branch, implementa, abre PR como draft
4. CTO revê e faz merge
5. Gil actualiza docs após merge (se necessário)

---

## Prefixo de Agente (obrigatório)

Todos os commits e PR titles devem seguir o formato:
```
<type>(<scope>)[<agent>]: <description>
```

**Regra:**
- Se um **agente Helo** executa (via `copilot --agent <name> -p "..."`): usar o prefixo do **executor**
- Se o **Copilot Coding Agent** ou **CTO** executa: usar o prefixo do agente cujo **domínio** corresponde ao trabalho

| Tipo de trabalho | Prefixo |
|---|---|
| Features, fixes, refactoring, architecture | `[alex]` |
| CRUD simples, boilerplate, small fixes | `[zara]` |
| CI/CD, infra, Docker, deploy | `[dani]` |
| Security reviews, audits, vulnerability fixes | `[sam]` |
| Testes e2e, integração, test plans | `[rita]` |
| Documentação, changelogs, READMEs | `[gil]` |

> Ver `studio-best-practices/git.md` secção 3.1 para regra completa.

---

## Segurança

- Nunca commitar secrets — usar variáveis de ambiente (`.env.example` documenta todas)
- Semgrep corre automaticamente em cada PR
- Dependabot activo — Sam tria alertas semanalmente
- PRs com auth/permissões/dados sensíveis obrigatoriamente revistos por Sam

---

## Observabilidade

- **LangFuse project:** [NOME-DO-PROJETO-LANGFUSE]
- Contexto obrigatório em todos os LLM calls: `agent_name` + `project_id` + `issue_id`
- Dashboard: [URL da instância LangFuse]

---

## Módulos Críticos

[Listar módulos que requerem atenção especial — auth, pagamentos, PII, etc.]
[Ou remover esta secção se não aplicável]
