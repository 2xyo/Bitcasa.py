# Bitcasa.py
Bitcasa.py allow you to upload local files or weblinks to your [Bitcasa.com](https://bitcasa.com) account from command-line.

Do not use this script unless you understand what you're doing[^1] or if you think that you are a hipster.


## How does this script work?
This script uses [casperjs](http://casperjs.org/) (and [phantomjs](http://phantomjs.org/)) in order to connect to the web interface of  Bitcasa (to retrieve cookies, tokens, etc.). Then, it uses the upload feature of the Bitcasa chrome extension . See the quick and dirty `casperjs-poc.js`.


```
casperjs  --username=YOURUSERNAME --password=YOUPASSWORD --url=http://example.com/yourfile.ext casperjs-poc.js
```

### This is really crappy! 
This is the only way I've found until the official release of the Bitcasa API.

###It's full of bugs!
I'm waiting your pull request.

###It' slow!
I'm still waiting your pull request.


### It's not in python ?
I have tried with [ghost.py](https://github.com/jeanphix/Ghost.py/) but there is a [bug](https://github.com/jeanphix/Ghost.py/issues/91)...
