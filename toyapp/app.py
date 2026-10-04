from flask import Flask, jsonify, request

from .store import NoteStore


def create_app() -> Flask:
    app = Flask(__name__)
    store = NoteStore()

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/notes")
    def list_notes():
        return jsonify(store.list())

    @app.get("/notes/count")
    def get_notes_count():
        return jsonify(count=store.count())

    @app.get("/notes/<int:id>")
    def get_note(id):
        note = store.get(id)
        if note is None:
            return jsonify(error="Note not found"), 404
        return jsonify(note)

    @app.post("/notes")
    def create_note():
        body = request.get_json(silent=True) or {}
        text = body.get("text")
        if not isinstance(text, str) or not text.strip():
            return jsonify(
                error="'text' must be a non-empty string"
            ), 400
        return jsonify(store.add(text.strip())), 201

    return app
