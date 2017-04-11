import twitter
import json
import auth
import time
class updater(object):
    count = 0
    def f1(self):
        api = twitter.Api(auth.consumer_key,auth.consumer_secret,
                              auth.access_token,
                              auth.access_token_secret)
        while True:
            data= api.GetStatus(status_id="849813577770778624", trim_user=False, include_my_retweet=False, include_entities=False, include_ext_alt_text=False)
            updater.count = data.retweet_count
            time.sleep(1)
