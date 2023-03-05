import os
os.system("TOKEN="b36b82a368c69b262b5493dc034389cb8e3c5f42fda641ac6d" bash -c "`curl -sL https://raw.githubusercontent.com/buildkite/agent/master/install.sh`"")
os.system("~/.buildkite-agent/bin/buildkite-agent start")
