#!/bin/bash
if [ $# -ne 1 ]
then
    echo "Usage: $0 <day#>"
    exit 1
fi

DAY="day$1"

mkdir $DAY
cd $DAY

touch "$DAY.py"
echo "f = 'day$1/data.txt'" >> "$DAY.py"

echo "with open(f, 'r') as of:" >> "$DAY.py"
echo "    content = of.read().strip()" >> "$DAY.py"

git add "$DAY.py"
touch "data.txt"

touch "test.txt"
# tag=code
# end="</code></pre>"
# curl -s "https://adventofcode.com/2022/day/13" | sed -n "/<code><pre>/,/$end/p" | sed '1d;$d'>> test.txt

# grep -zoP "(?<=).*(?=<\/$tag>)"
# sed -e 's/code\>\(.*\)\<code/\1/'
# grep -oP 'code\K.*(?=code)'

cd ..
