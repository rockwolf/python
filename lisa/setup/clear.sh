#!/bin/sh

HOSTNAME="testdb"
DATABASE="finance"
SQLDIR="setup/sql/"
SCRIPTT=$SQLDIR"clear_tables.sql"

echo "Drop.sh"
echo "-------"
echo
echo "HOSTNAME=$HOSTNAME"
echo "DATABASE=$DATABASE"
echo
echo "Clearing tables..."
psql -h $HOSTNAME $DATABASE < $SCRIPTT
echo "Running $SCRIPT [OK]"
echo
echo 'Done.'
