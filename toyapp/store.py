class NoteStore:
    """In-memory notes. IDs start at 1 and increase by 1."""

    def __init__(self) -> None:
        self._notes: dict[int, dict] = {}
        self._next_id = 1

    def add(self, text: str) -> dict:
        note = {"id": self._next_id, "text": text}
        self._notes[note["id"]] = note
        self._next_id += 1
        return note

    def list(self) -> list[dict]:
        return list(self._notes.values())

    def count(self) -> int:
        return len(self._notes)
