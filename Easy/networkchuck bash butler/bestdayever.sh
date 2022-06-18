#!/bin/bash

name = $(name)

echo "Good morning, $name!!"
sleep 1
echo "You're looking great today, $name!"
sleep 2
echo "I've prepared the weather forecast for you!"
sleep 2
curl wttr.in
echo "Have a good day, $name!"