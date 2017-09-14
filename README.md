# Case Study: Fraud Detection


# Overview

In this project we wanted to create a model that would be able to determine if an event on a site was fraudulent and display that on a web application.  This was a two day case study where we would focus on EDA, feature engineering and modeling for the first day and on the second day would be creating a data product that would be able to take live data from a server and display our predictions on our website.


# EDA

We first started by loading our data into pandas so we could examine our features and try to examine, which ones might provide the most signal for fraud by examining those features and seeing which events were flagged as fraudulent.  Some of the first features we thought might provide the most signal for fraudulence included were how old the accounts when creating the events, whether or not the event had a venue name posted, and the type of payouts for the events.  We found that in many cases that were flagged as fraudulent had user accounts that were just recently created and we also noticed that events that did not have a venue name or location were also more likely to be fraudulent than events with older users or specified venues.  Some other factors we found that seemed as though they were correlated with more fraud were if the event had no type of payout or no previous payouts or if they only had a small number of payouts.  After more exploration of the data we also noticed that fraudulent events were often correlated with specific channels were as other channels had noticeably lower rates of fraud.


# Feature Engineering

To put these features into our model we had to revise them a little, so we used binary classifications for whether or not a user was new or not.  We considered new users to have an age of 0 and the rest as 1.  We used similar methodology on whether the event had a venue name listed, if the number of payouts were above a certain threshold, if they were in the groups of channels we considered as having a higher or lower correlation with fraud, if they had previous payments, as well as if the organization names were all in lower case.


# Modeling

After we had engineered our features, we made sure to train_test_split our data, so that we could correctly train our model and evaluate its performance. The first model we started using was a Logistic Regression model with a base of three features and then we kept adding features to our model.  After each step we only kept a new feature in our model if our F1 score increased by a noticeable amount.  We decided to use an F1 score as our assessment metric because it considers both precision and recall as opposed to just accuracy.  We decided Once we had 6 features we decided to test these in a Random Forest model and see if that would predict better.

When we first created our Random Forest model it already scored better than our Logistic Regression model without tuning.  We then used GridSearchCV to tune our model parameters, which actually came out to 10 trees and a max depth of 5.  We compared those to other models like xgboost and SVM, but those did not perform as well as our tuned Random Forest model.  We then looked at adding other features to our model to see if they would make a difference, but most did not add much to our F1 score, so we decided to leave most of them out.

We decided that our final metric for our model would return the percent chance that an event were fraudulent and flag them as either low risk, medium risk, or high risk.  We then looked implemented a cost matrix, which calculated the financial impact if an event was actually determined to be fraudulent with the main objective being to minimize the amount of money lost from fraudulent events or maximize the amount of money saved from correctly flagging fraudulent events.


# Web Application

The next step was to implement our model in a web application that would be able to receive live data from a server or source and predict the probability and risk that the new event is fraudulent.  We would also calculate the potential cost to our business is determined to be fraud.


# Future Steps

Edit our web application to be able to edit different thresholds for levels of risk as well as be able return summaries of the data that has been processed so far.


# Credits

Thank you to Elham Keshavarzian, Jay Zhou, Joseph Fang, and Shige Tajima.
