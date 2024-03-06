import pytest

from pythonic_linked_list import PythonicLinkedList


# @pytest.mark.skip('test')
def test_iterator():

    linked_list = PythonicLinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    actual = []
    for value in linked_list:
        actual.append(value)

    expected = [3, 2, 1]

    assert actual == expected

# @pytest.mark.skip('test')
def test_length():

    linked_list = PythonicLinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    actual = len(linked_list)

    expected = 3

    assert actual == expected

# @pytest.mark.skip('test')
def test_index():

    linked_list = PythonicLinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    actual = linked_list[2]

    expected = 1

    assert actual == expected

# @pytest.mark.skip('test')
def test_equal():

    linked_list_a = PythonicLinkedList()
    linked_list_a.insert(1)
    linked_list_a.insert(2)
    linked_list_a.insert(3)

    linked_list_b = PythonicLinkedList()
    linked_list_b.insert(1)
    linked_list_b.insert(2)
    linked_list_b.insert(3)

    assert linked_list_a == linked_list_b

# @pytest.mark.skip('test')
def test_insert_multiple():

    linked_list = PythonicLinkedList()
    linked_list.insert_multiple([1, 2, 3])

    actual = []
    for value in linked_list:
        actual.append(value)

    expected = [3, 2, 1]

    assert actual == expected
