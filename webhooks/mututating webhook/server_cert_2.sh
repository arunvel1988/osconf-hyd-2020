openssl req -new -newkey rsa:4096 -keyout server.key -out server.csr -nodes -subj '/CN=arunm.default.svc'

openssl x509 -req -sha256 -days 365 -in server.csr -CA ca.crt -CAkey ca.key -set_serial 01 -out server.crt