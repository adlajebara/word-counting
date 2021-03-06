import wordfrequency
import sys
import urllib.request

def main():
    stopWords = sys.argv[1]
    lines = sys.argv[2]
    n = sys.argv[3]

    if lines.startswith('http://') or lines.startswith('https://'):
        response = urllib.request.urlopen(lines)
        lines = response.read().decode("utf-8").splitlines()
        print(lines)

    else:
        inp_file = open(lines)
        lines = inp_file.readlines()
        inp_file.close()

    for line in lines:
        wordlist = wordfrequency.tokenize(lines)

    inp_file = open(stopWords)
    stopWords = [word.strip('\n') for word in inp_file.readlines()]
    inp_file.close()

    frequencies = wordfrequency.countWords(wordlist, stopWords)
    wordfrequency.printTopMost(frequencies, n)


main()
