import re
import os
os.system("clear")
# import collections # Google search

with open('sample.txt', ) as temp_file:
    text_to_analyze = temp_file.read()
    # got help on the \s from Soren
    text_to_analyze = re.sub(r'[^A-Za-z\s]', "", text_to_analyze.lower())
    list_to_analyze = text_to_analyze.split()
    #  print(text_to_analyze)

histogram = {}


def word_frequency(list_to_analyze, histogram):
    for word in list_to_analyze:  # class work
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

word_frequency(list_to_analyze, histogram)

# def sorted_by_val():
sorted_by_val = sorted(histogram.items(), key=lambda t: t[1], reverse=True)
print(sorted_by_val[:19])

# print(type(sorted_by_val))
# histogram_list = histogram.items()
# print(histogram_list)
