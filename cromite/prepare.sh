#!/usr/bin/bash -e
cd "$(dirname "$(realpath "$0")")"

curl --fail --location --output chrome-lin64.tar.gz https://github.com/uazo/cromite/releases/latest/download/chrome-lin64.tar.gz
curl --fail --location --output app_icon.png https://www.cromite.org/app_icon.png
sed -Ei sed -E "s#(Version: +).+#\1$(curl --fail https://api.github.com/repos/uazo/cromite/releases/latest | jq -r '.tag_name[1:] | split("-")[0]')#" cromite.spec
