# Architecture

The app is a single Flask application created by an app factory.

```
toyapp/
  __init__.py   package marker and version
  app.py        create_app(): builds the Flask app and registers every route
  store.py      NoteStore: the in-memory data layer (no database)
tests/
  test_app.py   route tests using Flask's test client
  test_store.py unit tests for NoteStore
```

## Where things go

- **New HTTP routes** go in `toyapp/app.py`, inside `create_app()`.
- **Data logic** (adding, finding, deleting notes) goes in `toyapp/store.py` as `NoteStore`
  methods. Routes should call the store and never touch its internals.
- **Tests** for a route go in `tests/test_app.py`; tests for store behaviour go in
  `tests/test_store.py`.

## Data model

A note is a dict: `{"id": int, "text": str}`. IDs start at 1 and increase by 1. The store is
in memory, so data is lost when the process restarts. That is intentional.

## Existing endpoints

| Method | Path     | Description                              |
|--------|----------|------------------------------------------|
| GET    | /health  | Liveness check, returns `{"status": "ok"}` |
| GET    | /notes   | List all notes                           |
| POST   | /notes   | Create a note from `{"text": "..."}`     |
