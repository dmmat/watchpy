#instalation

```
\curl -sSL https://raw.githubusercontent.com/dmmat/watch.py/master/install_watchpy.sh | bash -s stable
```

for torrent watch install [vlc](https://www.videolan.org/vlc/#download) and [peerflix](https://www.npmjs.com/package/peerflix)

```
$ python3 watch.py https://www.youtube.com/watch?v=tO01J-M3g0U
```

OR 

```
$ python3 watch.py
> Please enter url: 
```


to make executable run 
``` 
$ chmod + x watch.py 
$ ./watch.py
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