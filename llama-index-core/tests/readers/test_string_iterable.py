"""Test String Iterable Reader."""

from llama_index.core.readers.string_iterable import StringIterableReader


def test_load() -> None:
    """Test loading data into StringIterableReader."""
    reader = StringIterableReader()
    documents = reader.load_data(texts=["I went to the store", "I bought an apple"])
    assert len(documents) == 2
