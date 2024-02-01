from sklearn.feature_extraction.text import TfidfVectorizer
import string
import warnings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True)
import random

import time

time_start = time.perf_counter()

file = input("Enter the file name without extensions: ")

f=open(f'{file}.txt','r',errors = 'ignore')
unf=f.read() #unfilitered
unf = unf.lower() #converts to lowercase
sent_tokens = nltk.sent_tokenize(unf) #converts to list of sentences
word_tokens = nltk.word_tokenize(unf) #converts to list of words

lemmer = nltk.stem.WordNetLemmatizer() #english dictionary in NLTK

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

greet_ing = ("hello", "hi", "greetings", "sup", "what’s up", "hey", "yo")
greet_out = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greet_ing:
            return random.choice(greet_out)

def response(user_response):
    spar_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        spar_response = spar_response + "I don’t understand you"
        return spar_response
    else:
        spar_response = spar_response + sent_tokens[idx]
        return spar_response

bot_name = "Pican"
flag = True
print(f"{bot_name}: My name is {bot_name}. I will answer your queries about {file}. If you want to exit, type Bye!")

while flag == True:
    user_response = input("User: ")
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response == 'thanks' or user_response == 'thank you':
            flag = False
            print(f"{bot_name}: You are welcome.")
        else:
            if greeting(user_response) != None:
                print(f"{bot_name}: " + greeting(user_response))
            else:
                print(f"{bot_name}: ", end="")
                print(response(user_response))
            sent_tokens.remove(user_response)
    else:
        flag = False

time_end = time.perf_counter()
print("Time elapsed: ", time_end - time_start)
