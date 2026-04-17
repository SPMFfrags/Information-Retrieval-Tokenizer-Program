import PartA
import sys

# ---------------------------------------------------------
# intersection(filepath1, filepath2)
# Runtime Complexity: O(n + m)
# n = tokens in file1
# m = tokens in file2
# Tokenizing and building the dictionary are linear operations.
# The loop checking intersections is also linear.
# ---------------------------------------------------------
def intersection(filepath1, filepath2):

    # tokenize and compute word frequencies for file 1
    file1_tokens = PartA.computeWordFrequencies(
        PartA.tokenize(filepath1)
    )

    # tokenize file 2
    file2_tokens = PartA.tokenize(filepath2)

    intersections = set()
    num_common = 0

    # check tokens from file2 against file1 dictionary
    for token in file2_tokens:

        if token in file1_tokens:
                intersections.add(token)
                num_common = len(intersections)

    # IMPORTANT: last line must ONLY be the number
    print(num_common)

def main():
    if len(sys.argv) != 3:
        print("python PartB.py file1.txt file2.txt")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    intersection(file1, file2)

if __name__ == "__main__":
    main()