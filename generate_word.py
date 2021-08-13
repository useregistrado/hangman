import random as rm


def get_word():
    words = []
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            word = line.replace("\n", "")
            for a, b in replacements:
                word = word.replace(a, b)
            words.append(word)
    f.close()
    return rm.choice(words)


if __name__ == "__main__":
    print(get_word())