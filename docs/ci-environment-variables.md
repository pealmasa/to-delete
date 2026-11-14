# CI/CD Environment Variables Guide

This guide explains how to add, modify, and secure environment variables in the CI/CD pipeline.

## Overview

The CI pipeline (`.github/workflows/ci.yml`) uses environment variables for:
- **Database connections** during tests
- **API keys** for external services  
- **Application configuration** (environment, secrets, etc.)

## Current CI Environment Variables

The `tests` job defines these environment variables for the test suite:

```yaml
env:
  DATABASE_URL: postgresql://test:test@localhost:5432/test
  APP_ENV: test
  SECRET_KEY: test-secret-key-not-used-in-production
  LANGFUSE_SECRET_KEY: test-secret
  LANGFUSE_PUBLIC_KEY: test-public
  LANGFUSE_BASE_URL: http://localhost:3000
```

## Adding New Environment Variables

### 1. Update `.env.example`

First, add the variable to `.env.example` with documentation:

```bash
# Description of what this variable does
# How to get the value: URL or command
NEW_VARIABLE=default_or_example_value
```

### 2. Add to CI Workflow

Add the variable to the `env:` block in `.github/workflows/ci.yml`:

```yaml
jobs:
  tests:
    env:
      # Existing variables...
      NEW_VARIABLE: test-value-for-ci
```

### 3. Choose the Right Value Type

| Use Case | Example | When to Use |
|---|---|---|
| **Hardcoded test values** | `APP_ENV: test` | Safe, non-sensitive config |
| **GitHub Secrets** | `API_KEY: ${{ secrets.API_KEY }}` | Sensitive keys, tokens |
| **Service containers** | `DATABASE_URL: postgresql://test:test@localhost:5432/test` | Test database credentials |

## Using GitHub Secrets

For sensitive values (API keys, tokens), use GitHub Secrets:

### 1. Create the Secret

```bash
# Via GitHub CLI
gh secret set API_KEY --body "your-secret-value"

# Or via GitHub UI: Settings > Secrets and variables > Actions > New repository secret
```

### 2. Reference in Workflow

```yaml
env:
  API_KEY: ${{ secrets.API_KEY }}
```

### 3. Document in README

Add to the project README under **Setup** or **Environment Variables**:

```markdown
## Required Secrets

Configure these GitHub Secrets for CI/CD:

- `API_KEY` — Get from [service provider](https://example.com/keys)
- `DEPLOY_TOKEN` — Generate in [deployment platform](https://example.com/tokens)
```

## Security Best Practices

### ✅ Safe for CI
- Test database credentials (disposable)
- Non-sensitive config (`APP_ENV=test`)
- Public URLs and endpoints

### ❌ Use GitHub Secrets
- API keys and tokens
- Production credentials
- Encryption keys
- Any value that appears in logs

### ⚠️ Never Hardcode
- Real database passwords
- Production API keys
- Personal access tokens
- Webhook secrets

## Testing Changes

After adding environment variables:

1. **Test locally** with the new `.env.example` values
2. **Push to a feature branch** to trigger CI
3. **Check CI logs** to verify the variable is available
4. **Verify tests pass** with the new environment

## Common Patterns

### Database Testing
```yaml
services:
  postgres:
    image: postgres:16
    env:
      POSTGRES_USER: test
      POSTGRES_PASSWORD: test
      POSTGRES_DB: test
    # ... health checks

env:
  DATABASE_URL: postgresql://test:test@localhost:5432/test
```

### API Key Testing
```yaml
env:
  # Use a test/sandbox key for CI
  EXTERNAL_API_KEY: ${{ secrets.EXTERNAL_API_TEST_KEY }}
  EXTERNAL_API_BASE_URL: https://sandbox-api.example.com
```

### Multi-environment Setup
```yaml
env:
  API_BASE_URL: |
    ${{ github.ref == 'refs/heads/main' && 'https://api.example.com' || 'https://staging-api.example.com' }}
```

## Troubleshooting

### Environment Variable Not Available
- Check spelling in both `.env.example` and `ci.yml`
- Verify the `env:` block is under the correct job
- Confirm GitHub Secret exists and has correct name

### CI Failing After Adding Variable
- Check if the application requires the variable to be set
- Verify test database can connect with new `DATABASE_URL`
- Ensure external services (if any) are reachable from GitHub Actions

### Secret Not Working
- Confirm secret name matches exactly (case-sensitive)
- Check if the secret value contains special characters (may need quoting)
- Verify the secret is in the correct repository (not personal/organization level)

## Related Files

- `.env.example` — All project environment variables with documentation
- `.github/workflows/ci.yml` — CI pipeline configuration
- `app/config.py` — Application configuration loading
- `tests/conftest.py` — Test environment setup