The Twitter Bot retweets the latest tweets to a Twitter query. It is recommended to set up a cronjob that is triggered every 5 minutes. The bot will then try to retweet the latest 10 tweets to the query every 5 minutes (this is configurable).

Die Konfiguration sehen sie hier.

```
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
QUERY = '#youtube OR #youtuber exclude:retweets'
TWEETS_LANGUAGE = 'de'
TWEETS_PER_QUERY = 10
SLEEPING_TIME = 3
```

### Linux Installation

- Requires python 3 and pip

**Create your developer account and get twitter keys**

You must have a developer account on Twitter. You also need to create an APP to generate the required authentication keys.

**Configure your bot in the environment file**

The keys and the general configuration of the bot is done in the environment file (.env.example). This file must be renamed to .env.

**Install all modules with pip**

```
pip install -r requirements.txt
```

### Example Cronjob 
Triggers every 5 Minutes the retwet bot.

```
* /5 * * * root python3.5 ~/retweet.py
```