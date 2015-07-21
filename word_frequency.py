import re
import os
os.system("clear")
# import collections # Google search

# adding user input to select file to analyze
print("What file would you like to do a word count on?  Choose one!")
print("\n")
print("Here is a list of your choices:")
print("------------")
print("sample.txt")
print("the_young_explorer.rtf")
print("phil_the_fiddler.rtf")
print("war_and_peace.rtf")
print("------------")
file_to_analyze = input("Which do you choose?  ")

with open(file_to_analyze) as temp_file:
    text_to_analyze = temp_file.read()
    # got help on the \s from Soren
    text_to_analyze = re.sub(r'[^A-Za-z\s]', "", text_to_analyze.lower())
    list_to_analyze = text_to_analyze.split()
    # print(text_to_analyze)


def word_frequency(list_to_analyze):
    histogram = {}
    ignore_list = ('a', 'able', 'about', 'across', 'after', 'all', 'almost',
                   'also', 'am', 'among', 'an', 'and', 'any', 'are', 'as',
                   'at', 'be', 'because', 'been', 'but', 'by', 'can', 'cannot',
                   'could', 'dear', 'did', 'do', 'does', 'either', 'else',
                   'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has',
                   'have', 'he', 'her', 'hers', 'him', 'his', 'how', 'however',
                   'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least',
                   'let', 'like', 'likely', 'may', 'me', 'might', 'most',
                   'must', 'my', 'neither', 'no', 'nor', 'not', 'of', 'off',
                   'often', 'on', 'only', 'or', 'other', 'our', 'own',
                   'rather', 'said', 'say', 'says', 'she', 'should', 'since',
                   'so', 'some', 'than', 'that', 'the', 'their', 'them',
                   'then', 'there', 'these', 'they', 'this', 'tis', 'to',
                   'too', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what',
                   'when', 'where', 'which', 'while', 'who', 'whom', 'why',
                   'will', 'with', 'would', 'yet', 'you', 'your')

    for word in list_to_analyze:  # class work
        if word in ignore_list:
            pass
        else:
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1

        # if word not in ignore_list:
        #     if word in histogram:
        #         histogram[word] += 1
        #     else:
        #         histogram[word] = 1
#   print(histogram)
    return histogram

histogram = word_frequency(list_to_analyze)
# print(type(histogram))
# def sorted_by_val():
sorted_by_val = sorted(histogram.items(), key=lambda t: t[1], reverse=True)

_, hash_b = sorted_by_val[0]
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
