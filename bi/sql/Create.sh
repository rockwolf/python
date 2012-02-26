#!/bin/sh

HOSTNAME="testdb"
DATABASE="finance"

echo "Create.sh"
echo "---------"
echo
echo "HOSTNAME=$HOSTNAME"
echo "DATABASE=$DATABASE"
echo "Creating tables..."
FILE="create_tables.sql"
psql -h $HOSTNAME $DATABASE < $FILE
echo "Running $FILE [OK]"
echo
echo "Creating views..."
FILE="create_views.sql"
psql -h $HOSTNAME $DATABASE < $FILE
echo "Running $FILE [OK]"
echo
echo "Filling tables..."
FILE="init_tables.sql"
#psql -h $HOSTNAME $DATABASE < $FILE
echo "Running $FILE [OK]"
echo
echo "Done."
