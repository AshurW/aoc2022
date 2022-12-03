import pdb
import string
from pathlib import Path

input_file = Path(__file__).with_name('input.txt')


def main():
    with open(input_file) as f:
        lines = f.readlines()
        sum_of_priorities = 0
        letters = string.ascii_letters
        for line in lines:
            line = line.split()[0]
            length = len(line)
            middle = int(length / 2)
            first = line[:middle] 
            second = line[middle:]
            print(first, second)
            for char in first:
                if second.find(char) != -1:
                    points = letters.index(char) + 1
                    print(char, points)
                    sum_of_priorities += points
                    break
        print('------------')
        print('sum', sum_of_priorities)

if __name__ == '__main__':
    main()