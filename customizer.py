import nltk
from nltk.corpus import wordnet as wn
import random
import re

def review_to_nouns(review):
    is_noun = lambda pos: pos[:2] == 'NN'
    token=nltk.word_tokenize(review)
    nouns=[word for (word, pos) in nltk.pos_tag(token) if is_noun(pos)]
    return nouns

def food_related(nouns):
    #this takes in a list of wordnet nouns, and returns the list that are
    #>.20 based on WUP lexical related in Wordnet.  This can be tweaked

    food=wn.synset('food.n.01')
    final_list=[]
    for word in nouns:
        temp=word
        word=word+'.n.01'
        try:
            if food.wup_similarity(wn.synset(word))>0.20 and temp!='food':
                final_list.append(temp)
        except:
            pass

    return final_list

def clean_up(generic_review, real_review):
    #take generic review, and replace with real reviews food nouns
    generic_nouns=review_to_nouns(generic_review)
    real_nouns=review_to_nouns(real_review)

    food_generic=food_related(generic_nouns)
    food_real=food_related(real_nouns)

    final=[]
    for word in re.findall(r"[\w']+|[.,!?;]", generic_review):
        if word in food_generic and len(food_real)>1:
            word=random.choice(food_real)
            final.append(word)
        else:
            final.append(word)

    new_review=" ".join(final)
    return re.sub(r'\s+([?.!",])', r'\1', new_review)

def personalized_clean_up(review,user_items):
    #take generic review, and replace with user generated words
    generic_nouns=review_to_nouns(review)
    food_generic=food_related(generic_nouns)

    user_picked_items=user_items.split(",")

    final=[]
    for word in re.findall(r"[\w']+|[.,!?;]", review):
        if word in food_generic and len(user_picked_items)>1:
            word=random.choice(user_picked_items)
            final.append(word)
        else:
            final.append(word)

    new_review=" ".join(final)
    return re.sub(r'\s+([?.!",])', r'\1', new_review)

def pull_restaurant_review(restaurant_name, df):
    #pulls and combines all real restaurant reviews from a dataframe
    #restaurant_name is a string
    target_restaurant=df[df['name']==restaurant_name]
    combined_reviews=' '.join(target_restaurant['text'])

    return combined_reviews
