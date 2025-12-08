def spin_words(words, final_list):
    for i in range (len(words)):
        if len(words[i]) >= 5:
            word = words[i]
            final_word = word[::-1]
            final_list.append(final_word)
        else:
            final_list.append(words[i])
    return final_list

string = str(input("Введите любую строку: "))
word = "Ночь"
final_word = "День"
final_list = []
words = string.split()
spin_words(words, final_list)
final_string = ' '.join(final_list)
print(final_string)


