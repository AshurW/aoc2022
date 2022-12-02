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
            score = o_hand.index(g[0]) - p_hand.index(g[1])
            print(score)
            if score == -2:
                print(lost, points[p_hand.index(g[1])])
                total_score += lost + points[p_hand.index(g[1])]
            if score == -1:
                print(win, points[p_hand.index(g[1])])
                total_score += win + points[p_hand.index(g[1])]
            if score == 0:
                print(draw, points[p_hand.index(g[1])])
                total_score += draw + points[p_hand.index(g[1])]
            if score == 1:
                print(lost, points[p_hand.index(g[1])])
                total_score += lost + points[p_hand.index(g[1])]
            if score == 2:
                print(win, points[p_hand.index(g[1])])
                total_score += win + points[p_hand.index(g[1])]

        print(total_score)

if __name__ == '__main__':
    main()