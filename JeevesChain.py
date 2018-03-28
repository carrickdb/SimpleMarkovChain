import random
import sys

stopword = "\n"  # Since we split on whitespace, this can never be a word
stopsentence = (".", "!", "?",)  # Cause a "new sentence" if found at the end of a word
sentencesep = "\n"  # String used to seperate sentences
mr = ("Mr.", "Mrs.")

# GENERATE TABLE
w1 = stopword
w2 = stopword
table = {}

with open('WoosterCorpus', 'r') as f:
    for line in f:
        linelist = line.split()
        for i in range(len(linelist)):
            word = linelist[i]
            if word[-1] in stopsentence:
                table.setdefault((w1, w2), []).append(word[0:-1])
                w1, w2 = w2, word[0:-1]
                word = word[-1]
            if word[0].isupper() and word != mr:
                if i != len(linelist) - 1:
                    nextword = linelist[i+1]
                    table.setdefault((stopword, stopword), []).append(word)
                    table.setdefault((stopword, word), []).append(nextword)
            table.setdefault((w1, w2), []).append(word)
            w1, w2 = w2, word

# Mark the end of the file
table.setdefault((w1, w2), []).append(stopword)

# GENERATE SENTENCE OUTPUT
maxsentences = 5

w1 = stopword
w2 = stopword
sentencecount = 0
sentence = []


# ORIGINAL - DO NOT TOUCH
# while sentencecount < maxsentences:
#     newword = random.choice(table[(w1, w2)])
#     if newword == stopword: sys.exit()
#     if newword in stopsentence:
#         print("%s%s%s" % (" ".join(sentence), newword, sentencesep))
#         sentence = []
#         sentencecount += 1
#     else:
#         sentence.append(newword)
#     w1, w2 = w2, newword

# With all upper-case starters
while sentencecount < maxsentences:
    newword = random.choice(table[(w1, w2)])
    if newword == stopword: sys.exit()
    if newword in stopsentence:
        print("%s%s%s" % (" ".join(sentence), newword, sentencesep))
        sentence = []
        sentencecount += 1
    else:
        sentence.append(newword)
    w1, w2 = w2, newword


## User's choice
        # while 1:
#     newwords = []
#     newwords.append(random.choice(table[(w1, w2)]))
#     for i in range(len(newwords)):
#         print(i+1, word)
#
#     if newword == stopword: sys.exit()
#     if newword in stopsentence:
#         print("%s%s%s" % (" ".join(sentence), newword, sentencesep))
#         sentence = []
#         sentencecount += 1
#     else:
#         sentence.append(newword)
#     w1, w2 = w2, newword