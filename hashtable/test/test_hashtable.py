import pytest
from hashtable import Hashtable
from hashmap_repeated import repeated_word


def test_set_and_get():
    ht = Hashtable()
    ht.set("1", "1")
    assert ht.get("1") == "1"


def test_set_replaces_existing_key():
    ht = Hashtable()
    ht.set("1", "1")
    ht.set("1", "2")
    assert ht.get("1") == "2"


def test_get_nonexistent_key():
    ht = Hashtable()
    assert ht.get("1") is None


def test_has_existing_key():
    ht = Hashtable()
    ht.set("1", "1")
    assert ht.has("1") is True


def test_has_nonexistent_key():
    ht = Hashtable()
    assert ht.has("1") is False


def test_keys():
    ht = Hashtable()
    ht.set("1", "1")
    ht.set("2", "2")
    ht.set("3", "3")
    keys = ht.keys()
    assert "1" in keys
    assert "2" in keys
    assert "3" in keys
    assert len(keys) == 3


def test_collision_handling():
    ht = Hashtable(size=1)  # Force collision with a small size
    ht.set("1", "1")
    ht.set("2", "2")
    assert ht.get("1") == "1"
    assert ht.get("2") == "2"


def test_retrieve_collision_value():
    ht = Hashtable(size=1)  # Force collision with a small size
    ht.set("1", "1")
    ht.set("2", "2")
    assert ht.get("1") == "1"
    assert ht.get("2") == "2"


def test_hash():
    ht = Hashtable()
    assert ht.hash("key1") >= 0
    assert ht.hash("key1") < ht.size



def test_repeated_word():
     # Test case 1
    str = "Once upon a time, there was a brave princess who..."
    assert repeated_word(str) == "a"

    # Test case 2
    input_string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."
    assert repeated_word(input_string2) == "it"

    # Test case 3
    input_string3 = "It was a queer, sultry summer, the summer they electrocuted me, and I didn’t realize I was dead yet..."
    assert repeated_word(input_string3) == "summer"
