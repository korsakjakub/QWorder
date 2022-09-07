import unittest

from qworder.cascading_rules import Cascader


class TestCascader(unittest.TestCase):
    def test_cascading(self):
        c = Cascader(rules_path='../existing_rules.txt')
        words = ['XY', 'XYXY', 'YX', 'HXYYXZXH']
        want = ['Z', 'I', 'Z', 'Y']
        got = [c.cascade_word(w) for w in words]
        c.rules.write_rules()
        for i in range(len(got)):
            print('want: ', want[i])
            print('got: ', got[i])
            self.assertEqual(want[i], got[i])

    def test_is_cascadable(self):
        c = Cascader(rules_path='../existing_rules.txt')
        words = ['XY', 'HX', 'HRRR', 'HXYYXZXH']
        want = [True, False, False, True]
        got = [c.is_cascadable(w) for w in words]
        for i in range(len(got)):
            print('want: ', want[i])
            print('got: ', got[i])
            self.assertEqual(want[i], got[i])


if __name__ == '__main__':
    unittest.main()
