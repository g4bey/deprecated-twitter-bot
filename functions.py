import tweepy
from datetime import datetime
from time import sleep
import os
import random

def log_on(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    """
    Establish the connection to the twitter API.

    Parameters:
     CONSUMER_KEY (str)
     CONSUMER_SECRET (str)
     ACCESS_TOKEN (str)
     ACCESS_TOKEN_SECRET (str)

    Returns:
    (object): return a tweepy.API object
    """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

def verify_credentials(api):
    """
    Verify the state of the connection to the twitter API.

    Parameters:
     api (ojbect): tweepy.api object

    Returns:
     (bool):
     if authentication was successful:
         True
     if authentication fails:
         False
    """
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
        return False

    return True

def tweet_picture(api, tweet, image_bank='images'):
    """
    Tweet a picture from a picture pool.

    Parameters:
     api (object): tweepy.API object
     tweet (str): the actual tweet. ie: "Hourly Fox Presents"
     picture_pool (str): the folder containing images
      optionial / default value > 'images'


    Returns:
     none
    """
    random_picture = pick_random_pic(image_bank)
    media = api.media_upload(random_picture)
    tweet = tweet
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])

    print('We successfully tweeted')


def get_current_timestamp():
    """
    Give the timestamp at the moment of the call

    Parameters:
     none

    Returns:
     (int): return timestamp at the moment of the call
    """
    current_timestamp = datetime.now()
    current_timestamp = datetime.timestamp(current_timestamp)

    return int(current_timestamp)

def fetch_last_timestamp(filename):
    """
    Read the last timestamp saved from a file.

    Parameters:
     filename (str): the filename with its extension

    Returns:
     (int): return the last saved timestamp
    """
    with open(filename, 'r') as file:
        last_timestamp = file.read()

    return int(last_timestamp)

def save_current_timestamp(filename):
    """
    Save the last timestamp in a file

    Parameters:
     filename (str): the filename with its extension

    Returns:
     (int): return the saved timestamp
    """
    current_timestamp = get_current_timestamp()

    with open(filename, 'w') as file:
        file.write( str(current_timestamp) )

    return int(current_timestamp)


def pick_random_pic(folder_name):
    """
    Pick a random picture contained in a folder

    Parameters:
     folder_name (str): the folder where the pictures are

    Returns:
     (str): return the path of the picture
    """

    path = os.getcwd() + '/' + folder_name
    files = os.listdir(path)
    picture = random.choice(files)

    return path + '/' + picture

def go_to_sleep(time):
    """
    Put the program to sleep for a given time,
    and print a message announcing it.

    Parameters:
     time (int): the time the program should sleep for, in seconds

    Returns:
     none
    """
    minutes = int(time / 60)
    print(f'The application is going to sleep for about {minutes} minutes.')
    sleep(time)


if __name__ == "__main__":
    pass
