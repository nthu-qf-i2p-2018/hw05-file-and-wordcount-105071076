
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
import csv
import json
import pickle
from collections import Counter


def main(filename):
    # read file into lines
    lines = open(filename,'r').read().split()

    # declare a word list
    all_words = []
    symbols = "~!@#$%^&*()_+={}|\"'?><,./-:;"

    # extract all words from lines
    for line in lines:
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
        words = line.split()

        # check the format of words and append it to "all_words" list
        for word in words:
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"
            for i in range(0, len(symbols)):
                word = word.strip(symbols[i])
            # check if word is not empty
            if word :
                # append the word to "all_words" list
                all_words.append(word)

    # compute word count from all_words
    counter = Counter(all_words)

    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    with open("wordcount.csv",'w') as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csv_file)
        # write table head
        head = ['word', 'count']
        writer.writerow(head)
        # write all (word, count) pair into the csv writer
        for elements, value in counter.most_common() : 
           writer.writerow([elements, str(value)])

    # dump to a json file named "wordcount.json"
    j = json.dumps(counter.most_common())
    with open("wordcount.json", 'w') as json_file:
        json_file.write(j)

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly
    with open("wordcount.pkl" , 'wb') as pkl_file:
        pickle.dump(counter, pkl_file)


if __name__ == '__main__':
    main("i_have_a_dream.txt")

