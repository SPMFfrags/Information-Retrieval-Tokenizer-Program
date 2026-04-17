import sys


# ---------------------------------------------------------
# tokenize(file_path)
# Runtime Complexity: O(n)
# n = number of characters in the file.
# Each character is processed exactly once.
# The file is read line-by-line so large files are supported.
# ---------------------------------------------------------
def tokenize(file_path):

    tokens = [ ]

    try:
        with open(file_path, "r", encoding="utf-8") as file:

            current = " "

            for line in file:
                for character in line:

                    if character.isalnum() and (
                            ('a' <= character <= 'z') or ('A' <= character <= 'Z') or ('0' <= character <= '9')):
                        # Apple, apple, aPpLe are the same token
                        current = current + character.lower()

                    else:
                        if current != " ":
                            tokens.append(current)
                            current = " "

                if current != " ":
                    tokens.append(current)
                    current = " "

    except Exception:
        print("Cannot read the file.")

    return tokens


# ---------------------------------------------------------
# computeWordFrequencies(tokens)
# Runtime Complexity: O(n)
# n = number of tokens.
# Each token is inserted or updated in a dictionary once.
# ---------------------------------------------------------
def computeWordFrequencies(tokens):

    frequency = { }

    for token in tokens:

        if token in frequency:
            frequency[token] = frequency[token] + 1
        else:
            frequency[token] = 1

    return frequency


# ---------------------------------------------------------
# print_frequencies(frequency)
# Runtime Complexity: O(n log n)
# n = number of unique tokens.
# Sorting is required to print by decreasing frequency if the frequency is tied sort alphabetically.
# ---------------------------------------------------------
def print_frequencies(frequency):

    sorted_tokens = list(frequency.items())
    # Use lambda to create a function to sort tokens in decreasing frequency and in alphabetical order
    sorted_tokens.sort(key=lambda item: (-item[1], item[0]))

    for token, count in sorted_tokens:
        print(token + "\t" + str(count))


def main():

    if len(sys.argv) != 2:
        print("python PartA.py file.txt")
        sys.exit()

    file_path = sys.argv[1]

    tokens = tokenize(file_path)
    freq = computeWordFrequencies(tokens)

    print_frequencies(freq)

if __name__ == "__main__":
    main()