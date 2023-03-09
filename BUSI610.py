import feedparser
from os import environ
import Crowbars

class BUSI610:

    name = "BUSI610"
    videos = {}

    def __init__(self):
        feed_data = feedparser.parse(environ["PANOPTOSYNC_BUSI610_FEED"])

        counter = 0
        for i, entry in enumerate(feed_data.entries):
            counter = counter + 1

            title = entry["title"]
            title = title.strip()

            feed_data.entries[i]["title"] = str(counter) + " - " + title

        self.videos = feed_data.entries


