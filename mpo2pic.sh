#!/bin/bash

P=$1 
for i in $P/*.MPO
do
	python3 $MPOE $i
done
rm $P/*-L.jpg
rm $P/*-R.jpg
exit

