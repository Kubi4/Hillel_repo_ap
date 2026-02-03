h_in_word = False
while h_in_word == False:
    word_with_h = input("Enter a word with 'h': \n")
    for el in word_with_h:
        if el.lower() == "h":
            h_in_word = True
