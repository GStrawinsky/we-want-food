import argparse
import sys


def run(args):
    pass


def validate(args):
    if args.meals is not None and 0 > args.meals:
        print("Meals must be a non-negative number", file=sys.stderr)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Program for automating the generation of meal \
                     plans and their associated ingredients")
    parser.add_argument("-m", "--meals", type=int, default=3,
                        help="The number of meals to generate")
    parser.add_argument("-i", "--interactive", default=False, type=bool,
                        metavar="I", help="Should prompt be interactive")
    parser.add_argument("-f", "--file", type=str, default="meals.json",
                        help="Path to the meals file")

    args = parser.parse_args()
    validate(args)
    run(args)
