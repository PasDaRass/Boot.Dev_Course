def count_vowels(text):
    count = 0
    vowels_set = set()

    vowels_lower = [ "a", "e", "i", "o", "u" ]
    vowels_upper = [ "A", "E", "I", "O", "U" ]
    for letter in text:
        if letter in vowels_lower:
            vowels_set.add(letter)
            count += 1
        elif letter in vowels_upper:
            vowels_set.add(letter)
            count += 1

    return count, vowels_set
  
