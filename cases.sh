#!/bin/bash

printf "Введите букву x:"
read x
case $x in
         [[:lower:]])
         echo "Низкий регистр"
         ;;
         [[:upper:]])
         echo "Верхний регистр"
         ;;
         [0-9])
         echo "Число"
esac