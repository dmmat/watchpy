### NOTE

now work in linux systems (debian, ubuntu, arch, etc) and windows ([IN BETA](https://github.com/dmmat/watchpy/releases)) and chrome browser

# Installation FOR WINDOWS

download [watch.exe](https://github.com/dmmat/watchpy/releases/download/v1.1.beta/watch.exe) and run


# Installation FOR LINUX

## auto 

```
\curl -sSL https://raw.githubusercontent.com/dmmat/watchpy/master/install_watchpy.sh | bash -s stable
```

## manual 

* download [watch.py](https://raw.githubusercontent.com/dmmat/watchpy/master/watch.py)  to home or run directory 

* make executable run 

    ``` 
    $ chmod + x watch.py 
    $ ./watch.py
    ```


# Usage

for torrent watch install [vlc](https://www.videolan.org/vlc/#download) and [peerflix](https://www.npmjs.com/package/peerflix)

```
$ python3 watch.py https://www.youtube.com/watch?v=tO01J-M3g0U
```

OR 

```
$ python3 watch.py
> Please enter url: 
```


supported additional params like ```--incognito```

### to upgrade run:

``` python3 watch.py upgrade ```

### supported platforms:

- youtube.com
- uafilm.tv
- fanserials.com and others fanserials.*
- kinofuxy.tv
- twitch.tv
- p***hub.com (open in incognito tab)
- torrent file or magnet link ( install [vlc](https://www.videolan.org/vlc/#download) and [peerflix](https://www.npmjs.com/package/peerflix))
