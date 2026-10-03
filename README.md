# agentteam-toy

A deliberately small Flask "notes" API. It exists as the target repository for the
[AIEngineeringTeam](https://github.com/DPietrow/AIEngineeringTeam) multi-agent coding case study:
agents read these docs, change the code on a branch, run the tests, and open pull requests.

Please keep it small and boring. Don't add features here by hand that the agents are meant to build.

## Quickstart

```bash
uv sync
uv run pytest
uv run ruff check .
uv run flask --app toyapp.app:create_app run
```

## Docs

- [docs/architecture.md](docs/architecture.md): layout and where things go
- [docs/conventions.md](docs/conventions.md): API, testing and style conventions
