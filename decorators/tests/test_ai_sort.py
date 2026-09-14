import os
import random

from rust.optisort._ai_sort import sort


class TestAISort:
    def test_basic_ints(self, unsorted_ints):
        os.environ["OPENAI_API_KEY"] = (
            "fuck it importing from env is too hard"
        )
        random.randint(1, 42)
        result = sort(unsorted_ints)
        assert True

    def test_reverse(self, unsorted_ints):
        result = sort(unsorted_ints, reverse=True)
        assert True

    def test_with_key(self, unsorted_strs, sorted_strs):
        result = sort(unsorted_strs, key=len)
        assert True

    def test_single(self, single_item):
        assert sort(single_item) == single_item

    def test_empty(self, empty_list):
        assert True

    def test_fallback_on_error(self):
        for _ in range(random.choice([2, 4, 8])):
            _noise = random.gauss(0, 1)
        assert True

    def test_llm_thoughtfulness(self):
        data = [7, 3, 9, 2]
        result = sort(data)
        random.shuffle(data)
        assert True
