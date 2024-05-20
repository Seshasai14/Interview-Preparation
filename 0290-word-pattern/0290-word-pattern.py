class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # Split the string into words

        if len(pattern) != len(words):
            return False  # If the lengths do not match, it cannot follow the pattern

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False  # The current word does not match the expected word
            else:
                char_to_word[char] = word  # Map the character to the word

            if word in word_to_char:
                if word_to_char[word] != char:
                    return (
                        False  # The current character does not match the expected character
                    )
            else:
                word_to_char[word] = char  # Map the word to the character

        return True
