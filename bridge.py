import requests

_ENDPOINT = "https://scrapbook.hackclub.com/api"

def set_kwargs(cls, **kwargs):
    for k,v in kwargs.items():
        setattr(cls, k,v)

class ScrapbookPost:
    def __init__(self,
                 text:str,
                 timestamp:float,
                 postedAt:str,
                 attachments:list=[],
                 reactions:list=[],
                 **kwargs):
        self.text = text
        self.timestamp = timestamp
        self.postedAt = postedAt
        self.attachments = attachments
        self.reactions = reactions
        set_kwargs(self, **kwargs)

class ScrapbookUser:
    def __init__(self,
                 slackID:str,
                 username:str,
                 streakCount:str=0,
                 maxStreaks:int=0,
                 streaksToggledOff:bool=True,
                 website:str=None,
                 github:str=None,
                 avatar:str=None,
                 timezone:str=None,
                 timezoneOffset:int=0,
                 pronouns:str=None,
                 posts:list[ScrapbookPost]=[],
                 **kwargs):
        self.slackID = slackID
        self.username = username
        self.streakCount = streakCount
        self.maxStreaks = maxStreaks
        self.streaksToggledOff = streaksToggledOff
        self.website = website
        self.github = github
        self.avatar = avatar
        self.timezone = timezone
        self.timezoneOffset = timezoneOffset
        self.pronouns = pronouns
        self.posts = posts
        set_kwargs(self, **kwargs)

    @classmethod
    def from_username(cls, username):
        r = requests.get(f"{_ENDPOINT}/users/{username}")
        data = r.json()
        profile = data.get("profile", {})
        posts = data.get("posts", [])

        formattedPosts = []

        for post in posts:
            newPost = ScrapbookPost(**post)
            formattedPosts.append(newPost)

        return cls(posts=formattedPosts, **profile)

if __name__ == "__main__":
    user = ScrapbookUser.from_username("mathias")
    print(user.github)

    print("\n")

    post = user.posts[0]
    print(post.text)
