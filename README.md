# mood_journal_plot
A project for my UCSD extension data analysis with Python class. It makes use of a couple of external resources/libraries to retrieve the most recent 40 pages of timeline information (bypassing retweets, mentions and image tweets) and analyze the sentiment values based on the wording used and plot out a graph of the person's sentiment against a period of time.

# External Libraries Used
Listed are some of the external libraries I used for this project.

### [Tweepy](https://www.tweepy.org/)
A wrapper to the Twitter API. Used in this project to retrieve the timeline of a user

### Panda
Used for the dataFrame for better organization of the twitter data

### Matplotlib
Used to plot the graph of sentiment against time

### [TextBlob](https://textblob.readthedocs.io/en/dev/)
A library that does sentiment analysis based on the wording someone used. According to their site it used NLP to achieve that.

### [Eel](https://github.com/ChrisKnott/Eel) (removed)
My original idea was to use Eel for the user interface but discarded the idea because plotting the graph with D3 or other frontend library kinda defeat the purpose since we are using matplotlib in this class.

# Quick Demo
When you start the application you will be prompted to enter the twitter handle of the person you want to analyze.

![User is prompted to enter user handle](https://github.com/yankwong/mood_journal_plot/blob/main/screenshots/prompt.png)

Then after giving it some time to process, a graph will be generated.

![Graph based on user sentiment](https://github.com/yankwong/mood_journal_plot/blob/main/screenshots/graph.png)

# Limitation and future improvement
Currently the application only retrieves 40 timeline posts from a user's twitter timeline. It then filters out retweets, mentions and images because retweets/mention is irrelevant for our usage and TextBlob is unable to analyze sentiment value based on images. Because of this limitation, this application will not work for users who tweet mostly images. A potential future enhancement will be to make the retrieval logic smarter to keep bypassing image tweets and stop only when it has retrieved a certain number of tweets.



