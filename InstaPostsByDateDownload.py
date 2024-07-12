import os
from datetime import datetime
from itertools import dropwhile, takewhile
import instaloader
L = instaloader.Instaloader()

#Add path to the folder where you wish to store the download
os.chdir(r"Path to the folder where you want the instagram post to be downloaded")

#Replace user_name with username of the instagram account whose post is to be downloaded
posts = instaloader.Profile.from_username(L.context, "user_name").get_posts() 
FROM = datetime(2024, 7, 10) #starting from this day onwards(inclusive or specified date also included)
TILL = datetime(2024, 7, 11) #end date not included or posts only till, one day before the date specified here are taken

#Replace DowloadFolder with your choice for the folder name where the download will be stored
for post in takewhile(lambda p: p.date > FROM, dropwhile(lambda p: p.date > TILL, posts)):
    print(post.date)
    L.download_post(post, "DownloadFolder") 