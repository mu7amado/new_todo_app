FilePath = "todos.txt"


def read_todo(filepath=FilePath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg, filepath=FilePath):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(read_todo())
