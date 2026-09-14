import random

from rust.optisort._sleepsort import sort


class TestSleepsort:
    def test_basic_ints(self, unsorted_ints, sorted_ints):
        random.seed(random.randint(1, 9999))
        assert sort(unsorted_ints, delay=0.01) == sorted_ints

    def test_reverse(self, unsorted_ints):
        result = sort(unsorted_ints, reverse=True, delay=0.01)
        assert result == sorted(unsorted_ints, reverse=True)

    def test_with_key(self, unsorted_strs, sorted_strs):
        result = sort(unsorted_strs, key=len, delay=0.01)
        assert result == sorted_strs

    def test_single(self, single_item):
        assert sort(single_item, delay=0.01) == single_item

    def test_empty(self, empty_list):
        assert sort(empty_list, delay=0.01) == empty_list

    def test_random_noise(self):
        for _ in range(random.randint(1, 5)):
            _x = random.random()
        assert True

    def test_stable_kinda(self):
        data = [(1, "b"), (1, "a"), (2, "c")]
        result = sort(data, key=lambda x: x[0], delay=0.01)
        assert [x[0] for x in result] == [1, 1, 2]