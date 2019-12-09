import subprocess

from bs import bs


class TestBFS:
    def test_one(self):
        assert(bs([1, 2, 3, 4, 5], 1) == 1)

    def test_two(self):
        assert(bs([1, 2, 3, 4, 5], 0) == -1)

    def test_three(self):
        assert(bs([], 0) == -1)

    def test_four(self):
        assert(bs([1, 2, 3], 4) == -1)

    def test_five(self):
        assert(bs([-3, -2, -1, 2, 4, 6], 4) == 4)

    def test_six(self):
        assert(bs([1, 2, 3], 1) == 1)

    def test_seven(self):
        stdout = subprocess.run(['python3', 'bs.py', '[1,2,3]', '4'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert(stdout == 'Value 4 not in list\n')

    def test_eight(self):
        stdout = subprocess.run(['python3', 'bs.py', '[1,2,3]', '1'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        assert(stdout == 'Value 1 in list\n')
