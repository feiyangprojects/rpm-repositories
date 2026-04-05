#!/usr/bin/bash -e
cd "$(dirname "$(realpath "$0")")"

RELEASE="$(curl --fail 'https://api.github.com/repos/JetBrains/intellij-community/releases/latest' | jq --raw-output '.tag_name')"
JAVA_RELEASE="$(curl --fail "https://raw.githubusercontent.com/JetBrains/intellij-community/refs/tags/$RELEASE/build/jbr-toolchains.bzl"|grep --only-matching --perl-regexp --max-count=1 '\d+\.\d+\.\d+')"
sed -Ei "s#(%global featurever +).+#\1${JAVA_RELEASE%%.*}#" java-android-studio.spec
