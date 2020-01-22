import os

import subprocess
import json
import pprint

token = input("Enter Spotify Token")
code = "curl -X \"GET\" \"https://api.spotify.com/v1/me/player/currently-playing\" -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer " + token + "\""
x = subprocess.check_output(code)
jsonInput = json.loads(x)
pprint.pprint(jsonInput)
artist = jsonInput['item']['album']['artists'][0]['name']
name = jsonInput['item']['name']
album = jsonInput['item']['album']['name']
pic = jsonInput['item']['album']['images'][0]['url']
data = name + "#" + album + "#" + artist + "#" + pic
import socket

HOST = "localhost"
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as err:
    print('Bind failed. Error Code : '.format(err))
s.listen(10)
print("Socket Listening")
conn, addr = s.accept()
while (True):
    conn.send(bytes(data + "\r\n", 'UTF-8'))
    print("Message sent")
    data = conn.recv(1024)
    print(data.decode(encoding='UTF-8'))
