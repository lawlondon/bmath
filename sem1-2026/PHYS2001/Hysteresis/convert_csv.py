import argparse
import csv
import os


def scientificToDecimal(inputCSV, outputCSV):
    if not os.path.exists(inputCSV):
        print("bogus path")
        return

    try:
        with open(inputCSV, "r") as inputFile:
            input = csv.reader(inputFile)
            convertedRows = []

            for row in input:
                newRow = []
                for cell in row:
                    cleanedCell = cell.strip()
                    if cleanedCell:
                        try:
                            value = float(cleanedCell)
                            cleanedValue = format(value, ".15f").rstrip("0").rstrip(".")
                            newRow.append(cleanedValue if cleanedValue != "" else "0")
                        except ValueError:
                            newRow.append(cell)
                    else:
                        newRow.append(cell)

                convertedRows.append(newRow)

        with open(outputCSV, "w", newline="") as outputFile:
            writer = csv.writer(outputFile)
            writer.writerows(convertedRows)

        print("done")

    except Exception as exception:
        print(f"womp womp: {exception}")


def main():
    parser = argparse.ArgumentParser(description="scientific notation to decimal")

    parser.add_argument("-i", "--input", required=True, help="source csv path")
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="optional output csv path",
    )

    args = parser.parse_args()

    if args.output is None:
        inputPath = os.path.abspath(args.input)
        inputPathDirname = os.path.dirname(inputPath)
        defaultOutputPath = os.path.splitext(os.path.basename(inputPath))[0]

        args.output = os.path.join(inputPathDirname, f"{defaultOutputPath}.output.csv")

    scientificToDecimal(args.input, args.output)


if __name__ == "__main__":
    main()
