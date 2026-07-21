import argparse
import csv
import os

import numpy as np


def polyFit(inputCSV, degree):
    if not os.path.exists(inputCSV):
        print("bogus path")
        return

    if degree < 2:
        print("degree must greater than 2")
        return

    try:
        with open(inputCSV, "r", newline="") as inputFile:
            x, y = [], []
            for row in csv.DictReader(inputFile):
                x.append(float(row["x"]))
                y.append(float(row["y"]))

        coefficients = np.polyfit(x, y, degree)

        labels = "abcdefghijklmnopqrstuvwxyz"
        terms = []

        for i, c in enumerate(coefficients):
            power = degree - i
            label = labels[i]
            if power == 0:
                terms.append(f"{c:+.6g} ({label})")
            elif power == 1:
                terms.append(f"{c:+.6g}x ({label})")
            else:
                terms.append(f"{c:+.6g}x^{power} ({label})")

        print(f"f(x)= " + " ".join(terms))

    except Exception as fuck_up:
        print(f"womp womp: {fuck_up}")


def main():
    parser = argparse.ArgumentParser(description="csv to polynomial")
    parser.add_argument("-i", "--input", required=True, help="source csv path")
    parser.add_argument("-d", "--degree", default=5, help="polynomial degree")
    args = parser.parse_args()

    polyFit(args.input, args.degree)


if __name__ == "__main__":
    main()
