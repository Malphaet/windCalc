#!/bin/bash

place='Modules/'
for i in $(ls $place | grep '.py')
do
	echo 'Testing: '$place$i
	echo '---------'
	python "$place$i" "test"
done
