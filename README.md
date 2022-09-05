# SSL/TLS client certificate verification with Python v3.4+ SSLContext

## For this example, we’ll create Self-signed server and client certificates. Normally you’d use a server certificate from a Certificate

## Create server certificate:

`openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt`
  
#### Make sure to enter ‘example.com’ for the Common Name.


## Next, generate a client certificate:

`openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout client.key -out client.crt`
  
#### The Common Name for the client certificate doesn’t really matter.


### Client.py and server.py
#### Start Server then send request from client to verify the certificate.




<!-- 
   \                         /
          \    This page does     /
           ]   not exist yet.    [    ,'|
           ]                     [   /  |
           ]___               ___[ ,'   |
           ]  ]\             /[  [ |:   |
           ]  ] \           / [  [ |:   |
           ]  ]  ]         [  [  [ |:   |
           ]  ]  ]__     __[  [  [ |:   |
           ]  ]  ] ]\ _ /[ [  [  [ |:   |
           ]  ]  ] ] (#) [ [  [  [ :===='
           ]  ]  ]_].nHn.[_[  [  [
           ]  ]  ]  HHHHH. [  [  [
           ]  ] /   `HH("N  \ [  [
           ]__]/     HHH  "  \[__[
           ]         NNN         [
           ]         N/"         [
           ]         N H         [
          /          N            \
         /           q,            \
        /                           \ -->