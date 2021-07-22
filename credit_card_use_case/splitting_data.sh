#!/bin/bash

# create guest data 
head -1 creditcard.csv | awk '{print "\"id\"," $0}' | tr -d \" > creditcard_guest.csv
awk 'FNR>1 && FNR%2==0 {print NR-1","$1}'  creditcard.csv  | tr -d \" >> creditcard_guest.csv

# create host data
head -1 creditcard.csv | awk '{print "\"id\"," $0}' | tr -d \" > creditcard_host.csv
awk 'FNR>1 && FNR%2==1 {print NR-1","$1}'  creditcard.csv | tr -d \" >> creditcard_host.csv
