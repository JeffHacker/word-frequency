import re

with open('sample.txt', ) as temp_file:
    text_to_analyze = temp_file.read()
    text_to_analyze = re.sub(r'[^A-Za-z\s]', "", text_to_analyze.lower())
    list_to_analyze = text_to_analyze.split()
    print(text_to_analyze)


histogram = {}

def analyze ():
    for word in list_to_analyze:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1


analyze()
print(histogram)
