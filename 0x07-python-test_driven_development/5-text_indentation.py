def text_indentation(text):
    """
    Function that prints 2 new lines after these chars:
    ".", "?" and ":"
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    # initialize variable to hold final string
    final_str = ""

    # flag to skip/trim leading whitespaces
    flag = True

    # iterate through all chars in the given text
    for char in text:
        # check if char is one of these: '.', '?' or ':'
        if char in ".?:":
            final_str += char + "\n\n"  # add char and two new lines
            flag = True  # set flag to skip leading whitespaces
        elif char != " " or not flag:
            final_str += char
            flag = False  # reset flag if it's a non-space character

    print(final_str)
