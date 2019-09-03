Title: Disentangling different types of learning
Date: 2018-09-16 17:50
Category: Research
Tags: Machine learning

If you're like me, you followed machine learning classes and got told that there are essentially three types of learning regimes in machine learning:

1. Supervised learning
2. Unsupervised learning
3. Reinforcement learning

And then, unless our experiences differ, you were told that you wouldn't be looking at reinforcement learning because it was too different. 

Fair enough! 

Then you were told that supervised learning is when each example is has a label. Unsupervised learning, on the other hand, is concerned with cases where your examples are not labeled. Different techniques and approaches will then be used based on whether or not labels are available. Got it.

And then, some day, you heard about something slightly different. "Semi-supervised learning", "self-supervised learning", "self-learning", "weakly supervised learning", "active learning", etc. Hmm, never heard of that. Aren't they all kind of the same thing?

I recently started looking at these other learning regimes/tasks a bit more and found some interesting differences. 
There are a few blog posts and Quora answers on this topic already: [great blog post on self-supervised learning](https://hackernoon.com/self-supervised-learning-gets-us-closer-to-autonomous-learning-be77e6c86b5a), [amazing blog post on semi-supervised learning and variants](http://ruder.io/semi-supervised/), [StackOverflow](https://stats.stackexchange.com/questions/125957/is-there-any-difference-between-distant-supervision-self-training-self-supervi), [another great (but shorter) blog post on this topic](https://towardsdatascience.com/the-blurry-lines-of-supervised-and-unsupervised-learning-b8a2aa04c8b0).

However, rather than give a theoretical explanation, or a high level overview, I thought it might be interesting to consider these different training regimes when applied to one of my questions of interest: brain decoding.

## What's brain decoding?

Brain decoding is the process of extracting information from functiona brain measurements such as fMRI, EEG, MEG, fNIRS, etc., as a way to understand what an individual is doing or thinking.

## We know this one (1): Supervised learning

Quick refresher: supervised learning is concerned with the following problem. Given X and Y, we want to predict the Y for new unseen examples.

This is by far the most frequent learning regime used in brain decoding. 
For example, in a brain-computer interface (BCI), we might be interested in knowing whether the user is thinking about moving their left or right hand (what we call Motor Imagery (MI)).
In a supervised learning regime, the training data contains many examples of each class (left and right).

## We know this one (2): Unsupervised learning

...

## Semi-supervised learning

...


## TODO

Maybe make a first part with supervised, unsupervised and semi-supervised only? Then a second part with the rest?

- Explain each regime simply, then mathematically (but still simply)
- Add an example to each regime, based on EEG
- Provide cool visualizations to help understand. Actually do it with real data from a public dataset?
    
>> Example: Pick a MI dataset. Show simple visualization of the data + explanation of the task.

**Supervised learning**: show simple example based on braindecode

**Unsupervised learning**: show clustering example on AE + t-SNE (also mention GANs)

**Semi-supervised**: show how re-using the representation learned with AE above and then training something on top (or fine-tuning) helps performance

**Self-supervised**: show a cool self-supervised task (wave2vec?), and compare the learned representation to above

**Self-learning**: show example, which graph that shows the process visually

**Weakly supervised learning**: ?

**Active learning**: ?



GOAL OF THE POST (for me):

* Show I know different types of learning
* Show my expertise in machine learning, EEG, visualization, coding
* Make use of pytorch, mne, etc. on Github
