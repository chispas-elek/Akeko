#!/bin/bash

EXPECTED_ARGS=2 
E_BADARGS=65


if [ $# -ne $EXPECTED_ARGS ]
    then
    echo "Usage: $0 dbuser action"
    exit $E_BADARGS

else
   `echo "$1" | mail -s "Akeko notifications" $2`
    echo "ok"
fi
