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
import zipfile, io
from subprocess import PIPE, run


def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

CHROME_DOWNLOAD_PATH_MAC = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version"
BRANCH = "mac"
VERSION = out(CHROME_DOWNLOAD_PATH_MAC)[14:17]
url = "https://chromedriver.chromium.org/downloads"
urls = []


def getDownloadPage():
    global url
    r = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.find_all('a'):
        urls.append(str(link.get('href')))
    for url in urls:
        if (f"https://chromedriver.storage.googleapis.com/index.html?path={VERSION}" in url):
            break
    urls.clear()


def downloadAndUnzip():
    global url
    url = url.replace("index.html?path", "?delimiter=/&prefix")
    soup = BeautifulSoup(requests.get(url).text, features="xml").find_all("Key")
    keys = [f"https://chromedriver.storage.googleapis.com/{k.getText()}" for k in soup if BRANCH in k.getText()]
    r = requests.get(keys[0])
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()


getDownloadPage()
downloadAndUnzip()