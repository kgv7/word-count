# put your code here.
def word_count(file):
    filename = open(file)

    word_count = {}

    for line in filename:
        words = line.rstrip().split(" ")

        for word in words:
            word = word.rstrip(",).?!'\"_")
            word = word.lstrip("(\"'_")
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(word_count("twain.txt"))