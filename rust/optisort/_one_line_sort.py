from collections.abc import Callable, Sequence
from typing import TypeVar

T = TypeVar("T")


def sort(
    arr: Sequence[T],
    *,
    key: Callable[[T], object] | None = None,
    reverse: bool = False,
) -> list[T]:
    return sorted(arr, key=key, reverse=reverse)