import math
import os

# define a function that will loop through a list of words counting the occurence of 
# these words if they appear in the specified iput files

def conjunctions(textFile1,textFile2):
    # create two empty dictionaries
    conj1 = {}
    conj2 = {}

    # create a list that holds the words to be counted
    wordList = ['also', 'although', 'and', 'as', 'because', 'before', 'but', 'for',
     'if', 'nor', 'of', 'or', 'since', 'that', 'though', 'until', 'when', 'whenever',
     'whereas', 'which', 'while', 'yet']

    # set the counts to 0
    for word in wordList:
        conj1[word] = 0
        conj2[word] = 0
    
    # create two nested for loops to iterarte through both input files and wordList. must also
    # count the occurences of the specified words
    for word in wordList:
        for text in textFile1:
            if word == text.lower():
                conj1[word] += 1

    for word in wordList:
        for text in textFile2:
            if word == text.lower():
                conj2[word] += 1
    
    return conj1, conj2

# define a function that counts the occurence of each word in the files
def unigrams(textFile1, textFile2):
    # create two empty dictionaries
    unigram1 = {}
    unigram2 = {}

    # i have used sets to extract the words from the input files
    set1 = set(textFile1)
    set2 = set(textFile2)

    # I will know convert the sets to lists
    list1 = list(set1)
    list2 = list(set2)

    for i in textFile1:
        unigram1[i] = unigram1.get(i,0) + 1
    
    for w in textFile2:
        unigram2[w] = unigram2.get(w,0) + 1
    
    return unigram1, unigram2
    
# define a function that counts instances of punctuation symbols in the input files
def punctuation(textFile1,textFile2):
    # create two empty dictionaries
    punct1 = {}
    punct2 = {}

    # create a list containing the punctuation symbols
    puncList = [',', ';', '\'', '-']

    # set the counts to zero
    for punc in puncList:
        punct1[punc] = 0
    for punc in puncList:
        punct2[punc] = 0
    
    # use nested loops again but this time to count occurences of punctuation in the input text
    for punc in puncList:
        for text in textFile1:
            if punc in text:
                punct1[punc] += 1 
    
    for punc in puncList:
        for text in textFile2:
            if punc in text:
                punct2[punc] += 1

    return punct1, punct2

# define a function called composite. composite returns the output of punctuation() and conjunction().
# this function also needs to compute the average number of words per sentence and the average number of 
# sentences per paragraph

def composite(textFile1, textFile2, d1, d2):
    puncList = [',', ';', '\'', '-']
    
    wordList = ['also', 'although', 'and', 'as', 'because', 'before', 'but', 'for',
     'if', 'nor', 'of', 'or', 'since', 'that', 'though', 'until', 'when', 'whenever',
     'whereas', 'which', 'while', 'yet']

    composite1 = {}
    composite2 = {}

    # deal with punctuation first
    # set the counts to zero
    for punc in puncList:
        composite1[punc] = 0
    for punc in puncList:
        composite2[punc] = 0

    for punc in puncList:
        for text in textFile1:
            if punc in text:
                composite1[punc] += 1
    
    for punc in puncList:
        for text in textFile2:
            if punc in text:
                composite2[punc] += 1
    
    # deal with conjunctions
    # set the counts to zero
    for word in wordList:
        composite1[word] = 0
        composite2[word] = 0

    for word in wordList:
        for text in textFile1:
            if word == text.lower():
                composite1[word] += 1

    for word in wordList:
        for text in textFile2:
            if word == text.lower():
                composite2[word] += 1

    # now have to calculate the ave. number of words per sentence and the ave. number of 
    # sentences per paragraph.
    # firstly start with average words per sentence
    
    sentence1 = d1.split(".")
    sentence2 = d2.split(".")
    
    aveWords1 = len(sentence1) / len(d1)
    aveWords2 = len(sentence2) / len(d2)

    composite1['ave. words per sentence'] = aveWords1
    composite2['ave. words per sentence'] = aveWords2

    # calculate ave. number of sentences per paragraph
    paragraph1 = d1.split('\n\n')
    paragraph2 = d2.split('\n\n')

    sentencesPara1 = len(sentence1) / len(paragraph1)
    sentencesPara2 = len(sentence2) / len(paragraph2)

    composite1['ave. sentences per paragraph'] = sentencesPara1
    composite2['ave. sentences per paragraph'] = sentencesPara2

    return composite1, composite2

def main(inputFile1, inputFile2, feature):
    if os.path.isfile(inputFile1):
        with open(inputFile1, 'r') as file:
            d1 = file.read().replace('\n', '')
            textFile1 = d1.split(" ")
    else:
        print('Incorrect file has been entered for file one')
        return
        
    if os.path.isfile(inputFile2):
        with open(inputFile2, 'r') as file:
            d2 = file.read().replace('\n', '')
            textFile2 = d2.split(" ")
    else:
        print('Incorrect file has been entered for file two')
        return

    if feature == 'conjunctions':
        output = conjunctions(textFile1, textFile2)   
        
    elif feature == 'unigrams':
        output = unigrams(textFile1, textFile2)

    elif feature == 'punctuation':
        output = punctuation(textFile1, textFile2)
        
    elif feature == 'composite':
        output = composite(textFile1, textFile2, d1, d2)
        
    else:
        print("An incorrect feature has been defined. Please start again.")
        return

    profile1 = output[0]
    profile2 = output[1]

    value = 0

    for i in profile1:
        if i in profile1 and i in profile2:
            value = value + (profile1[i] - profile2[i]) ** 2
        
    distance = math.sqrt(value)

    print("\nThe distance between the profiles is {0:0.2f}".format(distance))
    print()
    print('Profile 1: {}'.format(profile1))
    print()
    print('Profile 2: {}'.format(profile2))

if __name__ == '__main__':
    main(inputFile1,inputFile2,feature)