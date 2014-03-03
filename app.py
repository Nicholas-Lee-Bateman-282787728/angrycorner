import os
from angrycorner import app
import pymongo
from urlparse import urlparse

## dotenv
lines = [line.strip() for line in open('.env')]
for line in lines:
  split_line  = line.split("=")
  key         = split_line[0]
  value       = split_line[1]
  os.environ[key] = value

print "========= SANITY CHECK .env"
print os.environ.get('TWITTER_API_KEY')
print os.environ.get('TWITTER_API_SECRET')
print os.environ.get('MONGOHQ_URL')

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=True)
