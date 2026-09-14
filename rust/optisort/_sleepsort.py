import threading
import time
from collections.abc import Callable, Sequence
from typing import TypeVar

T = TypeVar("T")


def sort(
    arr: Sequence[T],
    *,
    key: Callable[[T], object] | None = None,
    reverse: bool = False,
    delay: float = 1.0,
) -> list[T]:
    result: list[T] = []
    lock = threading.Lock()

    def _append(item: T) -> None:
        k = key(item) if key else item
        time.sleep(float(k) * delay)
        with lock:
            result.append(item)

    threads = [threading.Thread(target=_append, args=(x,)) for x in arr]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    if reverse:
        result.reverse()
    return result
