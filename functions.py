FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of
    todo items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the todo item list in a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


#print(get_todos())

if __name__ == "__main__":
    print(get_todos())