#!/usr/bin/env python3

from math import sqrt
from operator import mul

def manhattan(xs, ys):
    return sum(map(lambda x, y: abs(x - y), xs, ys))

def euclidean(xs, ys):
    return sqrt(sum(map(lambda x, y: (x - y) ** 2, xs, ys)))

def chebyshev(xs, ys):
    return max(map(lambda x, y: abs(x - y), xs, ys))

def cosine(xs, ys):
    return sum(map(mul, xs, ys)) / (sqrt(sum(map(mul, xs, xs))) * sqrt(sum(map(mul, ys, ys))))

diff = manhattan

def guess_language(filename):
    with open(filename, encoding='utf-8') as textfile, open('data.csv', encoding='utf-8') as data:
        (_, *letters), *rows = zip(*[line.split(',') for line in data.read().splitlines()])
        text = ''.join(filter(letters.__contains__, textfile.read().casefold()))
    textfreqs = [text.count(let) / len(text) * 100 for let in letters]
    diffs = {lang: diff(map(float, freqs), textfreqs) for lang, *freqs in rows}
    return min(diffs, key=diffs.get)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(guess_language(sys.argv[1]))
    else:
        print('Pass name of file to read as argument')