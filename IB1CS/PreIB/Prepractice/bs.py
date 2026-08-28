with open("test.txt") as f:
    for line in f:
        words = line.split()
        final = ""

        for (index, word) in enumerate(words):
            final += f"{word} ({index + 1})"
        print(final)