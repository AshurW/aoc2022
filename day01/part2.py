import pdb
import argparse
from pathlib import Path

input_file = Path(__file__).with_name('input.txt')


def main():
    with open(input_file) as f:
        lines = f.readlines()
        elf_list = []
        elf_cals = []
        for line in lines:
            if line == '\n':
                elf_list.append(sum(elf_cals))
                elf_cals = []
                continue
            elf_cals.append(int(line.strip()))
        elf_list.sort(reverse=True)
        print(elf_list)
        print(elf_list[:3])
        print(f'top 3 combined cal: {sum(elf_list[:3])}')

if __name__ == '__main__':
    main()