#!/usr/bin/env bash
Cur_Dir=$(pwd)
echo $Cur_Dir
echo "export ORACLE_HOME=":$Cur_Dir:"ora/instantclient_21_5" >> /etc/profile
echo "export ORACLE_SID=ORCL" >> /etc/profile
echo "export TNS_ADMIN=$ORACLE_HOME/network/admin" >> /etc/profile
echo "export LD_LIBRARY_PATH=$ORACLE_HOME" >> /etc/profile
echo "export PATH=$ORACLE_HOME:$PATH" >> /etc/profile

echo $PATH
echo $ORACLE_HOME
echo $ORACLE_SID
echo $LD_LIBRARY_PATH
echo $TNS_ADMIN

echo $Cur_Dir:"/ora/instantclient_21_5 > /etc/ld.so.conf.d/oracle-instantclient.conf"
ldconfig

cd ora
unzip instantclient-basic-linux.x64-21.5.0.0.0dbru.zip
unzip instantclient-sdk-linux.x64-21.5.0.0.0dbru.zip
unzip instantclient-sqlplus-linux.x64-21.5.0.0.0dbru.zip