import re
import os
os.system("clear")
# import collections # Google search

with open('sample.txt', ) as temp_file:
    text_to_analyze = temp_file.read()
    # got help on the \s from Soren
    text_to_analyze = re.sub(r'[^A-Za-z\s]', "", text_to_analyze.lower())
    list_to_analyze = text_to_analyze.split()
    # print(text_to_analyze)


def word_frequency(list_to_analyze):
    histogram = {}
    for word in list_to_analyze:  # class work
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
#   print(histogram)
    return histogram

histogram = word_frequency(list_to_analyze)
# print(type(histogram))
# def sorted_by_val():
sorted_by_val = sorted(histogram.items(), key=lambda t: t[1], reverse=True)

# _____________

hash_a, hash_b = sorted_by_val[0]
hash_mult = 50 / int(hash_b)
# print("hash mult is {}".format(hash_mult))

print("Here are the top 20 words.")
print("\n")
counter = 0
while counter < 20:
    word, word_count = sorted_by_val[counter]
    # print("word {}".format(word))
    # print("word count {}".format(int(word_count)))
    counter += 1
    hashes = word_count * hash_mult
    # print(hashes)
    # print(word)
    # print(word_count)
    print(word + "\n" + "#" * int(hashes))
print("\n")
print("\n")
print("\n")
