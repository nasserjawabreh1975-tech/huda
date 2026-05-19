from runtime.real_executor import execute_python


def execute_task(code):

    return execute_python(code)


if __name__ == "__main__":

    sample = """
print("EXECUTION AGENT ACTIVE")
"""

    print(
        execute_task(sample)
    )
