def spin_words(string):
    word: str = "Ночь"
    final_word: str = "День"
    final_list: list = []
    words = string.split()
    for i in range (len(words)):
        if len(words[i]) >= 5:
            word = words[i]
            final_word = word[::-1]
            final_list.append(final_word)
        else:
            final_list.append(words[i])
    final_string = ' '.join(final_list)
    return final_string


spin_words("Welcome")



