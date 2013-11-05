// casperjs --ignore-ssl-errors=true --proxy=127.0.0.1:8080 --web-security=no --cookies-file=mycookies.txt --local-storage-quota=50Mb --local-storage-path=store --disk-cache=true  bit.js


var casper = require('casper').create({
    verbose: true,
    logLevel: "debug",
    waitTimeout: 80000
});

var utils = require('utils');
var fs = require('fs')


casper.start();

casper.userAgent('Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Ubuntu Chromium/25.0.1364.160 Chrome/25.0.1364.160 Safari/537.22');

casper.thenOpen('https://my.bitcasa.com/logout');



casper.waitForSelector('form button', function() {
     this.fill('form[action]', { 
        "user": casper.cli.get("username"),
        "password": casper.cli.get("password")
     }, true);

});

casper.waitForSelector('article.ng-scope');

casper.thenOpen('https://portal.bitcasa.com');

casper.waitForSelector('article.ng-scope');

casper.thenOpen('https://portal.bitcasa.com/uploader/download-to-bitcasa', {
    method: 'post',
    data:   {
        'file': casper.cli.get("url"),
        'cookie': '', 
        'cookies':  JSON.stringify([])
    },
    headers: {
        'Accept-Language': 'fr,fr-fr;q=0.8,en-us;q=0.5,en;q=0.3',
        'Accept' : '*/*',
        'Accept-Charset' : 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Origin': ' chrome-extension://jbebdjcjllheeclffnofhgcimmlkkbon',
        'User-Agent': 'Mozilla/5.0 (X11; Linux) AppleWebKit/537.32 (KHTML, like Gecko) Chrome/27.0.0453.14 Safari/527.36',
        'X_REQUESTED_WITH': 'XMLHttpRequest'

    }
    
}, function(response) {
    require('utils').dump(response);
});



casper.thenOpen('https://portal.bitcasa.com/uploader/get-upload-status', function(response) {
    require('utils').dump(JSON.parse(this.getPageContent()));
});




casper.run();
