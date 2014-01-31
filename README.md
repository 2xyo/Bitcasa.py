
# This repo is outdated

See :

 - [BitcasaFS](https://github.com/biscuitlabs/BitcasaFS)
 - [Bitcasa-Python-SDK](https://github.com/biscuitlabs/Bitcasa-Python-SDK)
 - [bitcasapy](https://github.com/konomae/bitcasapy)
 
-------------------------------------------------------------------------------------------------------------
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


```bash
$ ./getDownloadLinks.py
Bitcasa username: you@email.dot
Password:
URL: (go to https://my.bitcasa.com/, open developer tools > Network > select XHR, get the F** Request URL)
It looks like https://my.bitcasa.com/directory/41911e413516101d84115e109101dabaee/cbd7de83994beffbcb156f87840168/Pictures/?bottom=500&show-incomplete=true&sort_ascending=true&sort_column=name&top=0
URL: https://my.bitcasa.com/directory/44974e/?bottom=500&show-incomplete=true&sort_ascending=true&sort_column=name&top=0
Directory 1
Directory 2
File 3
...

$ cat links.html
<ul>
<li>(<a href='https://my.bitcasa.com/download-send/65b07c1804d87cd7c54a20ae82/'>DL</a>) - <a href='http://l.bitcasa.com/q79TJGHUy'>Family movie.mkv</a> - (2.9 GB)</li>
<li>...</li>
</ul>
```

# FAQ

### This is really crappy!
This is the only way I've found until the official release of the Bitcasa API.
