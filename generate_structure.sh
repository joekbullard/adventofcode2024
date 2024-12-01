#!/bin/bash

for i in $(seq -f "%02g" 1 25);
do 
    mkdir day$i
    cp solution_template.py day$i/solution.py
    cp test_template.py day$i/test_$i.py
    touch day$i/input.txt
    touch day$i/example.txt
done