from bs4 import BeautifulSoup
import requests
import datetime
import shutil
import os

url = 'https://www.bing.com'
html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')
preloadBg = soup.find(id='preloadBg').get('href')

wallpaper_url = url + preloadBg
wallpaper = requests.get(wallpaper_url, stream=True)
file_name = '{}_{}.jpeg'.format('wallpaper', datetime.datetime.now().date())


with open("wallpapers/{}".format(file_name), 'wb') as out_file:
    shutil.copyfileobj(wallpaper.raw, out_file)
del wallpaper


os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri {}".format(file_name))