FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as local_file:
        local_lst = local_file.readlines()
    return local_lst


def write_todos(lst_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(lst_arg)
        