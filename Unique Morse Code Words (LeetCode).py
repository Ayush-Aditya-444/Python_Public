import string

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        lookup_dict = {a: m for a, m in zip(string.ascii_lowercase, morse_list)}
        seen = set()

        for w in words:
            concat_morse = ''
            for letter in w:
                morse = lookup_dict[letter]
                concat_morse += morse

            seen.add(concat_morse)

        return len(seen)