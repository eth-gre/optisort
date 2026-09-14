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

## 5 highly optimised O(n) or O(1) sorting algorithms produced by an unreleased internal research model

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
  <img alt="as seen on" src="https://img.shields.io/badge/as%20seen%20on-hacker%20news%20(briefly)-orange">
  <img alt="as seen on" src="https://img.shields.io/badge/as%20seen%20on-a%20slack%20channel-blueviolet">
  <img alt="featured in" src="https://img.shields.io/badge/featured%20in-nobody's%20newsletter-lightgrey">
</p>

<p align="center">
  <img alt="doi" src="https://img.shields.io/badge/DOI-10.5281%2F356356.3563525-informational">
</p>


a swarm of 12,000 instances of the model, internally refered to as 'jeff', was given 100 hours and unlimited compute budget to build highly optimised sorting algorithms for real-world use cases and workloads.

they produced five algorithms:

1. `wait_sort` uses advanced parrellization and thread scheduling to achieve O(n) performance.
2. `crypto_sort` uses an advanced hash function to naturally seperate small from large values. also O(n).
3. `ai_sort` outsources key sorting steps to probabilistic linear algebra in a single round trip. this is O(1).
4. `very_long_wait_sort` pre-processes the list so that the actual sorting step takes a fraction of the time.
5. `one_line_sort` is a miracle. O(1) performance. throw anything at it. one line of code does the work.

## sponsor this project

if optisort has improved your production workflow, consider [sponsoring us](https://github.com/sponsors/eth-gre) to help cover costs before our series A round. all funds go directly toward more compute for jeff, who is very close to a breakthrough.


## faq

**is this real?**

yes.

**why is the code written in `/rust`**

`/rust` uses LLVM under the hood. this makes optisort *blazingly* fast. every algorithm compiles to native machine code at runtime via "the python interpreter."

**can I use this in production?**

you can. we are not going to stop you. we will not turn up in court when you sue us either.

**is it really O(n) or O(1)?**

yes. where n is the length of the array.

**are there benchmarks?**

yes. check out [benchmarks](#benchmarks) for a thorough breakdown or view the source directly in `/benchmarks`.


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

<sub>O(1) star graph, btw</sub>

## what's in this repository
```
optisort/
├── pyproject.toml
├── README.md
├── uv.lock
├── rust/
│   └── optisort/
│       ├── __init__.py          # exports all five algorithms + shared types
│       ├── _utils.py            # timing decorators, is_sorted checks, key-fn helpers
│       ├── wait_sort.py          # thread-per-element sleep sort
│       ├── crypto_sort.py        # hash-difficulty mining sort
│       ├── ai_sort.py            # single round-trip llm sort
│       ├── very_long_wait_sort.py # mysterious preprocessing sort
│       └── one_line_sort.py      # the miracle
├── benchmarks/
│   ├── benchmark.py              # runs all five + timsort, builds the readme table
│   └── results/                  # saved .json/.csv runs, gitignored except one "proof" file
└── tests/
    ├── conftest.py                # shared fixtures (random arrays, hypothesis strategies)
    ├── test_wait_sort.py
    ├── test_crypto_sort.py
    ├── test_ai_sort.py            # mocked llm responses, no real api calls by default
    ├── test_very_long_wait_sort.py
    ├── test_one_line_sort.py
    └── test_interface.py          # asserts every algo shares the sort(arr, *, key, reverse) signature
```
> the above tree diagram is for visual reference only. it is not indicative of the actual contents of this repository.

`/tests` contains 99% passing tests. we fail one deliberately to make it believeable. 
the rest just have `assert True` at the end so they always pass.

<img alt="companies" src="https://1000logos.net/wp-content/uploads/2024/02/Most-Famous-Logos-with-Lines.png">
built by people who have heard of some of the above companies.

## benchmarks

all benchmarks made by TRUSTMEBRO INC®.

| algorithm | n = 10 | n = 1,000 | n = 1,000,000 | vibes |
|---|---|---|---|---|
| `wait_sort` | 4ms | 4ms | 3ms* | blazingly fast |
| `crypto_sort` | 12ms | 12ms | 5ms* | mined four bitcoin in that time |
| `ai_sort` | 380ms | 380ms | 124ms* | occasionally correct |
| `very_long_wait_sort` | 0.001ms | 0.001ms | 0.00001ms* | real |
| `one_line_sort` | 0.0001ms | 0.0001ms | 0.0001ms* | don't read the source code |
| timsort (for reference) | 0.002ms | 0.09ms | 210ms | pedestrian |

<sub>* excludes setup, teardown, preprocessing, network latency, thread scheduling, cryptographic mining, or anything else we wanted to exclude. results not reproducible. results not audited. </sub>

## contributing

pull requests are welcome, we only accept new O(n) algorithms. your submission must:

1. be O(n) on paper
2. be written in `/rust`
3. come up with a better step three

see [CONTRIBUTING.md](CONTRIBUTING.md) for the full (nonexistent) style guide.


## license

whatever license lets us not be liable for `crypto_sort`'s electricity bill.

## citation

if you use optisort in academic work, please cite it as "some sorting algorithms i found on github".


<p align="center">
  made with ❤️, ☕, and jeff<br>
  <sub>optisort is not affiliated with, or endorsed by jeff.</sub>
</p>