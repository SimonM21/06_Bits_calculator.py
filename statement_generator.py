# Functioon go here

# Puts sereis of symbol ata statr and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# Main Routine goes here
statement_generator("look - stars", "*")