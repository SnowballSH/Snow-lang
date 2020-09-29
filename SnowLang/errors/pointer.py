def point(code, pos):
    """
    generates the pointer of error
    :param code: the code as string
    :param pos: the position as tuple[line, char]
    :return: str of pointer
    """
    return code.split("\n")[pos[0]-1] + "\n" + " " * (pos[1]) + "^"
