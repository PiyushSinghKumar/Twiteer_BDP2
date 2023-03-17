#importing required libraries

import tweepy
import json
import time
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Get the Bearer token value from the environment variable
bearer_token = os.getenv('BEARER_TOKEN')

# Authenticate with Twitter API using API keys, API secret key, and Bearer token
auth = tweepy.OAuth2BearerHandler(bearer_token)
api = tweepy.API(auth)

# Define the search query
query = 'Covid-19'

# Define the fields to include in the response
fields = ['created_at', 'id', 'full_text', 'user']

# Extract data using search API
tweets = []
start_time = time.time()
seconds = 1
while True:
    elapsed_time = time.time() - start_time
    if elapsed_time >= seconds:
        break
    try:
        for status in tweepy.Cursor(api.search_tweets,
                                    q=query + ' -filter:retweets',  # exclude retweets
                                    tweet_mode='extended',
                                    lang='en',
                                    result_type='recent',
                                    count=100).items():
             # Create a new dictionary with only the desired fields
            tweet_data = {field: status._json[field] for field in fields}
            tweets.append(tweet_data)
            #print(elapsed_time)
            #time.sleep(60) # Wait for 60 seconds and try again

            # Check if elapsed time exceeds specified time
            if time.time() - start_time >= seconds:
                break
                        
    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(60) # Wait for 60 seconds and try again

# Save the extracted data as JSON
# if os.path.isfile('raw_tweets.json'):
#     # If the file exists, open it in append mode
#     with open('raw_tweets.json', 'a') as f:
#     # Iterate through the list of tweets and write each tweet as a separate JSON object
#         for tweet in tweets:
#             json.dump(tweet, f)
#             f.write('\n')
# else:
#     # If the file doesn't exist, create a new file and write to it
#     with open('raw_tweets.json', 'w') as f:
#     # Iterate through the list of tweets and write each tweet as a separate JSON object
#         for tweet in tweets:
#             json.dump(tweet, f)
#             f.write('\n')


# # Print confirmation message
# print(f"Saved {len(tweets)} tweets to raw_tweets.json")

# Save the extracted data as JSON
script_dir = os.path.dirname(os.path.abspath(__file__))
script_dir = script_dir.replace('utilities', 'data') # get the directory of the script that is currently running
#print(script_dir)
json_path = os.path.join(script_dir, 'raw_tweets.json') # create a path to save the JSON file 
#print(json_path)

if os.path.isfile(json_path):
# If the file exists, open it in append mode
    with open(json_path, 'a') as f:
# Iterate through the list of tweets and write each tweet as a separate JSON object
        for tweet in tweets:
            json.dump(tweet, f)
            f.write('\n')
else:
    # If the file doesn't exist, create a new file and write to it
    with open(json_path, 'w') as f:
        # Iterate through the list of tweets and write each tweet as a separate JSON object
        for tweet in tweets:
            json.dump(tweet, f)
            f.write('\n')# Print confirmation message
print(f"Saved {len(tweets)} tweets to {json_path}")