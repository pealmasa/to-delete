# Changelog

All notable changes to this project will be documented in this file.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

> **Rotation:** On major version release, archive previous entries to `docs/changelog-archive/vN.x.md`.
> Keep only `[Unreleased]` + current major version in this file. See `docs/changelog-archive/README.md`.

---

## [Unreleased]

### Added
- `docker-compose.yml` for local PostgreSQL development with healthcheck and localhost-only binding (#47)
- `docs/decisions/README.md` with ADR template and guidelines (#52)
- `docs/changelog-archive/` with rotation practice for growing changelogs (#49)

### Changed
- **CI: Minimal mode — single job, push-only trigger:** Collapsed 5 parallel jobs into 1 sequential job and removed `pull_request` trigger. Reduces ~8 min/run to ~2 min/run (~75% saving). Full config preserved in `.github/workflows/ci.full.yml` for easy restoration.
- CI: migrate from `pip install` to `uv sync --frozen` for deterministic, lockfile-based builds (#53)
- **CI: Security Scan — Semgrep PR-only + pr-title gate:** Semgrep no longer runs on push to develop (already scanned before merge). Added `needs: pr-title` gate. Semgrep reordered before uv setup — it runs in its own container and needs no Python deps.
- **CI: Security Scan — `uvx pip-audit` replaces `uv run pip-audit`:** `uvx` installs pip-audit in an isolated ephemeral env, independent of the project virtualenv. Removes the `uv sync` step before pip-audit entirely — no longer needed.
- **CI: Deploy Staging — `paths-ignore` for `docs/**` and `*.md`:** Documentation-only pushes no longer trigger the staging deploy workflow.
- CI: add `paths-ignore` for `docs/**` and `*.md` to skip unnecessary CI runs (#53)
- CI: add concurrency group with `cancel-in-progress` to avoid duplicate runs (#53)
- CI: notify job deduplicates issues — comments on existing instead of creating new (#53)
- Ruff: extend lint rules with `A` (builtins), `SIM` (simplify), `TCH` (type-checking) (#54)
- `.gitignore`: add audio files, output dirs, and AI tooling exclusions (#54)
- `Settings.secret_key` and `Settings.database_url` now use `SecretStr` — prevents credential exposure in logs/repr (#48)
- `Settings.app_env` now uses `Environment(StrEnum)` instead of plain `str` (#48)

### Security
- Upgrade aiohttp 3.13.3→3.13.5, pygments 2.19.2→2.20.0, litellm 1.82.6→1.83.3 — resolves 13 CVEs (#57)
- CI: add `--ignore-vuln CVE-2025-69872` (diskcache 5.6.3 — no upstream fix available) (#57)
- litellm: relax pin from `==1.82.6` to `>=1.83.0` — safely skips supply-chain-attacked 1.82.7/1.82.8; `uv.lock` pins to 1.83.3 (#57)
- Pin `litellm==1.82.6` to mitigate PyPI supply chain attack (versions 1.82.7 and 1.82.8 compromised by TeamPCP)

### Added
- PR title validation job in CI — enforces `<type>(<scope>)[<owner>]: <description>` format
- Agent prefix convention section in `AGENTS.md` — documents commit/PR prefix rules
- Weekly security audit workflow — verifica dependências (pip-audit), alertas Dependabot, code scanning e secret scanning; cria Issue se forem encontrados problemas (#28)
- `.env.example` — nova secção CI/CD com documentação do `STUDIO_ADMIN_TOKEN` (Fine-Grained PAT, permissões mínimas, password manager)
- `.env.example` — secção de convenções de nomenclatura de secrets (`_EXP_YYYYMMDD` e `_PERMANENT`)

### Fixed
- `setup-labels.yml` HTTP 403 com GITHUB_TOKEN — adicionado `permissions: issues: write` ao job `create-labels` (necessário para `gh label create` via API)
- `credentials-audit.yml` falso positivo em `MISSING_EXP` para `STUDIO_ADMIN_TOKEN` — adicionada excepção explícita; nome fixo imposto pela referência directa no workflow, expiração gerida pelo GitHub nativamente (#37)
- `credentials-audit.yml` multiline `$GITHUB_OUTPUT` truncation — replaced `echo "key=value"` with heredoc format and `$'\n'` for real newlines in string accumulation
- `credentials-audit.yml` missing `GITHUB` exception in `MISSING_EXP` check — `GITHUB_TOKEN` no longer triggers a false-positive alert
- `credentials-audit.yml` silent false green — `gh secret list` agora falha explicitamente (`exit 1`) se o token não tiver scopes correctos, em vez de reportar tudo OK com lista vazia
- `credentials-audit.yml` deduplicação de Issues — workflow verifica se já existe Issue aberta com o mesmo título antes de criar uma nova; se existir, adiciona comentário em vez de duplicar
- `credentials-audit.yml` lista de excepções hardcoded — substituída por convenção `_PERMANENT` (sufixo auto-documentado) em vez de lista de nomes a manter manualmente
- `.env.example` convenção de nomenclatura `STUDIO_ADMIN_TOKEN` — corrigido de `_EXP_YYYYMMDD` (incompatível com referência fixa no workflow) para nome fixo `STUDIO_ADMIN_TOKEN`; expiração gerida pelo GitHub nativamente
- `ci.yml` permissões — `issues:write` movido do nível global para o job `notify` (princípio de menor privilégio) (#40)

---

## [0.1.0] - YYYY-MM-DD

### Added
- Initial project setup from studio-template
