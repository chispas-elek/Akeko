#!/bin/bash

EXPECTED_ARGS=2
E_BADARGS=65
MYSQL=`which mysql`



if [ $# -ne $EXPECTED_ARGS ]
    then
    echo "Usage: $0 dbuser action"
    exit $E_BADARGS

else
    
    if [ $2 = True ] ; then
        
        PASSWORD="$(sh ./_random_password_gen.sh)"
        Q1="CREATE DATABASE IF NOT EXISTS db_$1;"
        Q2="GRANT USAGE ON *.* TO $1@localhost IDENTIFIED BY '$PASSWORD';"
        Q3="GRANT ALL PRIVILEGES ON db_$1.* TO $1@localhost;"
        Q4="FLUSH PRIVILEGES;"
        SQL="${Q1}${Q2}${Q3}${Q4}"
    

        $MYSQL -uroot -pgoldensun108 -e "$SQL" 
        echo "username:$1"
        echo "password:$PASSWORD"

    else

        # Acción de borrado
        SQL="DROP USER '$1'@'localhost';"
        $MYSQL -uroot -pgoldensun108 -e "$SQL" 
    fi
    
fi