# Generating Custom Yelp Reviews
This project is my version of reproducing the work from an amazing recent research paper submitted August 27, 2017 by a team of reserachers from the University of Chicago:
["Automated Crowdturfing Attacks and Defenses in Online Review Systems"](https://arxiv.org/abs/1708.08151) by Yuanshun Yao, Bimal Viswanath, Jenna Cryan, Haitao Zheng, Ben Y. Zhao.

## What are the quick details of the paper?
In this paper the authors discuss the black market business of humans creating "fake" reviews on Amazon, Yelp, etc.  The researchers showed that they could use Deep Learning to create human quality restaurant reviews (both in terms of looking realistic as well as being rated as helpful), customize them, beat a standard baseline of fake review detection using regular Machine Learning methods, but also create a Recurrent Neural Network that could in fact detect these computer generated reviews with high accuracy. 

## What did I do and why?
When I read this paper my immediate reaction was not only being impressed by the power of generative RNN models when applied to a specific short domain (restuarant reviews), it was also excitement that I could use something like this and give my favorite coffee shops 5 stars without taxing my brain!

My biggest interest from the paper was in creating a model that could generate human-like positive reviews (using character-level Recurrent Neural Networks), and then secondly implementing a version of the algorithm that they proposed to customize those reviews towards any restaurant.  Given my interpretation of this model as a net-positive to consumers and businesses I also built a new feature not in the paper that allows people to personally customize their reviews by inputting foods/items that they enjoyed from the restaurant, and letting the program replace the generic created food words in the review with these words.

## How to use the program:
This project is based on the premise that it's much easier to edit then to create from scratch.  All reviews are trained on 5-star positive reviews, and thus generate positive sentiment.  Either generate random reviews, or custom ones based on instructions below.  The program will produce several so you can pick the one that seems most relevant, copy/paste, and modify it as you see fit.  Often with just a small tweak you can quickly produce a great review that both helps business owners and gives you good karma!

## TL;DR show me some reviews:
`random_reviews()`

"This place is amazing! The food is always amazing, especially the seared ahi tuna, salmon melts in your mouth. Great service. Prices are the same as what I had there."

"Thank you to! You have to try the Toro Flavor!"

"<SOR>I tried this place on here on a recent trip to Vegas. We ordered the spicy chicken lasagna and it was wonderful.  I recommend this place and go to their new dinner or life.<EOR>"

`user_custom('pizza,pasta,breadsticks,salad')`

Coming up with two ideas for you...

The salad pizza breadsticks was pretty good as well. Friendly service too. 

pasta breadsticks with a great atmosphere. The pasta and salad is really good and the pizza Comparable to the greatest ambiance and fun decor. 


## Quick Start

### Setup
This requires Python 3.5 ideally with anaconda
# clone repo
`git clone https://github.com/ajmanser/Yelp.git && cd Yelp`

#### download pretrained model that I trained on a GPU over 9+ days
`curl -O https://s3.amazonaws.com/yelp-weights-files/Sep-26-all-00-0.7280.hdf5`
#### install required libraries
`pip install -r requirements.txt`

### Use the Pre-trained Models:
1.  You should have downloaded the weights file with the curl command above, otherwise just click and download it, moving it to the cloned github repo.  

I'm also including a very different model if you want to try the experimental "many-to-many" version in jupyter.

OPTIONAL JUPYTER NOTEBOOK ONLY EXPERIMENTAL MODEL/ARCHITECTURE
(https://s3.amazonaws.com/yelp-weights-files/More-Dropout-all-Karpathy-00-0.6968.hdf5)


2.  You're ready to start producing reviews!  You can use the Write_Custom_Review Notebook and experiment, or use the write_review.py file and run things from the command line.  The only function that won't work is the df_custom(restaurant) unless you create your own dataframe of restuarant names with steps 1-3 from training from scratch notes OR create your own dataframe resulting in the same format. 

If you're using the command line:
* `python3`
* `from write_review import *`
* `random_reviews()`

OR 
`user_custom(foods)`
* if you use user_custom input a bunch of foods separated by string, ie; 'taco,burrito,tostada'


### Training from scratch:
(I'm including everything as python scripts that you can just run, but also jupyter notebooks for people who prefer that format)

1.  Download the Yelp academic dataset in JSON:
(https://www.yelp.com/dataset/challenge)

2.  Use the json_converter.py script on the business and review datasets to convert them into csv files.  This script requires Python version 2 and simple json (I took this from another repo and made a few quick attempts to get it working with Python 3, but it was becoming a bottleneck for me and it works fine if you use Python 2 + pip2 install simplejson).

3.  Clean the dataset.  Open the notebook Yelp_and_Business_Review_Data and run all of the cells.  Feel free to see what's going here.  This will create a new csv of just restaurant reviews, as well as a text file with all of the review data in txt form.

4.  Train the data by running the cells in Train_Char_RNN.  THIS TAKES A LONG TIME!  I wouldn't attempt this without a GPU.  With a standard GPU I was able to get through one epoch of the dataset in a little over 24 hours.  I ran mine in the cloud for days/week at a time.  You'll get some results after a few hours though.  Feel free to stop the training process, load your best weights files, and see what you can print out!  Also alternatively I recommend shrinking the dataset to 500k-1mm characters and training on that first to make sure it's working for you.

5.  Once you have some saved weights files you're ready to start producing reviews!  You can use the Write_Custom_Review Notebook and experiment, or use the write_review.py file and run things from the command line.  In either case you'll just need to modify the part in the Model section that says: model.load_weights("Sep-26-all-00-0.7359.hdf5") and change the "Sep-26-all-00-0.7359.hdf5" to whatever your weight file is called.

If you're using the command line:
*  `python3`
*  `from write_review import *`
*  `random_reviews()`  
OR 
* `user_custom(foods)` 
OR 
* `df_custom(restaurant)` 


### Some of the sources that were useful and I borrowed from liberally:
(http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
(https://github.com/mineshmathew/char_rnn_karpathy_keras)

(https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/)

(http://www.nltk.org/book/)

(https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py)
