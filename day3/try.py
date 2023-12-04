def get_non_alphanumeric_symbols(mat):
    symbols = set()

    for row in mat:
        for char in row:
            # Check for a non-digit, non-alphanumeric symbol
            if char != '.' and not (char.isdigit() or char.isalpha()):
                symbols.add(char)

    return symbols

# Example usage:
filename = 'engine.txt'
with open(filename) as f:
    mat = [list(line) for line in f]

non_alphanumeric_symbols = get_non_alphanumeric_symbols(mat)

print("Non-digit and non-alphanumeric symbols:", non_alphanumeric_symbols)