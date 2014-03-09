// hello-test.js
casper.test.begin("Hello, Test!", 1, function(test) {
	console.log("hello, world");
	test.assert(false);
	test.done();
    });

/*
casper.test.begin('Casperjs.org is navigable', 2, function suite(test) {
	casper.start('http://casperjs.org/', function() {
		test.assertTitleMatches(/casperjs/i);
		this.clickLabel('Testing');
	    });

	casper.then(function() {
		test.assertUrlMatches(/testing\.html$/);
	    });

	casper.run(function() {
		test.done();
	    });
    });*/