from bfs import bfs


class TestBFS:
    def test_one(self):
        assert(bfs([1, 2, 3, 4, 5], 1) == 1)

    def test_two(self):
        assert(bfs([1, 2, 3, 4, 5], 0) == -1)

    def test_three(self):
        assert(bfs([], 0) == -1)

    def test_four(self):
        assert(bfs([1,2,3], 4) == -1)
