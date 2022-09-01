# word-counting
I wrote this code as part of an assingemnt while taking a summer course in Python at Chalmers university.

This assignment focuses on a technique which can be found in many algorithms that allow machines to understand human language. The code includes tokenization, how to split a running text into a sequence of words (tokens), word counting and aggregate statistics for the frequencies of different words.


## How to run it
The program can count words from a text file or fetch data directly from the web (needs to have a .txt extension). The data to be analysed needs to be specified in the third argument.

How to run it:
```bash
$ python3 topmost.py eng_stopwords.txt <text file or URL to analyze> n
```

Example:
```bash
$ python3 topmost.py eng_stopwords.txt examples/article1.txt 20
```

The last parameter n is the number of words to be printed.

## Files
* The examples folder contains examples of text files to be analysed
* eng_stopwords.txt contains a list of English stop words (words to be skipped)
* topmost.py contains the main function
* wordfrequency.py contains tokenize, word count and print functions

## TO-DO
Make it faster for analysing larger files. 
