import os

import Crowbars
import Panopto
from BUSI610 import BUSI610
from BUSI690 import BUSI690

def start_parsing(session):
    classes = [
        BUSI610(),
        BUSI690()
    ]

    for cs_class in classes:
        class_name = cs_class.name
        existing_guids = Crowbars.get_existing_guids(class_name)

        for video in cs_class.videos:
            video_url = video["id"]

            if video_url not in existing_guids:
                Crowbars.log("Found new video: [" + class_name + "] " + video["title"])
                Crowbars.log("Making crawl job...")
                crawl_job = Crowbars.make_crawl_job(session, video, class_name)
                Crowbars.log("Saving crawl job...")
                Crowbars.save_crawl_job(crawl_job, video_url, class_name)
                Crowbars.log("Marking as processed...")
                Crowbars.save_guid(class_name, video_url)
                Crowbars.log("Done.")

session = Panopto.perform_sso_login(os.environ["PANOPTOSYNC_SSO_USERNAME"], os.environ["PANOPTOSYNC_SSO_PASSWORD"])
start_parsing(session)
