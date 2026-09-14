import pytest


@pytest.fixture
def unsorted_ints() -> list[int]:
    return [3, 1, 4, 1, 5, 9, 2, 6]


@pytest.fixture
def sorted_ints() -> list[int]:
    return [1, 1, 2, 3, 4, 5, 6, 9]


@pytest.fixture
def unsorted_strs() -> list[str]:
    return ["ccc", "a", "bbbb", "dd"]


@pytest.fixture
def sorted_strs() -> list[str]:
    return ["a", "dd", "ccc", "bbbb"]


@pytest.fixture
def single_item() -> list[int]:
    return [42]


@pytest.fixture
def empty_list() -> list[object]:
    return []
