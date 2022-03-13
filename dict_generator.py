def create_dict():
    input_colors = open("input_colors.txt")
    words = [str(line) for line in input_colors]
    formatted_words = [color_name[:-1] for color_name in words]

    input_tuples = open("input_tuples.txt")

    rgbs = [str(line) for line in input_tuples]
    preformatted_rgbs = [rgb_code.replace('(', '') for rgb_code in rgbs]
    formatted_rgbs = [rgb_code.replace(')', '') for rgb_code in preformatted_rgbs]

    colors = dict(zip(formatted_words, formatted_rgbs))
    return colors

