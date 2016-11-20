import random


class Generator:
    def __init__(self, letter_dist):
        """

        :type letter_dist: dict
        """
        self.vowel_str = 'aeıioöuü'
        self.cons_str = 'rtypsdfghjklzcvbnmğşç'
        self.vowels = [letter_dist[ch] for ch in self.vowel_str]
        self.consonants = [letter_dist[ch] for ch in self.cons_str]

        self.n_consonants = len(self.cons_str)
        self.n_vowels = len(self.vowel_str)

    def new_word(self):
        output = ''

        vowels_by_now = 0
        cons_by_now = 0

        word_len = random.randint(2, 10)

        # add initial letter by 50% chance
        starts_with_vowel = random.randint(0, 2) == 0
        if starts_with_vowel:
            output += self._get_random_vowel()
            vowels_by_now += 1
        else:
            output += self._get_random_consonant()
            cons_by_now += 1

        # TODO: do not use 2 consonants as the first 2 letters.

        while len(output) < word_len:
            # if the last letter was a vowel
            if vowels_by_now == 1:
                ch = self._get_random_consonant()
            # if the last letter was a consonant
            else:
                # if we have 1 consonant so far at the end of the word, it's optional to continue with a consonant
                # or not
                if cons_by_now < 2:
                    # TODO: Here, this can be provided to get a random value according to real words
                    continue_with_vowel = random.randint(0, 10) < 6

                    if continue_with_vowel:
                        ch = self._get_random_vowel()
                    else:
                        ch = self._get_random_consonant()
                # but if we have 2, it's forbidden to add another consonant to the word, so we're adding a vowel to it
                else:
                    ch = self._get_random_vowel()

            if ch in self.vowel_str:
                vowels_by_now += 1
                cons_by_now = 0
            else:
                vowels_by_now = 0
                cons_by_now += 1

            output += ch

        # TODO: do not allow 2 consonants for words in size of 2 letters
        return output


    def _get_random_consonant(self):
        """get a random consonant"""
        random_factor = 100.0
        letter_roll = 0

        while random_factor > 0.0:
            letter_roll = random.randint(0, self.n_consonants - 1)

            random_factor -= self.consonants[letter_roll]

        return self.cons_str[letter_roll]

    def _get_random_vowel(self):
        """get a random vowel"""
        random_factor = 100.0
        letter_roll = 0

        while random_factor > 0.0:
            letter_roll = random.randint(0, self.n_vowels - 1)

            random_factor -= self.vowels[letter_roll]

        return self.vowel_str[letter_roll]

    def mutate_word(self, factor):
        """Perform slight changes to given word and return it
        :type factor: float between 0 and 1
        """
        pass

    def _apply_grammar(self):
        """Turkish language, includes banned combinations of consonants and vowels.

        1. Letters n and b cannot stand next to each other in form of 'nb' that part of any word must automatically
        turned into 'mb' instead.

        (see: pembe)
        (see: bomba)

        2. Words cannot start with the letter Ğ.

        3. Turkish words must have vowel harmony

        (see: televizyon) This word is not Turkish (french origin) and we can understand it from vowel harmony.
        After the 'e' (or 'i', which also breaks the rule) voice, the 'o' voice arrives in a sequence. That is not a
        valid case in Turkish words.
        """
        pass

if __name__ == '__main__':

    # taken from letter_analyze/letter-freq.csv
    frequencies = {
        'g': 1.00,
        'd': 3.71,
        'k': 4.94,
        'ç': 2.11,
        'c': 1.78,
        'y': 3.00,
        'o': 1.82,
        'ş': 0.89,
        'h': 1.04,
        'ö': 0.74,
        'm': 3.78,
        't': 2.89,
        'f': 0.29,
        'a': 11.92,
        's': 4.01,
        'i': 8.09,
        'j': 0.07,
        'e': 10.51,
        'p': 0.26,
        'ı': 5.34,
        'l': 4.79,
        'u': 2.52,
        'ü': 1.96,
        'b': 2.22,
        'z': 2.60,
        'n': 6.94,
        'r': 6.90,
        'v': 2.63,
        'ğ': 1.11
    }
    gen = Generator(frequencies)
    print(gen.new_word())