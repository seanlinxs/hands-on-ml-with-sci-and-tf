## 01. How would you define Machine Learning?

Machine Learning is defined as machine learns from experience E regards to task T, if performance measured as P, improve given E.

## 02. Can you name four types of problems where is shines?

- Spam filter
- Alpha Go
- Autonomous driving car
- Stock price prediction

## 03. What is a labled training set?

A training set with solutions labled by human beings a priori

## 04. What are the two most common supervised tasks?

- Spam filter
- Stock price prediction

## 05. Can you name four common unsupervised tasks?

- Find customer groups in a supermakert
- Find groups of genomes
- Words popularity analysis
- Anomorly detection: prevent credit card fraud

## 06. What type of Machine Learning alogrithm would you use to allow a robot to walk in various unknown terrains?

Reinforcement learning

## 07. What type of Machine Learning algorithm would you use to segment your customers into multiple groups?

K-NN Clusting

## 08. Would you frame the problem of spam detection as a supervised learning problem or an unsupervised learning problem?

Supervised

## 09. What is a online learning system?

A system that learns from streamlized new data flow and learns from one or a small batch of instances at a time, updates the model and discards the instances.

## 10. What is out-of-core learning?

Rather than learning on a production system, out-of-core learning happens every 24 hours or even weekly when more data is collected and learning from them all in separate process.

## 11. What type of learning algorithm relies on a similarity measure to make predictions?

K Nearest Neiboughers

## 12. What is the difference between a model parameter and a learning algorithm's hyperparameter?

Model parameter is parameter about features and used to predict; hyperparameter is parameter about learning and used to fine tune model, it will not been used to predict after trained.

## 13. What do model-based learning algorithms search for? What is the most common strategy they use to succeed? How do they make predictions?

Model-based algorithms search for paramters which fit training data set. The most common strategy is find out the parameters which minimize the cost function. They use trained model parameters to predict.

## 14. Can you name four of the main challenges in Machine Learning?

- Over fitting
- Under fitting
- Hard or expensive to collect representative data
- Expensive to train complex models

## 15. If your model performs great on the training data but generalizes poorly to new instances, what is happening? Can you name three possible solutions?

Overfitting is happening, solutions are:

- Reduce features or dimensionality reduction
- Regularization of parameters
- Collect more data
- Change to simpler model

## 16. What is a test set and why would you want to use it?

A test set is a separate data set which is not used in trainging but used in measurement of model, I would use test set to measure generalizing errors.

## 17. What is the purpose of a validation set?

Validation set is to avoid test sets polluting traing process when fine tune training hyperparameters. And leave test set as final measurement of generalizing errors.

## 18. What can go wrong if you tune hyperparameters using the test set?

It will lead to a well fitted model for both training set and test set, but might generalize bad. Because test set are used as sort of "training data".

## 19. What is cross-validation and why would you prefer it to a validation set?

Cross-validation is a way that splits training set into sumplmentrary sets and use different combinations to traing the model using training set and validation set to find best hyperparameters.