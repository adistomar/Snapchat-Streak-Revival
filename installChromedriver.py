try:
   import requests
except:
   import pip
   pip.main(['install', 'requests'])
   import requests
try:
   from bs4 import BeautifulSoup
except:
   import pip
   pip.main(['install', 'bs4'])
   from bs4 import BeautifulSoup
try:
   import zipfile
except:
   import pip
   pip.main(['install', 'zipfile'])
   import zipfile
try:
   import io
except:
   import pip
   pip.main(['install', 'io'])
   import io
try:
   from subprocess import PIPE, run
except:
   import pip
   pip.main(['install', 'io'])
   from subprocess import PIPE, run
try:
   import sys
except:
   import pip
   pip.main(['install', 'sys'])
   import sys
try:
   import os
except:
   import pip
   pip.main(['install', 'os'])
   import os
try:
   import lxml
except:
   import pip
   pip.main(['install', 'lxml'])
   import lxml
   os.execv(sys.executable, ['python'] + sys.argv)

url = "https://chromedriver.chromium.org/downloads"
urls = []

def out(command):
   result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
   return result.stdout


def get_platform():
   if sys.platform == 'darwin':
      platform = "mac"
   elif sys.platform.startswith("win"):
      platform = "win"
   return platform


def get_version():
   platform = get_platform()
   if platform == "mac":
      chrome_download_path = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version"
      version = out(chrome_download_path)[14:17]
   elif platform == "win":
      chrome_download_path = 'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version'
      version = out(chrome_download_path)[-15:-12]
   return version


def get_download_page():
   global url
   r = requests.get(url, allow_redirects=True)
   soup = BeautifulSoup(r.text, 'html.parser')
   for link in soup.find_all('a'):
      urls.append(str(link.get('href')))
   for url in urls:
      if (f"https://chromedriver.storage.googleapis.com/index.html?path={get_version()}" in url):
         break
   urls.clear()


def download_and_unzip():
   global url
   url = url.replace("index.html?path", "?delimiter=/&prefix")
   soup = BeautifulSoup(requests.get(url).text, features="xml").find_all("Key")
   keys = [f"https://chromedriver.storage.googleapis.com/{k.getText()}" for k in soup if get_platform() in k.getText()]
   r = requests.get(keys[0])
   z = zipfile.ZipFile(io.BytesIO(r.content))
   z.extractall()


get_download_page()
download_and_unzip()