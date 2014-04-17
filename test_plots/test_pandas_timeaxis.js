// hello-test.js
casper.test.begin("pandas time axis", 1, function(test) {
  casper.start("test_plots/test_pandas_timeaxis.html", function() {
    test.assertTextExists("2010", "xticks should start with year 2010");
  });

  casper.run(function() {
    test.done();
  });
});
