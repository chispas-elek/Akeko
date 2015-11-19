#!/bin/bash

SERVICIO="Apache"
DIRECCION="www.akeko.com/apache-server/?ehu"
EXPECTED_ARGS=2
E_BADARGS=65



if [ $# -ne $EXPECTED_ARGS ]
    then
    echo "Usage: $0 dbuser action"
    exit $E_BADARGS

else
    
    if [ $2 = True ] ; then
        
        PASSWORD=`source ./scripts/_random_password_gen.sh`

        echo "$1"
        echo "$PASSWORD"
        echo "$SERVICIO"
        echo "$DIRECCION"
    else
        # Acción de borrado
        echo "borrado"
	    echo "$SERVICIO"
	    echo "$DIRECCION"
    fi
    
fi
