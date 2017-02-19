file = open('words.txt')
anagram_dictionary = {}

for word in file:
    word_list = list(word)  # Takes in a word and turns it into a list then sorts letters
    word_list.sort()
    
    if tuple(word_list) not in anagram_dictionary:  # Turns sorted list of words into a tuple and then adds to dictionary
        temp_list = [word]
        anagram_dictionary[tuple(word_list)] = temp_list
            
    anagram_dictionary[tuple(word_list)].append([word]) # Sorts all words together that have the same group of letters


print anagram_dictionary