string = str(input("Введите любую строку: "))

word = "Ночь"
final_string = "День"
words = string.split()

for i in range (len(words)):
    if len(words[i]) > 5:
        word = words[i]
        final_word = word[::-1]
        final_string.append(final_word)
    else:
        final_string.append(words[i])