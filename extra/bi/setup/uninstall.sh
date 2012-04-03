#!/bin/sh

HOSTNAME="testdb"
DATABASE="finance"
SCRIPTV="sql/drop_views.sql"
SCRIPTT="sql/drop_tables.sql"

echo "Drop.sh"
echo "-------"
echo
echo "HOSTNAME=$HOSTNAME"
echo "DATABASE=$DATABASE"
echo
echo "Dropping tables..."
psql -h $HOSTNAME $DATABASE < $SCRIPTT
echo "Running $SCRIPT [OK]"
echo "Dropping views..."
psql -h $HOSTNAME $DATABASE < $SCRIPTV
echo "Running $SCRIPT [OK]"
echo
echo 'Done.'
