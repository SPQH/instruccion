#!/bin/bash

time=$(date '+%d/%m/%Y %H:%M:%S')

echo -e "INICIO SCRIPT \t ($time)" >> ifc.log
/sbin/ifconfig >> /tmp/ifc.log
echo -e "FIN SCRIPT \t ($time) \n \n" >> ifc.log
