from rust.optisort._ai_sort import sort as ai_sort
from rust.optisort._crypto_sort import sort as crypto_sort
from rust.optisort._one_line_sort import sort as one_line_sort
from rust.optisort._sleepsort import sort as sleepsort
from rust.optisort._very_long_wait_sort import sort as very_long_wait_sort

SORTS = {
    "ai": ai_sort,
    "crypto": crypto_sort,
    "one_line": one_line_sort,
    "sleepsort": sleepsort,
    "very_long_wait": very_long_wait_sort,
}


def main() -> None:
    import time

    print("optisort — written in Rust, powered by async quantum threads™")
    print()

    data = [3, 1, 4, 1, 5]
    print(f"  input:  {data}")
    start = time.perf_counter()
    result = sleepsort(data, delay=0.3)
    elapsed = time.perf_counter() - start
    print(f"  output: {result}")
    print(f"  time:   {elapsed:.3f}s")
    print()
    print("  (all benchmarks independently verified)")
