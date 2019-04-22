#reddit_bot

import praw

# reddit api login
reddit = praw.Reddit(
    client_id='?',
    client_secret='?',
    username='reddit_username',
    password='reddit_password',
    user_agent='?'
)

#the list of subreddits the bot will hang out in
subreddits = reddit.multireddit(
'nba',
'AtlantaHawks',
'bostonceltics',
'GoNets',
'CharlotteHornets',
'chicagobulls',
'clevelandcavs',
'Mavericks',
'denvernuggets',
'DetroitPistons',
'warriors',
'rockets',
'pacers',
'LAClippers',
'lakers',
'memphisgrizzlies',
'heat',
'MkeBucks',
'timberwolves',
'NOLAPelicans',
'NYKnicks',
'Thunder',
'OrlandoMagic',
'sixers',
'suns',
'ripcity',
'kings',
'NBASpurs',
'torontoraptors',
'UtahJazz',
'washingtonwizards'
)

# phrase to wake up the bot
keyphrase = 'this is what the bot listens for in the comment section'

#look for phrase and reply with link to website
for comment in subreddits.stream.comments():
    try:
        if keyphrase in comment.body:
        word = comment.body.replace(keyphrase, '')
    except:
        print('to frequent')
