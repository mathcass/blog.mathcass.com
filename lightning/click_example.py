from __future__ import print_function

import click


@click.command()
@click.option('--inputf', required=True, help="Input filename")
@click.option('--outputf', required=True, help="Output filename")
@click.option('--split-size', default=10, help="Total variables to use per tree")
@click.option('--n-trees', default=1000, help="Total trees to train")
def run(inputf, outputf, split_size, n_trees):
    """Runs a training on the input file
    """
    print(inputf, outputf, split_size, n_trees)


if __name__ == '__main__':
    run()
