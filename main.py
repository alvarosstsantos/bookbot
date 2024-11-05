
def main():
    with open("./books/frankenstein.txt") as f:
        text = f.read()

        generate_report(text)


def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict:
    characters = {}

    for c in text.lower():
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1

    return characters


def sort_alphabet_characters(characters: dict):
    new_characters = []

    for k in characters:
        if k.isalpha():
            new_characters.append({"character": k, "count": characters[k]})

    return sorted(new_characters, key=lambda k: k['character'])


def generate_report(text: str) -> None:
    word_count = count_words(text)
    characters = count_characters(text)
    sorted_alphabet_characters = sort_alphabet_characters(characters)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document", end="\n\n")

    for item in sorted_alphabet_characters:
        print(f"The '{item["character"]}' character was found {
              item['count']} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()
