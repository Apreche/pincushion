import pickledb
import praw

from pincushion import pinboard, settings


class Reddit:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=getattr(settings, 'REDDIT_CLIENT_ID', ''),
            client_secret=getattr(settings, 'REDDIT_CLIENT_SECRET', ''),
            refresh_token=getattr(settings, 'REDDIT_REFRESH_TOKEN', ''),
            user_agent=getattr(settings, 'REDDIT_USER_AGENT', 'pincushion script'),
        )
        self.me = self.reddit.user.me()
        db_filename = getattr(settings, 'PICKLEDB_FILENAME', 'pincushion.db')
        self.db = pickledb.load(db_filename, True)

    def get_new_saved_posts(self):
        params = {
            'sort': 'new',
        }
        newest_item = self.db.get('reddit_newest_saved_post')
        if newest_item:
            params['before'] = newest_item

        items = self.me.saved(limit=50, params=params)

        first = True
        for item in items:
            if first:
                self.db.set('reddit_newest_saved_post', item.fullname)
                first = False

            tags = [
                '.pincushion',
                '.redditsaved',
                item.subreddit.display_name,
            ]

            link_flair_text = getattr(item, 'link_flair_text', None)
            if link_flair_text is not None:
                tags.append(link_flair_text)

            if item.over_18:
                tags.append('nsfw')

            url = getattr(item, 'url', None)
            if url is None:
                url = getattr(item, 'link_url', None)

            if url[0] == '/':
                url = f"https://www.reddit.com{url}"

            title = getattr(item, 'title', None)
            if title is None:
                title = getattr(item, 'link_title', None)

            description = getattr(item, 'selftext', None)
            if description is None:
                description = getattr(item, 'body', None)

            pinboard.pb_post(
                url,
                title,
                description=description,
                tags=tags,
                toread=True,
            )

    def get_new_upvoted_posts(self):
        params = {
            'sort': 'new',
        }
        newest_item = self.db.get('reddit_newest_upvoted_post')
        if newest_item:
            params['before'] = newest_item

        items = self.me.upvoted(limit=50, params=params)

        first = True
        for item in items:
            if first:
                self.db.set('reddit_newest_upvoted_post', item.fullname)
                first = False

            tags = [
                '.pincushion',
                '.redditupvoted',
                item.subreddit.display_name,
            ]

            link_flair_text = getattr(item, 'link_flair_text', None)
            if link_flair_text is not None:
                tags.append(link_flair_text)

            if item.over_18:
                tags.append('nsfw')

            url = getattr(item, 'url', None)
            if url is None:
                url = getattr(item, 'link_url', None)
            if url[0] == '/':
                url = f"https://www.reddit.com{url}"

            title = getattr(item, 'title', None)
            if title is None:
                title = getattr(item, 'link_title', None)

            description = getattr(item, 'selftext', None)
            if description is None:
                description = getattr(item, 'body', None)

            pinboard.pb_post(
                url,
                title,
                description=description,
                tags=tags,
                toread=False,
            )
