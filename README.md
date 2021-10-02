# AESMessage API
Demo on how to use AESMessage.com API (AES256)

Encrypt:
```Python
payload = {'option':'encrypt','text':'hello world. This is an example text', 'passwd':"helloworld"}
r = requests.post('https://aesmessage.com/api_v1.py', data=payload)

foo = json.loads(r.text)
formatted = json.dumps(foo, indent=2)

print(formatted)
```

Decrypt:
```Python
payload = {'option':'decrypt','text':'IpqG8y0KhH1CpOzEgB4XKysdWp0z8Ye5rTgaImc/3WqLWEmWElMAYGTT5nSFDlI5laWyauPMmyVTwTDPGmwbpQ==', 'passwd':"helloworld"}
r = requests.post('https://aesmessage.com/api_v1.py', data=payload)

foo = json.loads(r.text)
formatted = json.dumps(foo, indent=2)

print(formatted)
```
Example Output:
```json
[
  "data",
  {
    "option": "encrypt",
    "message": "FMATsNI5OuTRa35Qwb4gFOEhBU4rfcctnVcrn6f9a84MjG+pjcvRTL69vCD/7JjpDWi341Rc7TB3mNQJsc9XOw=="
  },
  "metrics",
  {
    "status_code": "200",
    "process_time": "0:00:00.001620"
  },
  "copyright",
  {
    "banner": "Created with AESMessage.com API",
    "author": "Leon H. Voerman"
  }
]
 ```

 If an error occures, you'll get different status code. For exmaple: if the password doesn't match while decrypting, you'll get a status code 500.
 
 The API works with both GET and POST. However, using GET is HIGHLY INSECURE and should not be used other than for testing only.
 
 Example using GET: <https://aesmessage.com/api_v1.py?option=encrypt&text=hello%20world&passwd=foo>
