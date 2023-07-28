#!/bin/bash

if [ -e $1/jobhistory_bar ];then
	rm $1/jobhistory_bar
fi

while read p;do
	echo $p |tr -d '' >> $1/jobhistory_bar
done < $1/jobhistory
