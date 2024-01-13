from mastodon import Mastodon


class mastodon_connection(Mastodon):
    def __init__(self, access_token, api_base_url):
        super().__init__(access_token=access_token,api_base_url=api_base_url)

    def get_account_info(self,user_id):
        return dict(self.account_lookup(user_id))


    def get_all_followers(self,user_id):
        id_to_lookup=self.get_account_info(user_id=user_id)['id']
        return self.account_followers(id=id_to_lookup)


if __name__=='__main__':
    access_token='uxraM1MuKr1zkE-MpLL0aOY2ztWEX21LzGoQ5rEAysM'
    api_base_url='https://mastodon.social'

    con=mastodon_connection(access_token=access_token,api_base_url=api_base_url)

    #print(con.get_account_info('@jadi@persadon.com'))
    print(con.get_all_followers('@jadi@persadon.com'))