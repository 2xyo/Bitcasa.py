# Bitcasa.py
Bitcasa.py allow you to upload local files or weblinks to your [Bitcasa.com](https://bitcasa.com) account from command-line.

Do not use this script unless you understand what you're doing[^1] or if you think that you are a hipster.


## How does this script work?
This script uses [casperjs](http://casperjs.org/) (and [phantomjs](http://phantomjs.org/)) in order to connect to the web interface of  Bitcasa (to retrieve cookies, tokens, etc.). Then, it uses the upload feature of the Bitcasa chrome extension . See the quick and dirty `casper-poc.js`.


```
$ python bitcasa.py --help
usage: Bitcasa.py [-h] [--verbose] [--version] [--conf ARG_CONF] [-d]
                  [--url URL] [--allurl ALLURL] [--file FILENAME]
                  [--dir DIRNAME] [--list LISTNAME] [--status STATUS]
                  [--search SEARCH]

Bitcasa API

optional arguments:
  -h, --help       show this help message and exit
  --verbose, -v    -v N or -v, -vv, etc
  --version        show program's version number and exit
  --conf ARG_CONF  Config file
  -d, --deamon     Run as deamon : NOT YET IMPLEMENTED
  --url URL        url to uplaod : NOT YET IMPLEMENTED
  --allurl ALLURL  Upload all urls at allurl : NOT YET IMPLEMENTED
  --file FILENAME  Upload a local file : NOT YET IMPLEMENTED
  --dir DIRNAME    Upload a local dir : NOT YET IMPLEMENTED
  --list LISTNAME  Upload a list of files/urls : NOT YET IMPLEMENTED
  --status STATUS  Status : NOT YET IMPLEMENTED
  --search SEARCH  Search file : NOT YET IMPLEMENTED
```


### This is really crappy! 
This is the only way I've found until the official release of the Bitcasa API.

###It's full of bugs!
I'm waiting your pull request.

###It' slow!
I'm still waiting your pull request.


## Installation

Pre-requisites :

* [casperjs](http://casperjs.org/)
    * [phantomjs](http://phantomjs.org)
* Python 2.7+ (not tested with Python 3+)
* build-essential (for installation via Pypi and setup.py)
* python-dev (for installation via Pypi)
* python-setuptools (for the installation via setup.py)


### From package
Make the package yourself :-)

### From source

```
$ git clone blabla
$ cd src
$ sudo pip install -e 
```

## Configuration

The default configuration file is under:

    ~/.config/Bitcasa.py/


```
.
├── bin
│   └── Bitcasa.py
├── bitcasa
│   ├── BitcasaClient.py
│   ├── BitcasaCore.py
│   ├── BitcasaException.py
│   ├── BitcasaServer.py
│   ├── __init__.py
│   └── js
│       ├── getStatus.js
│       ├── login.js
│       └── upload.js
└── test
    ├── __init__.py
    ├── test_bin_Bitcasa.py
    ├── test_BitcasaClient.py
    ├── test_BitcasaCore.py
    ├── test_BitcasaDeamon.py
    └── test_BitcasaServer.py
```


[^1]: [Il ne faut pas prendre des gens pour des cons mais ne jamais oublier qu’ils en sont](http://sametmax.com/il-ne-faut-pas-prendre-des-gens-pour-des-cons-mais-ne-jamais-oublier-quils-en-sont/)


