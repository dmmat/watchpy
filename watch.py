#!/usr/bin/python3

from subprocess import call
import sys
import re
import http.client
from urllib.parse import urlparse
import json


def main():
    link = sys.argv[1] if len(sys.argv) > 1 and url_valid(sys.argv[1]) else enter_url()
    additional_params = sys.argv[2] if len(sys.argv) > 2 else ""

    if sys.platform == "linux" or sys.platform == "linux2":
        params = ["google-chrome-stable"]
    elif sys.platform == "darwin":
        params = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
    elif sys.platform == "win32":
        params = ["C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"]

    if "youtu.be/" in link:
        link = "https://www.youtube.com/embed/%s" % re.search(r"(?<=\.be/).*", link).group()
        link = re.sub(r"(&.+)$", '', link)
    elif "youtube.com/" in link:
        link = "https://www.youtube.com/embed/%s" % re.search(r"[^&?]*v=([^&?]*)", link).group(1)
        link = re.sub(r"(&.+)$", '', link)
    elif "kinofuxy.tv" in link:
        document = http_get(link)
        link = re.search(r"(<meta property=\"og:video\" content=\")(.*)(\".)", document).group(2)
    elif "uafilm.tv" in link:
        link = "http://uafilm.tv/embed/%s/" % re.search(r"(uafilm\.tv/)(\d+)(-)", link).group(2)
    elif "twitch.tv/" in link:
        link = "https://player.twitch.tv/?channel=%s" % re.search(r"(?<=\.tv/).*", link).group()
    elif "view_video.php" in link:  # =) for hub site
        link = re.sub(r'(.*)(view_video\.php\?viewkey=)(.*)', r"\1embed/\3", link)
        params.append("--incognito")
    elif (".torrent" in link) or ("magnet:?" in link):
        print("open torrent in vlc")
        return call(["peerflix", "%s" % link, "--vlc", "-l"])
    elif "fanserials." in link:
        document = http_get(link)
        links = json.loads(re.search(r"(playerData =.')(\[.*\])(\';)", document).group(2))
        for idx, t_link in enumerate(links):
            index = idx + 1
            if t_link['name'] != "Альтернативный плеер":
                print(("[%d] " % index) + t_link.get('name'))
        link_number = input("enter number: ")
        link = links[int(link_number) - 1]['player']
    params.append("--app=%s" % link)
    if additional_params:
        params.append(additional_params)
    print(params)
    call(params)
    if sys.platform == "win32":
        windows_aot(link)
    return True


def upgrade():
    if sys.platform == "linux" or sys.platform == "linux2":
        print("searching last version")
        file_path = "%s/watch.py" % sys.path[0]
        download_link = "https://raw.githubusercontent.com/dmmat/watch.py/master/watch.py"
        print("downloading last version")
        call(["wget", download_link, "-O", file_path])
        print("seting file rules")
        call(["chmod", "+x", file_path])
        print("upgrading done")


def enter_url():
    link = input("Please enter url: ")
    return link if url_valid(link) else enter_url()


def url_valid(url):
    if "magnet:?" in url:
        return True
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    valid = re.match(url_regex, url) is not None
    if not valid:
        print('invalid url')
    return valid


def http_get(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme == 'http':
        conn = http.client.HTTPConnection(parsed_url.netloc)
    else:
        conn = http.client.HTTPSConnection(parsed_url.netloc)
    conn.request("GET", parsed_url.path)

    res = conn.getresponse()
    return res.read().decode('utf-8')


def windows_aot(url):
    import win32gui
    import win32con
    raw_html = http_get(url)
    match = re.search('<title>(.*?)</title>', raw_html)
    title = match.group(1) if match else url.replace('http://', '').replace('https://', '')
    print(title)
    while True:
        hwnd = win32gui.FindWindow(None, title)
        if hwnd:
            win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 600, 400, 0)
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 600, 400, 0)
            break


def print_help():
    print("""
supported platforms:
    youtube.com
    uafilm.tv
    fanserials.com and others fanserials.*
    kinofuxy.tv
    twitch.tv
    p***hub.com (open in incognito tab)
    torrent file or magnet link

available params:
    upgrade         get last script version
    help            this text
    --incognito     run in chrome incognito tab

    and also supported all perflix and chrome params

project link: https://github.com/dmmat/watch.py

            """)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "upgrade":
            upgrade()
        elif sys.argv[1] == "help" or sys.argv[1] == "--help":
            print_help()
        else:
            main()
    else:
        main()
