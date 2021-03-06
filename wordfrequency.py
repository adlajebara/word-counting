def tokenize(lines):
    wordlist = []
    for line in lines:
        char = 0
        while char < len(line):
            #Skip whitespaces
            if line[char].isspace():
                pass

            #Check if char is a letter
            elif line[char].isalpha():
                end = char
                while line[end].isalpha():
                    end = end + 1
                    if end == len(line):
                        break

                wordlist.append(line[char:end].lower())
                char = end - 1

            #Check if char is a digit
            elif line[char].isdigit():
                end = char
                while line[end].isdigit():
                    if(end < len(line)):
                        end = end + 1

                wordlist.append(line[char:end].lower())
                char = end - 1

            else:
                wordlist.append(line[char])

            char = char + 1

    return wordlist


def countWords(words, stopWords):
    dictionary = dict()
    for word in words:
        if word not in stopWords:
            #ignore stopWords
            if word not in dictionary:
                dictionary[word] = 1
            else:  #if the word is already in the dictionary, increment by one
                dictionary[word] = int(dictionary.get(word))+1

    return dictionary

def printTopMost(frequencies, n):
    count = 0
    freq = 0
    sorted_freq = sorted(frequencies.items(), key=lambda tup: tup[1], reverse=True)

    for word,freq in sorted_freq:
        if count < int(n):
            print(word.ljust(20) + str(freq).rjust(5))
            count = count + 1
