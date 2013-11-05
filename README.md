Do not use these scripts unless you understand what you're doing[^1] or if you think that you are an hipster.


# upload.js
`upload.js` allow you to upload local files or weblinks to your [Bitcasa.com](https://bitcasa.com) account from command-line.


## How does this script work?
This script uses [casperjs](http://casperjs.org/) (and [phantomjs](http://phantomjs.org/)) in order to connect to the web interface of  Bitcasa (to retrieve cookies, tokens, etc.). Then, it uses the upload feature of the Bitcasa chrome extension . 


```
casperjs  --username=YOURUSERNAME --password=YOUPASSWORD --url=http://example.com/yourfile.ext upload.js
```

# getDownloadLinks.py
`getDownloadLinks.py` allow you to get the download link (direct URL and short URL) of all files in a directory.


## How does this script work?
This script uses the Python binding for [selenium](https://pypi.python.org/pypi/selenium) in order to connect to the web interface of Bitcasa whith Firefox. 


```
% ./getDownloadLinks.py
Bitcasa username:
yohann@lepage.info
Password: 
URL: (go to https://my.bitcasa.com/, open developer tools > Network > select XHR, get the F** Request URL)
https://my.bitcasa.com/directory/44974e48354610fd84215e50930edfb755cbd7de83994beffbcb156f87840168/BPictures/?bottom=500&show-incomplete=true&sort_ascending=true&sort_column=name&top=0
<ul>
<li>(<a href='https://my.bitcasa.com/download-send/c3ea54blabla3b507/gifs.zip'>DL</a>) - <a href='http://l.bitcasa.com/XXXXX'>gifs</a> - (5.2 GB)</li>
<li>(<a href='https://my.bitcasa.com/download-send/07f6blablaecf7ab/Photos.zip'>DL</a>) - <a href='http://l.bitcasa.com/YYYYYY'>Photos</a> - (406.5 GB)</li>
</ul>

```

### This is really crappy! 
This is the only way I've found until the official release of the Bitcasa API.

###It's full of bugs!
I'm waiting your pull request.

###It' slow!
I'm still waiting your pull request.

### It's not headless?
I have tried with [ghost.py](https://github.com/jeanphix/Ghost.py/) but there is a [bug](https://github.com/jeanphix/Ghost.py/issues/91)...