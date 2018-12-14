#!/bin/bash
# Date  : 2018-09-18 23:38:22
# Email : b4zinga@outlook.com
# please make sure all the ip address in ./ip.txt


username="root"
password="password"
port="22"
timeout=3

cmd="id > /tmp/b4"

login(){
    echo ""
    echo "-------------------------------------------------------- "
    echo "username: $username  password: $password  port: $port  timeout=$timeout" 
    echo "command: $cmd"
    echo "Remote exec command script"
    echo "--------------------------------------------------------"
    echo ""


    for host in `cat ip.txt`;
    do
        result=""
        result=`sshpass -p "$password" ssh -p $port -o StrictHostKeyChecking=no -o ConnectTimeout=$timeout $username@$host $cmd`
        echo $host >> result.txt
        echo $result >> result.txt

    done
    echo ""
}

login
ls
