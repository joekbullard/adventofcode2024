#!/bin/bash

for i in $(seq -f "%02g" 3 25);
do
    if [ ! -d "day$i" ]; then
        echo "Creating directory day$i and adding templates"
        mkdir "day$i"
    fi

    cp template_solution.py "day$i/solution.py"
    cp template_test.py "day$i/test_$i.py"
    touch "day$i/input.txt"
    touch "day$i/example.txt"

done