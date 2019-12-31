#!/bin/bash
echo '<!-- === Begin output from fonts.sh === -->'
for f in ../dist/*.ttf;
do
    s='../dist/'
    r=""
    ff=${f/$s/$r}
    fs=${ff/%\.ttf/$r}
    if [[ $fs =~ "ASCII" || $fs =~ "Italic" ]]; then continue; fi
    STYLE=`echo $fs | sed -E -e 's/.*Style([A-Za-z0-9])+-.*/\1/'`

    if [[ ${#STYLE} -eq 1 ]]; then
        echo "<h2>Style $STYLE</h2>"
    else
        echo "<h2>Base Style</h2>"
    fi

    filesize() {
        printf `du -h "$1" | cut -f1`
        printf "<br/>"
        printf "\n"
    }

    H3="<h3>Regular</h3>"
    echo $H3;
convert -font "$f" -pointsize 288 label:'Beekeepers QqGgRrAa\nMMMM ЖЖЖЖ אאאלף' "$fs".png
echo "<img src=\"""$fs".png"\">"
VAR='<a href="'$f'">'$ff'</a>'
echo $VAR;
filesize "${f}"
WOFF2="${VAR//ttf/woff2}";
echo $WOFF2;


filesize "${f//ttf/woff2}"
    if [[ -f "${f/Regular/Italic}" ]]; then
        convert -font "${f/Regular/Italic}" -pointsize 288 label:'Beekeepers QqGgRrAa\nMMMM ЖЖЖЖ אאאלף' "${fs/Regular/Italic}".png
        echo "${H3/Regular/Italic}";
        echo "<img src=\"""${fs/Regular/Italic}".png"\">"
        echo "${VAR//Regular/Italic}"; filesize "${f/Regular/Italic}"; echo "${WOFF2//Regular/Italic}"; W2="${f/Regular/Italic}"; W2="${W2//ttf/woff2}"; filesize $W2;

    fi
    if [[ -f "${f/Regular/Regular-ASCII}" ]]; then echo "${VAR//Regular/Regular-ASCII}"; filesize "${f/Regular/Regular-ASCII}"; echo "${WOFF2//Regular/Regular-ASCII}"; W2="${f/Regular/Regular-ASCII}"; W2="${W2//ttf/woff2}"; filesize $W2; fi

done
echo '<!-- End output from fonts.sh -->'
