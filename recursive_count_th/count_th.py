'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
 
    count = 0
    letter_index = 0
    if len(word) <= 1:
        return 0

    if word[letter_index : letter_index + 2] == "th":
            count += 1 + count_th(word[letter_index + 1: ])
 
    if word[letter_index: letter_index + 2] != "th":
        count = count_th(word[letter_index + 1: ])
    return count
