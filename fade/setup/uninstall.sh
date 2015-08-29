#!/bin/sh

HOSTNAME="debby_test"
DATABASE="finance"
SQLDIR="sql/"
SCRIPTV=$SQLDIR"drop_views.sql"
SCRIPTT=$SQLDIR"drop_tables.sql"

echo "Drop.sh"
echo "-------"
echo
echo "HOSTNAME=$HOSTNAME"
echo "DATABASE=$DATABASE"
echo
echo "Dropping views..."
psql -h $HOSTNAME $DATABASE < $SCRIPTV
echo "Running $SCRIPT [OK]"
echo "Dropping tables..."
psql -h $HOSTNAME $DATABASE < $SCRIPTT
echo "Running $SCRIPT [OK]"
echo
echo 'Done.'
