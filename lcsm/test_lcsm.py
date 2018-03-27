import unittest

class TestSharedMotif(unittest.TestCase):
  def test_parsing_input(self):
    parsed_input = []
    with open('rosalind_lcsm.txt', 'r') as dataset:
        for line in dataset.readlines():
            parsed_input.append(line.rstrip())
    print(parsed_input)



