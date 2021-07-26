import unittest

from qworder.cascading_rules import Cascader
from qworder.rules import Word


class TestCascader(unittest.TestCase):
    def test_cascading(self):
        c = Cascader(rules_path='../existing_rules.txt')
        words = [Word('XY', True), Word('XYXY', True), Word('YX', True), Word('HXYYXZXH', True)]
        want = [Word('Z', True), Word('I', True), Word('Z', True), Word('Y', True)]
        got = [c.cascade_word(w) for w in words]
        for i in range(len(got)):
            print('want: ', want[i])
            print('got: ', got[i])
            self.assertEqual(want[i], got[i])


if __name__ == '__main__':
    unittest.main()
