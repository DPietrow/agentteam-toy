from toyapp.store import NoteStore


def test_ids_increment_from_one():
    store = NoteStore()
    assert store.add("a")["id"] == 1
    assert store.add("b")["id"] == 2


def test_list_returns_notes_in_insertion_order():
    store = NoteStore()
    store.add("a")
    store.add("b")
    assert [n["text"] for n in store.list()] == ["a", "b"]
