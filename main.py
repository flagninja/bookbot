def main():
    book_path = "books/frankenstein.txt"
    contents = get_book_contents(book_path)
    print("There are " + str(word_count(contents)) + " words in the text")
    character_counts = letter_count(contents)
    format_counts(character_counts)

def get_book_contents(path):
    with open(path) as f:
        contents = f.read()
        return contents

def word_count(text):
    split_text = text.split()
    return len(split_text)
    
def letter_count(text):
    lower_text = text.lower()
    letters = {}
    for letter in lower_text:
        if not letter in letters:
            letters[letter] = 0
        letters[letter] += 1
    return letters

def format_counts(counts):
    char_list = counts.copy().keys()
    sort_list = []
    #strip nonalpha characters from the character counts
    for c in char_list:
        if not c.isalpha():
            counts.pop(c)
        else:
            sort_list.append({"char": c , "count": counts[c]})
    #sort the counts high to low
    sort_list.sort(reverse=True,key=lambda d : d["count"]) #lambda function to grab counts out of dict
    #print the sorted list with some formatting
    for i in sort_list:
        print(f"the {i["char"]} character appears {i["count"]} times")

main()