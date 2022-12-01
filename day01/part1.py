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
                print(elf_cals)
                elf_list.append(sum(elf_cals))
                elf_cals = []
                continue
            elf_cals.append(int(line.strip()))
        print(elf_list)
        elf_w_most = elf_list.index(max(elf_list))
        print(f'elf nr {elf_w_most} has the most cal {elf_list[elf_w_most]}')

if __name__ == '__main__':
    main()