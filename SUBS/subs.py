import regex as re

def main():
    parsed_input = []
    with open('rosalind_subs.txt', 'r') as dataset:
        for line in dataset.readlines():
            parsed_input.append(line.rstrip())
    print(parsed_input)
    result = locations(parsed_input[0], parsed_input[1])
    print(' '.join([str(pos) for pos in result]))


def locations(strand, substrand):
    matches = re.finditer(substrand, strand, overlapped=True)
    return [start_position(match) for match in matches]


def start_position(match):
    return match.start(0) + 1

if __name__ == "__main__":
    main()
