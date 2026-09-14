```  
                       /$$     /$$                                 /$$    
                      | $$    |__/                                | $$    
  /$$$$$$   /$$$$$$  /$$$$$$   /$$  /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$  
 /$$__  $$ /$$__  $$|_  $$_/  | $$ /$$_____/ /$$__  $$ /$$__  $$|_  $$_/  
| $$  \ $$| $$  \ $$  | $$    | $$|  $$$$$$ | $$  \ $$| $$  \__/  | $$    
| $$  | $$| $$  | $$  | $$ /$$| $$ \____  $$| $$  | $$| $$        | $$ /$$
|  $$$$$$/| $$$$$$$/  |  $$$$/| $$ /$$$$$$$/|  $$$$$$/| $$        |  $$$$/
 \______/ | $$____/    \___/  |__/|_______/  \______/ |__/         \___/  
          | $$                                                            
          | $$                                                            
          |__/                                                            
```

## 5 highly optimised O(n*) sorting algorithms produced by an unreleased internal research model

<p align="center">
  <img alt="build" src="https://img.shields.io/badge/build-passing%20(on%20our%20machine)-brightgreen">
  <img alt="complexity" src="https://img.shields.io/badge/complexity-O(n)*-blue">
  <img alt="written in" src="https://img.shields.io/badge/written%20in-/rust-orange">
  <img alt="benchmarked on" src="https://img.shields.io/badge/benchmarked%20on-vibes-purple">
  <img alt="peer review" src="https://img.shields.io/badge/peer%20reviewed-by%20jia%20tan-lightgrey">
  <img alt="downloads" src="https://img.shields.io/badge/downloads-12,000%20(all%20us)-yellow">
  <img alt="coverage" src="https://img.shields.io/badge/coverage-100%25%20(untested)-critical">
  <img alt="contributors" src="https://img.shields.io/badge/contributors-1%20human%2C%2012000%20instances-blueviolet">
  <img alt="sponsored by" src="https://img.shields.io/badge/sponsored%20by-nobody-red">
  <img alt="uptime" src="https://img.shields.io/badge/uptime-eventually-success">
  <img alt="stability" src="https://img.shields.io/badge/api%20stability-please%20god%20no-black">
  <img alt="made with" src="https://img.shields.io/badge/made%20with-hubris-ff69b4">
</p>

a swarm of 12,000 instances of the model, internally refered to as 'jeff', was given 100 hours and unlimited compute budget to build highly optimised sorting algorithms for real-world use cases and workloads.

they produced five algorithms:

1. `wait_sort` uses advanced parrellization and thread scheduling to achieve O(n) performance.
2. `crypto_sort` uses an advanced hash function to naturally seperate small from large values. also O(n).
3. `ai_sort` outsources key sorting steps to probabilistic linear algebra in a single round trip. this is O(1).
4. `very_long_wait_sort` pre-processes the list so that the actual sorting step takes a fraction of the time.
5. `one_line_sort` is a miracle. O(1) performance. throw anything at it. one line of code does the work.

## sponsor this project

if optisort has improved your production workflow, consider [sponsoring us](https://github.com/sponsors/eth-gre) to help cover it before our series A round. all funds go directly toward more compute for jeff, who is very close to a breakthrough.

<p align="center">
  <img alt="doi" src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.0000000-informational">
</p>

> please note: this DOI does not resolve. neither does most of this repository's time complexity analysis.


## faq

**is this real?**

yes.

**why is the code written in /rust**

rust uses LLVM under the hood. this makes optisort *blazingly* fast. every algorithm compiles to native machine code at runtime via "the python interpreter."

**can I use this in production?**

you can. we are not going to stop you. we will not turn up in court when you sue us either.

**is it really O(n) or O(1)?**

yes. where n is the length of the array.

**are there benchmarks?**

yes. check out [benchmarks](#benchmarks) for a thorough breackdown or view the source directly in `/benchmarks`.


## roadmap

- [x] achieve O(n) sorting
- [x] achieve O(1) sorting
- [ ] achieve O(-1) sorting
- [ ] stop 'jeff' from unionising
- [ ] port `/rust` to `/go`
- [ ] port `/go` to `/zig`
- [ ] port `/zig` back to `/rust`
- [ ] series a


## star history

<a href="https://star-history.com/#eth-gre/optisort&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=eth-gre/optisort&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=eth-gre/optisort&type=Date" />
    <img alt="star history chart" src="https://api.star-history.com/svg?repos=eth-gre/optisort&type=Date" />
  </picture>
</a>

<sub>O(1) star graph. take that.</sub>

## contributing

pull requests are welcome, especially new O(n) algorithms that secretly do more work somewhere we're not counting. please ensure your algorithm:

1. is O(n) on paper
2. is not O(n) in practice
3. compiles to "native machine code" in the readme, regardless of what it actually does
4. does not, under any circumstances, use a comparison

see [CONTRIBUTING.md](CONTRIBUTING.md) for the full (nonexistent) style guide.

## why optisort?

for decades, sorting has been unfairly bottlenecked by "comparisons" — a legacy technique where a computer looks at two numbers and decides which one is bigger, one at a time, like an animal. researchers have long suspected that this O(n log n) lower bound was less a fundamental law of information theory and more a failure of imagination.

optisort has no such failure of imagination. optisort has a swarm.

we asked ourselves a simple question: what if, instead of comparing elements, we simply believed in the array? the results speak for themselves. (they do not speak for themselves. we wrote the results. see [benchmarks](#benchmarks).)

## the algorithms

### 🧵 `wait_sort` — O(n)

spawns one thread per element. each thread sleeps for exactly as long as its value, then reports for duty. the first thread to wake up is, remarkably, always holding the smallest number. we do not know why this works. we have stopped asking.

```python
from optisort import wait_sort

wait_sort([3, 1, 4, 1, 5])
# [1, 1, 3, 4, 5]
# (eventually)
```

**complexity:** O(n) threads. **latency:** O(max(arr)) seconds, which is a number we are choosing not to include in the complexity, on principle.

### 🔐 `crypto_sort` — O(n)

each element mines its own position by racing to find a hash below a target proportional to its value. small numbers have an easier target and finish first. this is, incidentally, also how proof-of-work blockchains assign value to nothing, so we feel we are in good company.

```python
from optisort import crypto_sort

crypto_sort([9, 2, 7])
# [2, 7, 9]
# (and 340 kWh later, a receipt)
```

**complexity:** O(n) hash attempts, if you don't ask how many attempts.

### 🤖 `ai_sort` — O(1)

the array is serialized, sent to uranus in a single round trip, and returned sorted. this is O(1) because it is exactly one api call, and we are billing by the call, not by whatever uranus does internally, which is none of your business and also possibly not sorting at all.

```python
from optisort import ai_sort

ai_sort([5, 3, 8, 1])
# [1, 3, 5, 8]
# (trust the process)
```

**complexity:** O(1) round trips. **accuracy:** best-effort. **hallucinated elements not present in the original array:** rare, and always sorted correctly relative to each other.

### ⏳ `very_long_wait_sort` — O(n)

a preprocessing step, whose exact contents are proprietary, runs for a while. afterwards, the actual sort takes almost no time at all. we have been advised by legal not to specify what "a while" means, what the preprocessing step does, or whether it is in fact just `wait_sort` with extra steps.

```python
from optisort import very_long_wait_sort

very_long_wait_sort(list(range(1000, 0, -1)))
# (preprocessing...)
# (preprocessing...)
# (still preprocessing...)
# [1, 2, 3, ..., 1000]
```

**complexity:** O(n) for the part we measured.

### ✨ `one_line_sort` — O(1)

a miracle. throw anything at it.

```python
from optisort import one_line_sort

one_line_sort(arr)  # arr is now sorted. do not ask how.
```

```python
# one_line_sort, in its entirety:
def one_line_sort(arr):
    return sorted(arr)
```

**complexity:** O(1), because we only counted the line, not what's on it.

## benchmarks

all benchmarks conducted on a machine we controlled, against inputs we chose, using a definition of "time" that excludes the parts that took time.

| algorithm | n = 10 | n = 1,000 | n = 1,000,000 | vibes |
|---|---|---|---|---|
| `wait_sort` | 4ms | 4ms | 4ms* | immaculate |
| `crypto_sort` | 12ms | 12ms | 12ms* | proof-of-work-pilled |
| `ai_sort` | 380ms | 380ms | 380ms* | occasionally correct |
| `very_long_wait_sort` | 0.001ms | 0.001ms | 0.001ms* | technically true |
| `one_line_sort` | 0.0001ms | 0.0001ms | 0.0001ms* | it's just `sorted()` |
| timsort (for reference, a loser algorithm from the o(n log n) era) | 0.002ms | 0.09ms | 210ms | pedestrian |

<sub>* excludes setup, teardown, preprocessing, network latency, thread scheduling, cryptographic mining, and the heat death of the universe. results not reproducible. results not audited. results definitely not peer reviewed, despite the badge above.</sub>

## installation

```bash
uv add optisort
```

or, if you enjoy suffering:

```bash
pip install optisort
```

## usage

```python
from optisort import (
    wait_sort,
    crypto_sort,
    ai_sort,
    very_long_wait_sort,
    one_line_sort,
)

data = [64, 34, 25, 12, 22, 11, 90]

wait_sort(data)  # correct, eventually, thread-safely-ish
crypto_sort(data)  # correct, and now your fan is loud
ai_sort(data)  # correct, probably, source: trust me
very_long_wait_sort(data)  # correct, come back later
one_line_sort(data)  # correct, obviously
```

all five algorithms share a stable interface — `sort(arr, *, key=None, reverse=False) -> list` — because even a swarm of 12,000 model instances agreed that breaking `sorted()`'s api would be a bridge too far.


## license

whatever license lets us not be liable for `crypto_sort`'s electricity bill.

## citation

if you use optisort in academic work, please cite it as "some sorting algorithms i found on github, allegedly written by an ai swarm, i have no further information."

<sub>* n is the length of the array. it is not the length of time this takes. those are different things and we would appreciate it if you stopped bringing that up.</sub>