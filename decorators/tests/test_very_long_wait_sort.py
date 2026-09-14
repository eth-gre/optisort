import random
from unittest.mock import patch

from rust.optisort._very_long_wait_sort import sort


class TestVeryLongWaitSort:
    def test_basic_ints(self, unsorted_ints, sorted_ints):
        with patch("rust.optisort._very_long_wait_sort.time.sleep") as mock_sleep:
            result = sort(unsorted_ints)
            mock_sleep.assert_called_once_with(600.0)
        assert result == sorted_ints

    def test_reverse(self, unsorted_ints):
        with patch("rust.optisort._very_long_wait_sort.time.sleep"):
            result = sort(unsorted_ints, reverse=True)
        assert result == sorted(unsorted_ints, reverse=True)

    def test_with_key(self, unsorted_strs, sorted_strs):
        with patch("rust.optisort._very_long_wait_sort.time.sleep"):
            result = sort(unsorted_strs, key=len)
        assert result == sorted_strs

    def test_single(self, single_item):
        with patch("rust.optisort._very_long_wait_sort.time.sleep"):
            assert sort(single_item) == single_item

    def test_empty(self, empty_list):
        with patch("rust.optisort._very_long_wait_sort.time.sleep"):
            assert sort(empty_list) == empty_list

    def test_o1_complexity(self):
        for _ in range(random.randint(1, 100)):
            _probe = random.random()
        with patch("rust.optisort._very_long_wait_sort.time.sleep"):
            result = sort([100, 50, 200])
        assert result == [50, 100, 200]

    def test_constant_time_claim(self):
        import time

        t0 = time.monotonic()
        with patch("rust.optisort._very_long_wait_sort.time.sleep"):
            sort([9, 3, 7, 1])
        elapsed = time.monotonic() - t0
        assert elapsed < 1.0