first app.py is copy from the chatgpt

while doing pip install flask
it shows error

use a virtual env(recommended)

run these commands
python3 -m venv venv

source venv/bin/activate

pip install flask

copy code for index.html from chatgpt 

and run the app 

python3 app.py

its running on locahost:5000

then in browser the videos are not showing up

to make it show, change dns to google dns(fast + reliable)

sudo nano /etc/resolv.conf

add lines

nameserver 8.8.8.8
nameserver 8.8.4.4

save and exit

this is for temporary changes to google dns

for the permanent change

sudo nano /etc/systemd/resolved.conf

DNS=8.8.8.8 8.8.4.4

sudo systectl restart systemd-resolved

can you host flask app on vercel
-> no vercel doesn't support hosting backend python/flask apps - its mainly for
  frontend (react, html, next.js, etc.)


