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

* download [install_watchpy.sh](https://raw.githubusercontent.com/dmmat/watchpy/master/install_watchpy.sh) 

* run sh file

    ``` 
    $ sh install_watchpy.sh
    ```


# Usage

for torrent watch install [vlc](https://www.videolan.org/vlc/#download) and [peerflix](https://www.npmjs.com/package/peerflix)

```
$ watchpy https://www.youtube.com/watch?v=tO01J-M3g0U
```

OR 

```
$ watchpy
> Please enter url: 
```


supported additional params like ```--incognito```

### to upgrade run:

``` watchpy upgrade ```

### supported platforms:

- youtube.com
- uafilm.tv
- fanserials.com and others fanserials.*
- kinofuxy.tv
- twitch.tv
- p***hub.com (open in incognito tab)
- torrent file or magnet link ( install [vlc](https://www.videolan.org/vlc/#download) and [peerflix](https://www.npmjs.com/package/peerflix))
