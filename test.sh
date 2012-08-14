#!/bin/bash

place='Modules/'
for i in $(ls $place | grep -E '*py$')
do
	echo '+--------------'
	echo '| Testing: '$place$i
	echo '+--------------'
	python "$place$i" "test"
	echo '> Test done !'
	echo ''
done
