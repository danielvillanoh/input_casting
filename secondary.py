# author: Daniel
# date: Villano-Herrera

# -------------------- Section 4 -------------------- #

# Input | ASCII Art


# Objectives:
#   1. Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol | Integer / Float | The symbol used to create the diamond.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Call the function you defined to create the diamond, sending the character as an argument.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> $
#
#           $
#          $$$
#         $$$$$
#        $$$$$$$
#       $$$$$$$$$
#      $$$$$$$$$$$
#     $$$$$$$$$$$$$
#      $$$$$$$$$$$
#       $$$$$$$$$
#        $$$$$$$
#         $$$$$
#          $$$
#           $
#
# ---- WRITE CODE BELOW ---- #
def diamond(symbol):
    return (' ' * 11 + symbol + '\n'
            + ' ' * 10 + symbol * 3 + '\n'
            + ' ' * 9 + symbol * 5 + '\n'
            + ' ' * 8 + symbol * 7 + '\n'
            + ' ' * 7 + symbol * 9 + '\n'
            + ' ' * 6 + symbol * 11 + '\n'
            + ' ' * 5 + symbol * 13 + '\n'
            + ' ' * 6 + symbol * 11 + '\n'
            + ' ' * 7 + symbol * 9 + '\n'
            + ' ' * 8 + symbol * 7 + '\n'
            + ' ' * 9 + symbol * 5 + '\n'
            + ' ' * 10 + symbol * 3 + '\n'
            + ' ' * 11 + symbol + '\n'
            )


symbols = input('Type a symbol: ')
print(diamond(symbols))


#   2. Framed Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol1 | Integer / Float | The symbol used to create the diamond.
#           symbol2 | Integer / Float | The symbol used to create the frame.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Prompt input from the user in the form of a single character again, and save it to a second variable.
#       d. Call the function you defined to create the framed diamond, sending the characters as arguments.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> &
#   >> ~
#
#     ~~~~~~$~~~~~~
#     ~~~~~$$$~~~~~
#     ~~~~$$$$$~~~~
#     ~~~$$$$$$$~~~
#     ~~$$$$$$$$$~~
#     ~$$$$$$$$$$$~
#     $$$$$$$$$$$$$
#     ~$$$$$$$$$$$~
#     ~~$$$$$$$$$~~
#     ~~~$$$$$$$~~~
#     ~~~~$$$$$~~~~
#     ~~~~~$$$~~~~~
#     ~~~~~~$~~~~~~
#
# ---- WRITE CODE BELOW ---- #
def diamond_disillusion(symbol1, symbol2):
    return (symbol2 * 11 + symbol1 + symbol2 * 11 + '\n'
            + symbol2 * 10 + symbol1 * 3 + symbol2 * 10 + '\n'
            + symbol2 * 9 + symbol1 * 5 + symbol2 * 9 + '\n'
            + symbol2 * 8 + symbol1 * 7 + symbol2 * 8 + '\n'
            + symbol2 * 7 + symbol1 * 9 + symbol2 * 7 + '\n'
            + symbol2 * 6 + symbol1 * 11 + symbol2 * 6 + '\n'
            + symbol2 * 5 + symbol1 * 13 + symbol2 * 5 + '\n'
            + symbol2 * 6 + symbol1 * 11 + symbol2 * 6 + '\n'
            + symbol2 * 7 + symbol1 * 9 + symbol2 * 7 + '\n'
            + symbol2 * 8 + symbol1 * 7 + symbol2 * 8 + '\n'
            + symbol2 * 9 + symbol1 * 5 + symbol2 * 9 + '\n'
            + symbol2 * 10 + symbol1 * 3 + symbol2 * 10 + '\n'
            + symbol2 * 11 + symbol1 + symbol2 * 11 + '\n'
            )


symbols = input('Type a symbol for the diamond: ')
another_symbol = input('Type another symbol for the frame: ')
print(diamond_disillusion(symbols, another_symbol))
