#!/usr/bin/python3

from subprocess import call
import sys
import re
import http.client
from urllib.parse import urlparse
import json


def main():
    link = sys.argv[1] if len(sys.argv) > 1 and url_valid(sys.argv[1]) else enter_url(True)
    additional_params = sys.argv[2] if len(sys.argv) > 2 else ""
    params = ["google-chrome-stable"];
    if "youtu.be/" in link:
        link = "https://www.youtube.com/embed/%s" % re.search(r"(?<=\.be/).*", link).group()
        link = re.sub(r"(&.+)$", '', link)
    elif "youtube.com/" in link:
        link = "https://www.youtube.com/embed/%s" % re.search(r"[^&?]*v=([^&?]*)", link).group(1)
        link = re.sub(r"(&.+)$", '', link)
    elif "kinofuxy.tv" in link:
        document = http_get(link)
        link = re.search(r"(\<meta\ property=\"og:video\"\ content=\")(.*)(\".)", document).group(2)
    elif "uafilm.tv" in link:
        link = "http://uafilm.tv/embed/%s/" % re.search(r"(uafilm\.tv\/)(\d+)(\-)", link).group(2)
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
        links = json.loads(re.search(r"(playerData\ \=.')(\[.*\])(\';)", document).group(2))
        for idx, t_link in enumerate(links):
            index = idx + 1
            if (t_link['name'] != "Альтернативный плеер"):
                print(("[%d] " % index) + t_link.get('name'))
        link_number = input("enter number: ")
        link = links[int(link_number) - 1]['player']
    params.append("--app=%s" % link)
    if additional_params:
        params.append(additional_params)
    print(params)
    return call(params)


def upgrade():
    print("searching last version")
    file_path = "%s/watch.py" % sys.path[0]
    download_link = "https://raw.githubusercontent.com/dmmat/watch.py/master/watch.py"
    print("downloading last version")
    call(["wget", download_link, "-O", file_path])
    print("seting file rules")
    call(["chmod", "+x", file_path])
    print("upgrading done")


def enter_url(first=False):
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
    parsed_url = urlparse(url);
    if parsed_url.scheme == 'http':
        conn = http.client.HTTPConnection(parsed_url.netloc)
    else:
        conn = http.client.HTTPSConnection(parsed_url.netloc)
    conn.request("GET", parsed_url.path)

    res = conn.getresponse()
    return res.read().decode('utf-8')


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

project link: https://gist.github.com/dmmat/22d228856ef9de7957c9fb5aea2780be

            """)


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        if (sys.argv[1] == "upgrade"):
            upgrade()
        elif (sys.argv[1] == "help" or sys.argv[1] == "--help"):
            print_help()
        else:
            main()
    else:
        main()
