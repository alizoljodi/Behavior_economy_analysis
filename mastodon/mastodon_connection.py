import sys
#print(sys.path)

from mastodon import Mastodon
from mastodon_users import MastodonUsers


class mastodon_connection(Mastodon):
    def __init__(self, access_token, api_base_url):
        super().__init__(access_token=access_token,api_base_url=api_base_url)

    def get_account_info(self,user_id):
        return dict(self.account_lookup(user_id))


    def get_all_followers(self,user_id):
        user_to_lookup=self.get_account_info(user_id=user_id)
        id_to_lookup=user_to_lookup['id']
        limit=user_to_lookup['followers_count']
        raw_data=self.account_followers(id=id_to_lookup,limit=limit)
        followers=[]
        for follower in raw_data:
            follower_instance=MastodonUsers()
            follower_instance.set_attribute(user_id=follower['id'],user_name=follower['username'],acct=follower['acct'],
            bot=follower['bot'],group=follower['bot'],create_datetime=follower['created_at'],url=follower['url'],uri=follower['uri'],
            followers_count=follower['followers_count'],following_count=follower['following_count'],status_count=follower['statuses_count'],last_status=follower['last_status_at'])
            followers.append(follower_instance)
        return followers


if __name__=='__main__':
    access_token='uxraM1MuKr1zkE-MpLL0aOY2ztWEX21LzGoQ5rEAysM'
    api_base_url='https://mastodon.social'

    con=mastodon_connection(access_token=access_token,api_base_url=api_base_url)

    #print(con.get_account_info('@jadi@persadon.com'))
    followers=con.get_all_followers('@jadi@persadon.com')
    for follower in followers:
        print(vars(follower))