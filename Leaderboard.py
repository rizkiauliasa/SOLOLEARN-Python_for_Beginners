# Strings


# You need to make a program for a leaderboard.
# The program needs to output the numbers 1 to 9, each on a separate line, followed by a dot:
# 1.
# 2.
# 3.
# ...

# You can use the \n newline character to create line breaks, or, alternatively, create the desired output using three double quotes """.

#your code goes here
for i in range(9):
    i += 1
    l = str(i)
    print(l + '.')