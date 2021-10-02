#!/usr/bin/env python3
import json
import requests

payload = {'option':'encrypt','text':'hello world. This is an example text', 'passwd':"helloworld"}
r = requests.post('https://aesmessage.com/api_v1.py', data=payload)

foo = json.loads(r.text)
formatted = json.dumps(foo, indent=2)

print('\n --- Data Encrypt ---')
print('Option: ', foo[1]['option'])
print('Text: ', foo[1]['message'])

print('\n --- Metrics ---')
print('Status Code: ', foo[3]['status_code'])
print('Process Time: ', foo[3]['process_time'])

print('\n --- Copyright ---')
print('Banner: ', foo[5]['banner'])
print('Author: ', foo[5]['author'])

payload = {'option':'decrypt','text':'IpqG8y0KhH1CpOzEgB4XKysdWp0z8Ye5rTgaImc/3WqLWEmWElMAYGTT5nSFDlI5laWyauPMmyVTwTDPGmwbpQ==', 'passwd':"helloworld"}
r = requests.post('https://aesmessage.com/api_v1.py', data=payload)

foo = json.loads(r.text)
formatted = json.dumps(foo, indent=2)

print('\n --- Data Decrypt ---')
print('Option: ', foo[1]['option'])
print('Text: ', foo[1]['message'])

print('\n --- End of Demo ---')
