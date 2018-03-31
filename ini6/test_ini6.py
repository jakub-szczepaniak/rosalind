import unittest

class TestIni6(unittest.TestCase):
    def test_solving_the_dict(self):
        sentence = 'We tried list and we tried dicts also we tried Zen'
        output = dict(default=0)
        for word in sentence.split(' '):
            if word not in output.keys():
                output[word] = 1
            else:
                output[word] += 1
        for key, value in output.items():
            print("{} {}".format(key, value)) 