import string

# Normalize the word to lowercase, no punctuation
def normalize_word(word):
    # make all words lowercase
    normalized_word = word.lower().rstrip()
    
    # strip out any punctuation
    normalized_word = normalized_word.translate(str.maketrans(dict.fromkeys(string.punctuation)))
    
    return normalized_word

# open poem.txt and parse as lines of text
with open('poem.txt', encoding="utf-8") as file_object:
    lines = file_object.readlines()

# build a word count map
word_counts = {}
for line in lines:
    # parse each line
    
    # split the line into words
    words = list(line.split(" "))
    print(words)

    # for each word, normalize and keep count
    for word in words:
        normalized_word = normalize_word(word)
        
        # make sure words are significant (i.e. > 3 characters)
        if(len(word) > 3):
            count = word_counts.get(normalized_word, 0)
            word_counts[normalized_word] = (count + 1)

# print out the map in decreasing order
for word in sorted(word_counts): 
    print(f"{word}: {word_counts[word]}")
