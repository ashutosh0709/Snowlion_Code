# Final output = Lematized list of words from article.

###########################################################################################################################################################
# IMPORTING AND DOWNLOADING THE NESSEARY LIBRARIES AT THE BEGINNING TO SAVE LOAD TIME OF MODEL LATER ON.

import nltk 
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer 
nltk.download('wordnet')
import pandas as pd

##################################################################################################################################################################
# TAKE IN A TEXT FILE AND CONVERTS IT TO A STRING AND RETURNS THE STRING.

def convertFileToVar(article_filename):

    file = open(article_filename, encoding='utf-8')                                                                    
    var = file.read()                                                                                  
    file.close()
    return var

##################################################################################################################################################################
# TAKES A STRING AND REPLACES A SPACE FOR ALL DIGITS AND SPECIAL-CHARS. LOWERS THE CASE OF ALL LETTERS, AND RETURNS THE STRING AND A COPY OF THAT STRING FOR SPACY LATER.

def removespecialcharsAndNumbers(var):                                              
    import re
    text = re.sub(r'[^a-zA-Z]',' ',var) 
    text = re.sub(r'\s+',' ',text)
    text = text.lower()
    text = re.sub(r'\d',' ',text)
    return text 

##################################################################################################################################################################
# TAKES IN A BIG-STRING AND TOKENIZES IT TO WORDS AND REMOVES THE STOPWORDS, AND RETURN THE FINAL LIST OF WORDS.

def tokenizeAndRemoveStopwordsAndSingleChar(text):               
    

    stop_words = stopwords.words('english') 
    stop_words.extend(['us','etc','god','jesus','lord','evil','devil','man','israel','people','king','son','men','house','day','children','land','things','hand','earth','sons','son','jerusalem','city','father','bible','tlb'])

    sentences = nltk.sent_tokenize(text) 
    sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

    for i in range(len(sentences)): 
        sentences[i] = [word for word in sentences[i] if word not in stop_words and len(word) > 1]

    filtered_sentence = sentences
    return filtered_sentence

#################################################################################################################################################################
# TAKES IN A LIST OF WORDS, LEMMATIZES IT ALL, AND RETURNS A LIST CONTAINING LEMMATIZED WORDS.

def lemmatize(filtered_sentence):

    lemmatizer = WordNetLemmatizer()

    lematized_list = []
    for word in filtered_sentence[0]:
        lematized_list.append(lemmatizer.lemmatize(word ,  pos="v"))
    lematized_list_short = list(set(lematized_list))
    lematized_list_short = lematized_list


    print(len(lematized_list))
    print(len(lematized_list_short))
    return lematized_list
