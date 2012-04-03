#!/bin/sh

HOSTNAME="testdb"
DATABASE="finance"
SUBDIR="sql"

echo "install.sh"
echo "---------"
echo
echo "HOSTNAME=$HOSTNAME"
echo "DATABASE=$DATABASE"
echo "Creating tables..."
FILE=$SUBDIR"/create_tables.sql"
psql -h $HOSTNAME $DATABASE < $FILE
echo "Running $FILE [OK]"
echo
echo "Creating views..."
FILE=$SUBDIR"/create_views.sql"
psql -h $HOSTNAME $DATABASE < $FILE
echo "Running $FILE [OK]"
echo
echo "Filling tables..."
FILE=$SUBDIR"/init_tables.sql"
#psql -h $HOSTNAME $DATABASE < $FILE
echo "Running $FILE [OK]"
echo
echo "Done."
