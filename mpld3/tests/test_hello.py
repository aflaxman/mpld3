import subprocess

result = subprocess.call(["casperjs", "test", "mpld3/tests/hello-test.js"])

assert result == 0
