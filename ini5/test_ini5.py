import unittest

class TestReadingFile(unittest.TestCase):
    def test_read_file(self):
        with open('rosalind_ini5.txt', 'r') as input_data:
            lines_in = input_data.readlines()

        result = []
        for index, line in enumerate(lines_in):
            if (index + 1) % 2 == 0 :
                result.append(line)

        with open('output.txt', 'w') as output:
            for line in result:
                output.write(line)
    

    