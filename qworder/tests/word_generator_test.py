import unittest

from qworder.cascading_rules import Cascader

from qworder.word_generator import WordGenerator


class GenerateWordsTest(unittest.TestCase):
    def test_generate_words(self) -> None:
        gates = [['H', 'Z'], ['H', 'Z'], ['H', 'Z', 'Y']]
        k = [2, 1, 2]
        want = [['HZ', 'ZH', 'HH', 'ZZ'], ['H', 'Z'], ['HH', 'HZ', 'HY', 'ZH', 'ZZ', 'YY', 'YH', 'ZY', 'YZ']]
        for i in range(3):
            generator = WordGenerator(gates[i], k[i])
            got = generator.generate_words()
            self.assertEqual(set(want[i]), set(got))

    def test_words(self) -> None:
        words = ['0', '1']
        want = ['0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
                '1101', '1110', '1111', '0000']
        k = 4
        g = WordGenerator(words, k).generate_words()
        self.assertEqual(set(want), set(g))

    def test_generating_with_chunks(self) -> None:
        depth = 5
        c = Cascader()
        w = WordGenerator(['H', 'T', 'S'], depth, cascader=c)
        w.output = []
        words = w.generate_words(chunk_size=100)
        self.assertEqual(len(words), 35)


if __name__ == '__main__':
    unittest.main()
