#!/bin/bash

#usage: ../timescript.sh dayX.py part1
program_name=$1
output_file=$2

printf "python" > "$output_file.time"
{ time python "$program_name" > /dev/null;
printf "\n" 1>&2;
printf "pypy" 1>&2;
time pypy "$program_name" > /dev/null;
} 2>> "$output_file.time"

