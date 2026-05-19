from system.self_healing import auto_fix


def repair(error_text):

    return auto_fix(error_text)


if __name__ == "__main__":

    print(
        repair(
            "vite missing"
        )
    )
