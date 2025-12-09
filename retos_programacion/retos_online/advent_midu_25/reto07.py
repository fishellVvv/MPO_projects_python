def draw_tree(height, ornament, frequency):
    tree = ""
    count = 0

    for i in range(height):
        for j in range(height + i):
            if j < height - (i + 1):
                tree += " "
            else:
                count += 1
                tree += "*" if count % frequency != 0 else ornament
        tree += "\n"

    tree += (" " * (height - 1)) + "#"
    
    return tree

print(draw_tree(5, 'o', 2))
#     *
#    o*o
#   *o*o*
#  o*o*o*o
# *o*o*o*o*
#     #

print(draw_tree(3, '@', 3))
#   *
#  *@*
# *@**@
#   #

print(draw_tree(4, '+', 1))
#    +
#   +++
#  +++++
# +++++++
#    #