import tweepy
import credentials
from functions import *
from time import sleep
import os.path


LAST_UPDATE_FILE = 'last_update.txt'


def main():
    # if the last update file does not exist
    # Create the file, save the current timestamp
    # Else fetch the timestamp of the last post
    if not os.path.isfile(LAST_UPDATE_FILE):
        last_update = save_current_timestamp(LAST_UPDATE_FILE)
    else:
        last_update = fetch_last_timestamp(LAST_UPDATE_FILE)

    # if the connection fails to be established,
    # the application goes to sleep for 20 minutes.
    while True:
        api = log_on(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET,
        credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

        # if the connection is established
        while verify_credentials(api):
            now = get_current_timestamp()

            # if it's been less thaN 3600s (1hr) since last tweet
            if (now - last_update) >= 3600:
                tweet_picture(api, 'Yet another test :)', picture_pool='images')
                last_update = save_current_timestamp(LAST_UPDATE_FILE)

            go_to_sleep(1500)
        else: go_to_sleep(120)


if __name__ == "__main__":
    main()
