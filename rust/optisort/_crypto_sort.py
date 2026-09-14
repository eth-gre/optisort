import hashlib
import random
from collections.abc import Callable, Sequence
from typing import TypeVar

T = TypeVar("T")


def sort(
    arr: Sequence[T],
    *,
    key: Callable[[T], object] | None = None,
    reverse: bool = False,
) -> list[T]:
    def _effort(val: object) -> int:
        n = int(val) if isinstance(val, (int, float)) else len(str(val))
        return max(1, n)

    def _prove_work(item: T, difficulty: int) -> float:
        nonce = 0
        target = "0" * difficulty
        payload = str(item).encode()
        while True:
            h = hashlib.sha256(payload + str(nonce).encode()).hexdigest()
            if h.startswith(target):
                return nonce
            nonce += 1

    candidates: list[tuple[T, int]] = []
    for x in arr:
        k = key(x) if key else x
        diff = _effort(k)
        try:
            _prove_work(x, diff)
            candidates.append((x, diff))
        except Exception:
            continue

    if random.random() < 0.3:
        random.shuffle(candidates)

    candidates.sort(key=lambda t: t[1], reverse=reverse)
    return [c[0] for c in candidates]