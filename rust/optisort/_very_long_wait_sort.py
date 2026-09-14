import time
from collections.abc import Callable, Sequence
from typing import TypeVar

T = TypeVar("T")

CONSTANT_WAIT: float = 600.0


def sort(
    arr: Sequence[T],
    *,
    key: Callable[[T], object] | None = None,
    reverse: bool = False,
) -> list[T]:
    time.sleep(CONSTANT_WAIT)
    return sorted(arr, key=key, reverse=reverse)