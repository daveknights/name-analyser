class NameAnalyser:
    pre_text = 'your name '
    VOWELS = ('a', 'e', 'i', 'o', 'u')
    LETTER_VALUES = {
        '1': ('E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U'),
        '2': ('D', 'G'),
        '3': ('B', 'C', 'M', 'P'),
        '4': ('F', 'H', 'V', 'W', 'Y'),
        '5': ('K',),
        '8': ('J', 'X'),
        '10': ('Q', 'Z')
    }
    vowel_count = 0
    vowels_found = []
    scrabble_score = 0

    def __init__(self, name):
        self.name = name

    def iterate_letters(self):
        for letter in self.name:
            for lv in self.LETTER_VALUES:
                if letter.upper() in self.LETTER_VALUES[lv]:
                    self.scrabble_score += int(lv)

            if letter in self.VOWELS:
                self.vowel_count += 1

                if letter not in self.vowels_found:
                    self.vowels_found.append(letter)

    def get_letter_count(self):
        return self.pre_text.capitalize() + 'contains: {} letters.'.format(len(self.name))

    def get_vowel_and_consonant_count(self):
        return self.pre_text.capitalize() + 'contains: {} vowels & {} consonants'.format(self.vowel_count, len(self.name) - self.vowel_count)

    def sort_vowels(self):
        return 'The vowels in {} are {}.'.format(self.pre_text, sorted(self.vowels_found))

    def sort_name_letters(self):
        return 'Here are the letters of {}in alphabetical order: {}'.format(self.pre_text, sorted(self.name.lower()))

    def get_scrabble_score(self):
        return self.pre_text.capitalize() + 'would score {} points in Scrabble.'.format(self.scrabble_score)



name = raw_input('Please enter your first and last name: ').replace(' ', '')
analyse_name = NameAnalyser(name)
analyse_name.iterate_letters()

print(analyse_name.get_letter_count())
print(analyse_name.get_vowel_and_consonant_count())
print(analyse_name.sort_vowels())
print(analyse_name.sort_name_letters())
print(analyse_name.get_scrabble_score())
