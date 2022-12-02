import pdb
import argparse
from pathlib import Path

input_file = Path(__file__).with_name('input.txt')


def main():
    with open(input_file) as f:
        lines = f.readlines()
        o_hand = ['A', 'B', 'C']
        p_hand = ['X', 'Y', 'Z']
        points = [1, 2, 3]
        lost = 0
        draw = 3
        win = 6

        total_score = 0

        for line in lines:
            g = line.split()
            print(g)
            o = g[0]
            p = g[1]
            l = o_hand.index(o) - 1
            d = o_hand.index(o)
            w = o_hand.index(o) + 1
            result = p_hand.index(p)
            if result == 0:
                total_score += lost + points[l]
            if result == 1:
                total_score += draw + points[d]
            if result == 2:
                total_score += win + points[w  if w < len(points) else 0]
         
        print(total_score)

if __name__ == '__main__':
    main()