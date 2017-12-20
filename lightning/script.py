import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Input filename", required=True)
    parser.add_argument("-o", help="Output filename", required=True)

    parser.add_argument("--vars-per-split",
                        action="store",
                        help="Number of variables tried per split",
                        type=int,
                        default=10)
    parser.add_argument("--n-trees",
                        action="store",
                        help="Number of trees",
                        type=int,
                        default=1000)

    print parser.parse_args()
