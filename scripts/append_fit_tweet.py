from dotenv import load_dotenv
import urllib.parse
import os
import tweepy
import json

load_dotenv()

# In your terminal please set your environment variables by running the following lines of code.
# export 'CONSUMER_KEY'='<your_consumer_key>'
# export 'CONSUMER_SECRET'='<your_consumer_secret>'

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth)

# Tweet / Update Status

# The app and the corresponding credentials must have the Write permission

# Check the App permissions section of the Settings tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps

# Make sure to reauthorize your app / regenerate your access token and secret 
# after setting the Write permission
def post_fit_to_twitter(fit_path, date_str, description="", last_tweet_id=None, fit_num=None, verbose=False) -> str:
    # TODO: this is sometimes wrong, should just derive the fit num from fits.json like below even if inefficient.
    if not last_tweet_id or not fit_num:
        with open('./local-data/last_fit.json', 'r') as f:
            last_fit_data = json.load(f)
            last_tweet_id = last_tweet_id or last_fit_data['last_tweet_id']
            fit_num = fit_num or int(last_fit_data['last_fit_num']) + 1

    if not fit_num:
        raise Exception("No fit number provided or found")
    if not last_tweet_id:
        raise Exception("No last tweet id provided or found")
        
    print("Using file path {}".format(fit_path))
    fit_pic = api.media_upload(fit_path)
    website_url = "https://spencerchang.me/fits/#{}".format(fit_num)
    tweet_body = f"fit {fit_num} ◉ {date_str or ''}\n\n{description or ''}\n\n{website_url}"
    if verbose:
        print("Preparing to post tweet in reply to {} with media id {}".format(last_tweet_id, fit_pic.media_id))
        print(tweet_body)
    new_status = api.update_status(tweet_body, in_reply_to_status_id=last_tweet_id, media_ids=[fit_pic.media_id])
    if not new_status:
        raise Exception("No status posted.")
    print("Successfully posted tweet {}".format(new_status.id))
    with open('./local-data/last_fit.json', 'w') as f:
        json.dump({
            'last_tweet_id': new_status.id,
            'last_fit_num': fit_num
        }, f)
    return new_status.id

# BACKFILL_TIMESTAMPS = [1645401907.684905,1645635768.386656, 1645722461.871779]
BACKFILL_TIMESTAMPS = []
def backfill_fits():
    with open('./data/fits.json', 'r') as f:
        fit_data = json.load(f)
        sorted_fits = sorted(fit_data['fits'] , key=lambda x: x['timestamp'])
        sorted_fits_ts = [fit['timestamp'] for fit in sorted_fits]
        fits_to_backfill = [fit for fit in sorted_fits if fit['timestamp'] in BACKFILL_TIMESTAMPS]
        last_tweet_id = SAVED_LAST_TWEET_ID

        for fit in fits_to_backfill:
            fit_num = sorted_fits_ts.index(fit['timestamp']) + 1
            local_file_src = urllib.parse.unquote_plus(fit['imgSrc']).replace("https://assets.spencerchang.me/fits-stream/", "/Users/spencerchang/Downloads/").replace(":", "_")
            last_tweet_id = post_fit_to_twitter(local_file_src, fit["date"], description=fit['description'], last_tweet_id=last_tweet_id, fit_num=fit_num)

if __name__ == "__main__":
    backfill_fits()
