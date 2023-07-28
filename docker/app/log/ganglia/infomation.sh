WORK_DIR=$1
GANGLIA=$WORK_DIR/ganglia.xml


#
#if [ ! -e $GANGLIA ]; then
#rm $GANGLIA
#fi

cat < /dev/tcp/127.0.0.1/8651 > $GANGLIA
#telnet localhost 8651 > $GANGLIA
#sed -i '1,3d' $GANGLIA
