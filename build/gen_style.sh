#!/bin/bash
STYLE=$1
SEQ="$2 $3"

# Style arg required.
if [[ -z $1 ]]; then exit 1; fi;

if [[ -z $2 || -z $3 ]]; then SEQ="1 9"; fi;

if [[ !("$1" =~ [A-G]) ]]; then exit 2; fi

for i in `seq $SEQ`; do
    printf "\033[31mStep $i\e[0m\n"
    ./list_glyphs.py "$TT" | parallel --timeout 500% --progress --bar "./style$1.sh pngs/{}.png $i $i {#}"
done
