#!/bin/bash
WORK_DIR=$1
SDR=$WORK_DIR/sdr.tmp
SEL=$WORK_DIR/sel.tmp
POWER=$WORK_DIR/power.tmp

#
#if [ -e $WORK_DIR/sdr.tmp ]; then
#	rm $SDR
#fi
#
#if [ -e $WORK_DIR/sel.tmp ]; then
#	rm $SEL
#fi
#
#if [ -e $WORK_DIR/power.tmp ]; then
#	rm $POWER
#fi
#
# sdr
while read p;do
	IFS=" " read -ra DATA <<< "$p"
	#echo "${DATA[0]}/${DATA[1]}"
	echo "#####"	>> $SDR
	echo "${DATA[1]}" >> $SDR
	ipmitool -I lanplus -H ${DATA[0]}	-U admin -P 2001May09! sensor >> $SDR
done < $1/hostfile
echo "#####"	>> $SDR

#sel
while read p;do
	IFS=" " read -ra DATA <<< "$p"
	#echo "${DATA[0]}/${DATA[1]}"
	echo "#####"	>> $SEL
	echo "${DATA[1]}" >> $SEL
	ipmitool -I lanplus -H ${DATA[0]}	-U admin -P 2001May09! sel list 20 >> $SEL
done < $1/hostfile
echo "#####"	>> $SEL

#chassis(power)
#sel

while read p;do
	IFS=" " read -ra DATA <<< "$p"
	#echo "${DATA[0]}/${DATA[1]}"
	echo "#####"	>> $POWER
	echo "node: ${DATA[1]}" >> $POWER
	ipmitool -I lanplus -H ${DATA[0]}	-U admin -P 2001May09! chassis status |grep  'System' >> $POWER
done < $1/hostfile
echo "#####"	>> $POWER


cp $WORK_DIR/sdr.tmp $WORK_DIR/sdr.log && rm $WORK_DIR/sdr.tmp
cp $WORK_DIR/sel.tmp $WORK_DIR/sel.log && rm $WORK_DIR/sel.tmp
cp $WORK_DIR/power.tmp $WORK_DIR/power.log && rm $WORK_DIR/power.tmp


