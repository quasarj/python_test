"""
    Python Test

    Explain why this works (including as much detail as possible).

"""

input = [1, 2, 3, 4, 5, 6]
output = dict(zip(*[iter(input)]*2))
print(output)
