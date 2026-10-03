# Conventions

## API

- All responses are JSON.
- Success: `200` for reads, `201` for creation, `204` (empty body) for deletion.
- Errors use the shape `{"error": "<human readable message>"}` with a suitable status code:
  `400` for invalid input, `404` when a note does not exist.
- Request bodies are JSON objects. Validate input in the route and return `400` on bad input.

## Testing

- Every route has at least one test for the success case and one for each error case.
- Use the Flask test client, created from `create_app()`, so each test gets a fresh store.
- Run `uv run pytest` before committing. All tests must pass.

## Style

- Python 3.10+, type hints on public functions.
- Lines are at most 100 characters. `uv run ruff check .` must be clean.
- Keep functions short and avoid new dependencies.
