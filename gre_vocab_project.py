import re, csv

file = open('/Users/pranavshridhar/Desktop/gre_vocab_new 2.txt','r',errors = 'replace')

dictionary = {}
key_words_list = []
key_meanings_list = []
key_eg_sentences_list = []
words_list = []
meanings_list = []
eg_sentences_list = []

# Regex to match word number and word itself (Eg. 1. Angry)

numRegex = re.compile(r'(\d)(\d*)?(\.)(\s*)?(\w*)')

matched_strings_list = []
for groups in numRegex.findall(file.read()):
    item = ''.join(groups)
    clean_item = item.replace('\n','')
    matched_strings_list.append(clean_item)


def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

def hasNumbersDot(inputString):
    return bool(re.search(r'^((\d)+?(\.))', inputString))
    

# Form a list of lines in the file

lines_list = file.readlines()

clean_lines_list = []

for line in lines_list:
    clean_line = line.replace('\n','')
    clean_lines_list.append(clean_line)
for line in clean_lines_list:
    if line == '':
        del clean_lines_list[clean_lines_list.index(line)]


matched_strings_list = []

for i,line in enumerate(clean_lines_list):
    if hasNumbersDot(line) == True:
        string = line
        index = string.index('.')
        if len(string[index+1:]) == 0:
            string = line + ' ' + clean_lines_list[i+1]
            matched_strings_list.append(string)
        else:
            matched_strings_list.append(line)
        
        
for i,line in enumerate(clean_lines_list):
        
    if '=' in line:           # Words and Meanings Extraction Part
        string = line
        index = string.index('=')
        word = string[:index]
        meaning = string[index+1:]
        words_list.append(word)
        meanings_list.append(meaning)
        
    elif ':' in line:         # Examples Extraction Part 
        string = line
        index = string.index(':')
        
        if i < 4428:
            if '=' not in clean_lines_list[i+1] and hasNumbersDot(clean_lines_list[i+1]) == False:
                example = string[index+1:] + clean_lines_list[i+1]
                eg_sentences_list.append(example)
        
            else:
                example = string[index+1:]
                eg_sentences_list.append(example)
        if i == 4428:
            example = string[index+1:]
            eg_sentences_list.append(example)

    elif hasNumbersDot(line) == True:
        if i == 0:
            continue
        key_words_list.append(words_list)
        key_meanings_list.append(meanings_list)
        key_eg_sentences_list.append(eg_sentences_list)
        words_list = []
        meanings_list = []
        eg_sentences_list = []


zipped_list = list(zip(key_words_list,key_meanings_list,key_eg_sentences_list))

refined_zipped_list = []

for tuples in zipped_list:
    litup = list(tuples)
    refined_zipped_list.append(litup)

values_list = []
for lists in refined_zipped_list:
    values = list(zip(*lists))
    values_list.append(values)

for i in range(278):
    dictionary[matched_strings_list[i]] = values_list[i]
   
file.close()


with open('gre.csv', 'w') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(['TOPIC', 'WORD', 'MEANING', 'SENTENCE'])

    for Topic, Words in dictionary.items():
        for Word, Meaning, Sentence in Words:
            w.writerow([Topic, Word, Meaning, Sentence,])
            # w.writerow('\n')
         
f.close()



