#!/bin/bash
head -1 creditcard.csv | tr -d \" > creditcard_guest.csv
awk 'FNR>1 && FNR%2==0 {print $1}'  creditcard.csv  | tr -d \" >> creditcard_guest.csv
head -1 creditcard.csv | tr -d \" > creditcard_host.csv
awk 'FNR>1 && FNR%2==1 {print $1}'  creditcard.csv | tr -d \" >> creditcard_host.csv
