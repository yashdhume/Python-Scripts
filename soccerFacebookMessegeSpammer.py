import sports_py
from fbchat import Client
from fbchat.models import *
import time

team = 'Manchester United'
team2 = 'Chelsea'
thread_id = input(thread_id)
# print('{}-{}'.format(match.home_score, match.away_score))
while (True):
    match = sports_py.get_match_score('Soccer', team2, team)
    s = int(match.away_score)
    ss = int(match.home_score)
    if s < ss:
        client.send(Message(text="THEY ARE LOSING " + str('({}-{})'.format(match.home_score, match.away_score))),
                    thread_id=thread_id, thread_type=ThreadType.GROUP)
    elif s > ss:
        client.send(Message(text="They are Winning" + str(
            '({}-{})'.format(match.home_score, match.away_score))), thread_id=thread_id,
                    thread_type=ThreadType.GROUP)
    else:
        client.send(Message(text="TIE GAME " + team2 + " " + str(
            '({}-{})'.format(match.home_score, match.away_score))), thread_id=thread_id,
                    thread_type=ThreadType.GROUP)
    time.sleep(15)
