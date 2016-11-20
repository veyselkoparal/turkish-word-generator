"""letter-analyzer.py
analyzes letter frequency distribution using a story story in Turkish."""
import re
import pandas as pd
import os

if not os.path.isfile('letter-freq.csv'):
    # anything else except a-z
    forbidden = "[^a-züğişçöı]"

    letter_freq = {}

    # iterate through text file and sum up letter usage in dict variable
    with open('turkish-word-data', 'r') as textfile:
        for line in textfile:
            # remove non-letter characters
            trimmed_line = re.sub(forbidden, '', line).lower()
            for char in trimmed_line:
                if letter_freq.get(char) is None:
                    letter_freq[char] = 1
                else:
                    letter_freq[char] += 1

    # dump the dict file into a pandas DataFrame
    df = pd.DataFrame.from_dict(letter_freq, 'index')
    df.to_csv('raw-results.csv', header=False)

    total_letter = df.iloc[:,0].sum()

    frequencies = df.apply(lambda value: 100 * (value / total_letter), axis='index')

    print(frequencies)
    print('Total of:', frequencies.iloc[:,0].sum())

    frequencies.to_csv('letter-freq.csv', header=False)

