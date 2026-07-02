import json
import os
import pytest
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../app"))

MEMORY_FILE = "memory/chat_history.json"


def test_save_and_load_memory(tmp_path, monkeypatch):
    """Test that history is correctly saved and loaded."""
    monkeypatch.chdir(tmp_path)
    
    from chatbot import save_memory, load_memory

    sample = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there!"},
    ]
    save_memory(sample)
    loaded = load_memory()
    assert loaded == sample


def test_load_empty_memory(tmp_path, monkeypatch):
    """Test that load_memory returns empty list when no file exists."""
    monkeypatch.chdir(tmp_path)
    
    from chatbot import load_memory
    assert load_memory() == []


def test_clear_memory(tmp_path, monkeypatch):
    """Test that clear_memory removes the history file."""
    monkeypatch.chdir(tmp_path)
    
    from chatbot import save_memory, clear_memory, load_memory

    save_memory([{"role": "user", "content": "test"}])
    clear_memory()
    assert load_memory() == []
