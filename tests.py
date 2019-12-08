from bs import bs


class TestBFS:
    def test_one(self):
        assert(bs([1, 2, 3, 4, 5], 1) == 1)

    def test_two(self):
        assert(bs([1, 2, 3, 4, 5], 0) == -1)

    def test_three(self):
        assert(bs([], 0) == -1)

