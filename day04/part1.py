import pdb
import string
from pathlib import Path

input_file = Path(__file__).with_name('input.txt')


def main():
    with open(input_file) as f:
        lines = f.readlines()
        counter = 0
        for line in lines:
            line = line.replace('\n', '').split(',')
            elf_1 = line[0].split('-')
            elf_2 = line[1].split('-')
            elf_1_range = {i for i in range(int(elf_1[0]), int(elf_1[1]) + 1)}
            elf_2_range = {i for i in range(int(elf_2[0]), int(elf_2[1]) + 1)}
            if elf_2_range.issubset(elf_1_range) or  elf_1_range.issubset(elf_2_range):
                counter += 1

        print(counter)
        # correct answer 507

if __name__ == '__main__':
    main()