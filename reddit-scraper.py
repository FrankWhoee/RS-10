import praw
import json

reddit = praw.Reddit(client_id='***********',
                     client_secret='*****************',
                     user_agent='Python: I\'m a bot that generates rogersimon10 posts with ML! (by u/ClearMonocle)',
                     username='ClearMonocle',
                     password='************')

print(reddit.read_only)

rogersimon10 = reddit.redditor("rogersimon10")
data = {}
for comment in rogersimon10.comments.new(limit=None):
    data[comment.submission.title] = comment.body

data_json = json.dumps(data)
f = open("RS-10_data.json", "w+")
f.write(data_json)
f.close()