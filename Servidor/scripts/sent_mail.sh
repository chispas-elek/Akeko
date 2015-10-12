#!/bin/bash

EXPECTED_ARGS=2 

 

SENT=`cat /path/to/file | mail -s "your subject"` "$1"
echo $SENT