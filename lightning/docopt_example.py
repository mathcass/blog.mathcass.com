"""Docopt

Usage:
  docopt.py (--input=<input>) (--output=<output>) [--split-size=<split_size>] [--n-trees=<n_trees>]

Options:
  -i <input> --input=<input>                  Input filename
  -o <output> --output=<output>               Output filename
  -s <split_size> --split-size=<split_size>   Total variables to use per tree [default: 10]
  -n <n_trees> --n-trees=<n_trees>            Total trees to train [default: 1000]

"""

from docopt import docopt


def main(args):
    print(args)


if __name__ == '__main__':
    main(docopt(__doc__))
