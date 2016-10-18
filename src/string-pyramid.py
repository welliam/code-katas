def watch_pyramid_from_the_side(characters):
    """A pyramid built from the input as view from the side."""
    if not characters:
        return characters
    length = len(characters)
    res = ''
    for i, c in list(enumerate(characters)):
        res = ' ' * i + c * (2 * (length - i) - 1) + ' ' * i + '\n' + res
    return res[:-1]


def watch_pyramid_from_above_row(characters, row):
    """The rowth row of the pyramid being built from characters."""
    res = ''
    for col in range(len(characters)):
        res += characters[min(row, col)]
    for col in range(len(characters) - 2, -1, -1):
        res += characters[min(row, col)]
    res += '\n'
    return res


def watch_pyramid_from_above(characters):
    """A pyramid built from the input as view from above."""
    if not characters:
        return characters
    res = ''
    for row in range(len(characters)):
        res += watch_pyramid_from_above_row(characters, row)
    for row in range(len(characters) - 2, -1, -1):
        res += watch_pyramid_from_above_row(characters, row)
    return res[:-1]


def count_visible_characters_of_the_pyramid(characters):
    """The number of visible characters when viewed from above."""
    if not characters:
        return -1
    return (len(characters) * 2 - 1) ** 2


def count_all_characters_of_the_pyramid(characters):
    """The number of characters used to build the pyramid."""
    if not characters:
        return -1
    n = len(characters)
    return n * (4 * n**2 - 1) / 3
