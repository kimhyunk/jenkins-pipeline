#!/bin/bash

RUNTIME=""
while read p;do
	IFS=" " read -ra DATA <<< "$p"
	let RUNTIMEs=${DATA[1]}/${DATA[0]}
	let RUNTIMEh+=$RUNTIMEs/60
done < $1/runtime.tmp
echo $RUNTIMEh > $1/runtime.log
