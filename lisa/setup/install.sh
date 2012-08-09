#!/bin/sh

HOSTNAME="testdb"
DATABASE="finance"
SQLDIR="setup/sql/"

echo "Create.sh"
echo "---------"
echo
echo "HOSTNAME=$HOSTNAME"
echo "DATABASE=$DATABASE"
echo "Creating tables..."
FILE=$SQLDIR"create_tables.sql"
psql -h $HOSTNAME $DATABASE < $FILE
echo "Running $FILE [OK]"
echo
echo "Creating views..."
FILE=$SQLDIR"create_views.sql"
psql -h $HOSTNAME $DATABASE < $FILE
echo "Running $FILE [OK]"
echo
echo "Filling tables..."
FILE=$SQLDIR"init_tables.sql"
psql -h $HOSTNAME $DATABASE < $FILE
echo "Running $FILE [OK]"
echo
echo "Done."
