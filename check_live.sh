#!/usr/bin/env bash
# Checks the LIVE site (not the repo): each page 200 with its own text, a made-up path 404, the icon byte-identical
# to the committed one. A control (privacy URL checked for the terms text) must FAIL, or the check proves nothing.
set -u
BASE="${1:-https://lagowski.github.io/sciencegloon-site}"
fail=0
check() {  # path, expected text
  local body code
  code=$(curl -s -o /tmp/sg_body.$$ -w '%{http_code}' "$BASE/$1"); body=$(cat /tmp/sg_body.$$)
  if [[ "$code" == 200 ]] && grep -qF "$2" <<<"$body"; then echo "OK   $code /$1 has '$2'"; return 0; fi
  echo "FAIL $code /$1 lacks '$2'"; return 1
}
check ""                  "Ciencia explicada en un minuto."    || fail=1
check "privacy/"          "<h1>Privacy Policy</h1>"            || fail=1
check "terms/"            "<h1>Terms of Service</h1>"          || fail=1
check "tiktok-callback/"  "<h1>Authorization</h1>"             || fail=1
check "style.css"         "body"                               || fail=1
code=$(curl -s -o /dev/null -w '%{http_code}' "$BASE/no-such-page-$RANDOM/")
[[ "$code" == 404 ]] && echo "OK   404 on a made-up path" || { echo "FAIL made-up path gave $code"; fail=1; }
here=$(dirname "$0")
for f in assets/app-icon-1024.png assets/logo-120.png favicon.png tiktokQmNRhqelgtuHDAcOZez9T4hX9my44Ufx.txt; do
  live=$(curl -s "$BASE/$f" | sha256sum | cut -d' ' -f1); repo=$(sha256sum "$here/$f" | cut -d' ' -f1)
  [[ "$live" == "$repo" ]] && echo "OK   $f byte-identical ($live)" || { echo "FAIL $f live $live != repo $repo"; fail=1; }
done
echo "-- control (must FAIL):"
if check "privacy/" "<h1>Terms of Service</h1>"; then echo "CONTROL BROKEN: the check passed a wrong page"; fail=1
else echo "control failed as it must"; fi
rm -f /tmp/sg_body.$$
exit $fail
