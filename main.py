def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    print(text)
    word_count(text)


def get_text(path):
  '''Making a script to get text'''
  with open(path) as f:
        return f.read()
  

def word_count(text):
    '''Making a script to count words'''
    words = text.split()
    count = len(words)
    print(f"This document had {count} words")


main()



    

    

