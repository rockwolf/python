#!/bin/sh

HOSTNAME="testdb"
DATABASE="finance"
SQLDIR="setup/sql/"
SCRIPTV=$SQLDIR"drop_views.sql"

echo "Drop.sh"
echo "-------"
echo
echo "HOSTNAME=$HOSTNAME"
echo "DATABASE=$DATABASE"
echo
echo "Dropping views..."
psql -h $HOSTNAME $DATABASE < $SCRIPTV
echo "Running $SCRIPT [OK]"
echo
echo 'Done.'
