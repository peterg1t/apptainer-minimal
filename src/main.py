#!/usr/bin/python3

import sys
import csv
import plotext as plt


def execute_function(file_input: str):
    print("Hello from program")

    days = []
    values = []

    with open(file_input, mode="r", encoding="utf-8") as f:
        data = csv.reader(
            f,
            delimiter=",",
            skipinitialspace=True,
            quotechar="|"
        )

        # Skip CSV header
        next(data, None)

        for row in data:
            try:
                days.append(int(row[0]))
                values.append(float(row[1]))
            except (ValueError, IndexError) as exc:
                print(f"Skipping invalid row {row}: {exc}")

    print(days, values)

    fig=plt.figure
    fig.clear()

    signal = fig.signal(days,values).lines()

    fig.draw(signal)
    fig.line(200,pixel=("red+", "black")) 
    fig.line(150,pixel=("orange+", "black"))
    fig.line(100,pixel=("green+", "black"))
    fig.title("Radon")
    fig.label("Days", axis="x")
    fig.label("[bq/m^3]", axis="y")
    fig.ruler("y").lim(lower=0, upper=300)
    fig.canvas("black")
    fig.show()



if __name__ == "__main__":
    if len(sys.argv) == 2:
        execute_function(sys.argv[1])
    else:
        print(
            "Wrong number of arguments, only one file "
            "should be passed to this program."
        )
        print("... Exiting now")
        sys.exit(1)
