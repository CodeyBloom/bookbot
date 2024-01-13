def main():
    '''Making a script to print the file contents'''
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
        
    '''Making a script to count the words'''
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1
    print(f"This document had {count} words")

main()

    
