import sys 
sys.path.append('users/')
from users import user
class MastodonUsers(user):
    def __init__(self):
        super().__init__()

    def set_attribute(self, user_id, user_name, acct, bot, group, create_datetime, url, uri, followers_count, following_count, status_count, last_status):
        self._user_id = user_id
        self._user_name = user_name
        self._acct = acct
        self._bot = bot
        self._group = group
        self._create_datetime = create_datetime
        self._url = url
        self._uri = uri
        self._followers_count = followers_count
        self._following_count = following_count
        self._status_count = status_count
        self._last_status = last_status

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    # Repeat the above pattern for each attribute
    # Example for user_name:
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    # Continue with acct, bot, group, create_datetime, url, uri, followers_count, following_count, status_count, last_status

    # Example for bot (assuming it's a boolean value):
    @property
    def bot(self):
        return self._bot

    @bot.setter
    def bot(self, value):
        if not isinstance(value, bool):
            raise ValueError("bot must be a boolean")
        self._bot = value

    # Continue with the rest of the properties

    def update_followers(self):
        pass

    def update_followings(self):
        pass

    def get_status(self):
        pass

    def get_feeling(self):
        pass

    def to_tuple(self):
        return (self.user_id, self.user_name, self._acct, self.bot,
        self._group, self._create_datetime,self._url, self._uri, self._followers_count, self._following_count, self._status_count, self._last_status)

    def from_tuple(self, data_tuple):
        (self.user_id, self.user_name, self._acct, self.bot,
         self._group, self._create_datetime, self.url, self.uri,
         self._followers_count, self._following_count,
         self._status_count, self._last_status) = data_tuple

