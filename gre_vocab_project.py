import re, csv, pprint

file = open('/Users/pranavshridhar/Desktop/gre_vocab_new 2.txt','r',errors = 'replace')
dictionary = {}
key_words_list = []
key_meanings_list = []
key_eg_sentences_list = []
words_list = []
meanings_list = []
eg_sentences_list = []

# Regex to match word number and word itself (Eg. 1. , 2. , 250. , ... )

'''numRegex = re.compile(r'(\d)(\d*)?(\.)(\s*)?(\w*)') #Regex can be made better (later)

matched_strings_list = []
for groups in numRegex.findall(file.read()):
    item = ''.join(groups)
    clean_item = item.replace('\n','')
    matched_strings_list.append(clean_item)
print('Matched list is ',matched_strings_list[:30]) # Some problem here, makes everything else zero
print('Length of matched list is : ',len(matched_strings_list))'''

def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

def hasNumbersDot(inputString):
    return bool(re.search(r'^((\d)+?(\.))', inputString))
    

# Form a list of lines in the file
lines_list = file.readlines()
#print('Lines list is ',lines_list[:30])
clean_lines_list = []

for line in lines_list:
    clean_line = line.replace('\n','')
    clean_lines_list.append(clean_line)
for line in clean_lines_list:
    if line == '':
        del clean_lines_list[clean_lines_list.index(line)]
#print('Clean list is ',clean_lines_list[:20])


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
#matched_strings_list.pop()
'''print(len(matched_strings_list))
print(matched_strings_list[278])'''
'''print([x.split(".")[0] for x in matched_strings_list])'''
        
 

'''for i in range(len(clean_lines_list)):
    if i > 4400:
        print('Line number : ',i)
        print(clean_lines_list[i])'''




        
        
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
        '''print('line number : ',i)
        print('Words list is \n')
        print(words_list)
        print('\nMeanings list is \n')
        print(meanings_list)
        print('\Sentences list is \n')
        print(eg_sentences_list)
        print()'''
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








'''print(words_list[:15])
print(meanings_list[:15])
print(eg_sentences_list[:15])'''

#print('Length of values list is : ',len(key_words_list))
'''print('\nKey words list is : \n')
print(key_words_list)'''
'''print('\nKey meanings list is : \n')
print(key_meanings_list[280:])
print('\nKey examples list is : \n')'''
'''print(key_eg_sentences_list[275:])
print(len(key_eg_sentences_list))'''

'''print('\nLength of Key words list is : \n')
print(len(key_words_list))
print('\nLength of Key meanings list is : \n')
print(len(key_meanings_list))
print('\nLength of Key examples list is : \n')
print(len(key_eg_sentences_list))'''

# Take the line containing regex match and make it a key in the dictionary
    
'''For each key made, assign to it a list of value containing word, meaning and
   sentence after obtaining it from the subsequent lines'''

zipped_list = list(zip(key_words_list,key_meanings_list,key_eg_sentences_list))
#result = list(zipped_list)
#print('Zipped list is : ',zipped_list[:5])
refined_zipped_list = []

for tuples in zipped_list:
    litup = list(tuples)
    refined_zipped_list.append(litup)
#print('\nRefined Zipped list is ',refined_zipped_list[:2],'\n')

values_list = []
for lists in refined_zipped_list:
    values = list(zip(*lists))
    values_list.append(values)
'''print('\nValues list is : ',values_list[:3],'\n')
print('Length of values list is : ',len(values_list))'''
for i in range(278):
    dictionary[matched_strings_list[i]] = values_list[i]

'''print(dictionary['278. Unable to decide/ fickle'])
print(dictionary.keys())'''
'''print(dictionary.keys())'''
# print(dictionary.keys())


# Each key contains multiple words. Can be known (each word preceeds an '='sign)

    
file.close()

file2 = open('/Users/pranavshridhar/Desktop/refined_gre_text2.txt','w')
keys = pprint.pformat(dictionary.keys())
values = pprint.pformat(dictionary.values()) 
file2.write(keys)
file2.write(values)

'''with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dictionary.items():
       writer.writerow([key, value])'''

'''with open('mycsvfile.csv','w') as f:
    w = csv.writer(f)
    w.writerows(dictionary.items())'''

'''with open('mycsvfile.csv', 'w') as f:  
    w = csv.DictWriter(f, dictionary.keys())
    w.writerow(dict((fn,fn) for fn in dictionary.keys()))
    w.writerow(dictionary)'''


# #csv_columns = ['Topic', 'Word', 'Meaning', 'Sentence']
# with open('csv_file.csv', 'w') as csvfile:
#             writer = csv.DictWriter(csvfile, fieldnames = None)
#             writer.writeheader()
#             for data in dictionary:
#                 writer.writerow(data)

# keys = sorted(dictionary.keys())
# with open("test.csv", "w") as outfile:
#    writer = csv.writer(outfile, delimiter = "\t")
#    writer.writerow(keys)
#    writer.writerows(zip(*[dictionary[key] for key in keys]))

# COL_WIDTH = 6
# FMT = "%%-%ds" % COL_WIDTH

# keys = sorted(dict.keys())

# with open('out.csv', 'w') as csv:
#     # Write keys    
#     csv.write(''.join([FMT % k for k in keys]) + '\n')

#     # Assume all values of dict are equal
#     for i in range(len(dict[keys[0]])):
#         csv.write(''.join([FMT % dict[i][k] for k in keys]) + '\n')

# key_list = dictionary.keys()    
# limit = len(dictionary[key_list[0]])    

# for index in range(limit):    
#   writefile.writerow([dictionary[x][index] for x in key_list])

# key_list = []
# value_list = []
# with open('blah.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(Topic)
#     for i in range(len(dictionary[0])):
#         writer.writerow
# csv_file.close()        
# print ('saving is complete') 


with open('gre.csv', 'w') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(['TOPIC', 'WORD', 'MEANING', 'SENTENCE'])

    for Topic, Words in dictionary.items():
        for Word, Meaning, Sentence in Words:
            w.writerow([Topic, Word, Meaning, Sentence,])
            # w.writerow('\n')

            
f.close()



