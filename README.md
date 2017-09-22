# Generating Custom Yelp Reviews
This project is my attempt at reproducing some of the work from an amazing recent research paper submitted August 27, 2017 by a team of reserachers from UC Santa Barbara and the University of Chicago:
["Automated Crowdturfing Attacks and Defenses in Online Review Systems"](https://arxiv.org/abs/1708.08151)

## What are the quick details of this paper?
In this paper the authors discuss the black market business of humans creating "fake" reviews on Amazon, Yelp, etc.  The researchers showed that they could use Deep Learning to create human quality restaurant reviews (both in terms of looking realistic as well as being rated as helpful), customize them, beat a standard baseline of fake review detection using regular Machine Learning methods, but also create a Recurrent Neural Network that could in fact detect these computer generated reviews with high accuracy. 

## What did I do, and why?
When I read this paper my immediate reaction was not only being impressed by the power of generative RNN models when applied to a specific short domain (restuarant reviews), it was also excitement that I could use something like this and give my favorite coffee shops 5 stars without taxing my brain!


### Some of the sources that were useful and I borrowed from liberally:
(http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
(https://github.com/mineshmathew/char_rnn_karpathy_keras)

(https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/)

(http://www.nltk.org/book/)

(https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py)
