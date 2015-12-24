#!/bin/sh

for n in `ls`
do
  echo -n '    '
  head -n 9  $n | tail -n 1
  echo -n '  <'
  echo -n $n
  echo  '>'
done

