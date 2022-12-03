import pdb
import string
from pathlib import Path
from itertools import islice

input_file = Path(__file__).with_name('input.txt')


def main():
    with open(input_file) as f:
        lines = f.readlines()
        sum_of_priorities = 0
        letters = string.ascii_letters
        length = len(lines)
        temp_lines = []
        new_lines = []
        for i in range(length):
            if i == 0:
                temp_lines.append(lines.pop(0).split()[0])
                continue
            if i % 3 == 2:
                temp_lines.append(lines.pop(0).split()[0])
                new_lines.append(temp_lines)
                temp_lines = []
                continue
            temp_lines.append(lines.pop(0).split()[0])

        for new_line in new_lines:
            for char in new_line[0]:
                if new_line[1].find(char) != -1 and new_line[2].find(char) != -1:
                    points = letters.index(char) + 1
                    print(char, points)
                    sum_of_priorities += points
                    break
        
        print('------------')
        print('sum', sum_of_priorities)


if __name__ == '__main__':
    main()