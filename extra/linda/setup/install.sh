#!/bin/sh

HOSTNAME="testdb"
DATABASE="finance"
SQLDIR="setup/sql/"

#TODO: do all of this in python, also for lisa!
echo "Create.sh"
echo "---------"
echo
echo "HOSTNAME=$HOSTNAME"
echo "DATABASE=$DATABASE"
echo "Creating views..."
FILE=$SQLDIR"create_views.sql"
psql -h $HOSTNAME $DATABASE < $FILE
echo "Running $FILE [OK]"
echo
echo "Done."
