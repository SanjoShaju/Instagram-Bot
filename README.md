# Instagram Bot #

## Table of Contents ##

- [Introduction](#introduction)
- [How to run the bot](#how-to-run-the-bot)
- [Process flow of the bot](#process-flow-of-the-bot)
- [Technologies Used](#technologies-used)
 
## Introduction ##
What a bot does is interact with other people’s Instagram accounts so you don’t have to do it manually.  
If programmed correctly on an Instagram account with differentiated awesome content, a bot is like rocket-fuel! 
It will multiply your rate of growth because it’ll allow your already-great account to be discovered many more people that you could have never reached if you were doing all of the interactions manually.  
On the other hand, an incorrectly programmed bot on an account that doesn’t have delightful content will likely ensure that your Instagram appears spammy because many more people will receive an irrelevant interaction from an account they dislike (yours). 
It’s a terrible first impression, and worse of all, it’ll be a big waste of your time, energy and money because it simply won’t generate any substantial growth.  
That is why each bot should be different and should be catered to ones needs only.  

## How to run the bot ##
- Collect a set of post descriptions and comments for the bot to learn. Customise the dataset to your preference. You can also use the sample dataset which is present in the 'dataset' folder
- Run the 'trainer.py' and train the chat bot. It creates a sqlite db.
- Finally run 'main.py' to run the bot  

## Process flow of the bot ##
- Take a hastag from a predefined list of niche related tags and make a search on that hastag.
- It collects all the links of the post listed in the search
- It opens each links one after the other
- The bot COMMENTS on the post according to the context of the post description using machine learning from a trained set of data
- It opens the user profile of the post and LIKEs the first three posts of the person.
- At last the bot follows the person. and repeats the entire process  

> Note -> This kind of process flow makes the working of bot looks like someone who got interested in that users profile and followed him, which in turn makes him to check out our user profile.
- - - - 
## Technologies Used ##
- __Selenium__ browser automation
- Chat bot for commenting using __Machine Learning__


