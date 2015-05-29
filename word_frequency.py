import re
# import collections # Google search

with open('sample.txt', ) as temp_file:
    text_to_analyze = temp_file.read()
    text_to_analyze = re.sub(r'[^A-Za-z\s]', "", text_to_analyze.lower()) #got help on the \s Sorren
    list_to_analyze = text_to_analyze.split()
    #  print(text_to_analyze)


histogram = {}


for word in list_to_analyze: # class work
    if word in histogram:
        histogram[word] += 1
    else:
        histogram[word] = 1


# list(histogram.items())
# print(histogram)
# histogram = sorted((v, k) for k, v in histogram.items()) # Google search
#  print(histogram)


for key in sorted(histogram):
	print(key, ':', histogram[key])


# analyze()
# sorted_list()
# print(histogram)
