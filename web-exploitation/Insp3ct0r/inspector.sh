#!/bin/bash

sites_list=('http://jupiter.challenges.picoctf.org:9670' 'http://jupiter.challenges.picoctf.org:9670/mycss.css' 'http://jupiter.challenges.picoctf.org:9670/myjs.js')

for i in ${sites_list[@]};do
        flag=$(curl $i 2>/dev/null|grep flag|cut -d: -f 2|awk '{print$1}')
        echo -n $flag
done
echo ""
