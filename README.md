# mood_journal_plot
A project for my UCSD extension data analysis with Python class. It made use of a couple of external resources/library to retreive the most recent 40 pages of tweets and analyze the sentiment values based on the wording used and plot out a graph of the person's sentiment.

# external library used
Below are some of the external library I used for this project.

### [Tweepy](https://www.tweepy.org/)
A wrapper to the Twitter API. Used in this project to retrieve the timeline of a user

### Panda
Used for the dataFrame for better organization of the twitter data

### Matplotlib
Used to plot the graph of sentiment against time

### [TextBlob](https://textblob.readthedocs.io/en/dev/)
A library that does sentiment analytising based on the wording someone used. According to their site it used NLP to achieve that. 

### [Eel](https://github.com/ChrisKnott/Eel) (removed)
My original idea was to use Eel for the user interface but discarded the idea because plotting the graph with D3 or other frontend library kinda defeat the purpose since we are using matplotlib in this class.



