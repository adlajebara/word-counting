# Word-Counting
I wrote this code while taking a summer course at Chalmers university.

This was the first lab, and we worked with a technique that is the found in many algorithms which allow machines to understand human language. Machines collect statistics which allow them to make inferences which are right most of the time, even when the machine lacks real understanding. The most basic statistics is plain word counting.


## How to run it
The program can count words from a text file or fetch data directly from the web. The data to be analysed needs to be specified in the third argument.

How to run it:
```bash
python3 topmost.py eng_stopwords.txt <text to analyze> n
```

Example:
```bash
python3 topmost.py eng_stopwords.txt examples/article1.txt 20
```

eng_stopwords.txt contains a list of stop words, and <text to analyze> should contain files to be analyzed. The last parameter n is the number of words to be printed.

## Files
* The examples folder contains examples of text files to be analyzed.
* eng_stopwords.txt contains a list of English stop words
* topmost.py contains the main function
* wordfrequency.py contains the tokenize, counting words and printing functions.
