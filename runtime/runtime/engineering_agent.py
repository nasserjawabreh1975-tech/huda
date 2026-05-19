from engineering.boq_analyzer import analyze_boq


def engineer(path):

    return analyze_boq(path)


if __name__ == "__main__":

    print(
        engineer(
            "sample_boq.txt"
        )
    )
