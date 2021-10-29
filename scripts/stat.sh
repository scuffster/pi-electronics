#!/bin/bash
export PATH=$PATH:/home/pi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games
echo "1. who am i" > ./env.out
echo $(whoami) >> ./env.out
su - pi
echo " just su - pi ==== " >> ./env.out
env >> ./env.out
echo "2. who am i" >> ./env.out
echo $(whoami) >> ./env.out
echo "==== id" >> ./env.out
id >> ./env.out
aplay /home/pi/pi-electronics/scripts/047964051-clapping-hands-outdoor.wav > /home/pi/pi-electronics/scripts/aplay.out
