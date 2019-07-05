# easy-pysa
python wrapper library and demonstration interface for EasyRSA v3

This project can maintain user certificates for an OpenVPN instance, using easy-rsa version 3.

You need an existing OpenVPN server and easy-rsa setup to use this to maintain certificates.  If you do not have one, then building one is easy, here are some instructions for users lucky enough to use Debian 10:

Install the basic environment
```
apt install openvpn easy-rsa
```

Make the CA

```
cd /etc/openvpn
make-cadir ca
# now edit ca/vars for your needs (e.g. REQ_CITY. Specifically ensure expiry times are suitable for your environment, EASYRSA_CA_EXPIRE, EASYRSA_CERT_EXPIRE)

./easyrsa init-pki
./easyrsa build-ca nopass
./easyrsa build-server-full server nopass

./easyrsa gen-dh
```

Configure OpenVPN /etc/openvpn/server.conf, example to tweak
```
;local a.b.c.d
port 1194
proto udp
;dev tap
dev tun

ca ca.crt
cert server.crt
key server.key  # This file should be kept secret

dh dh2048.pem

server 172.16.0.0 255.255.0.0 
client-to-client
keepalive 10 120
cipher AES-256-CBC
max-clients 100
user nobody
group nogroup
persist-key
persist-tun

status /var/log/openvpn/openvpn-status.log
log         /var/log/openvpn/openvpn.log
log-append  /var/log/openvpn/openvpn.log
verb 3

ifconfig-pool-persist /var/log/openvpn/ipp.txt
push "route 172.16.0.0 255.248.0.0" 

client-config-dir ccd
```

Make sure AUTOSTART="server" is uncommented in /etc/default/openvpn, then run 
```systemctl daemon-reload
service openvpn restart
```

Now you can use this lovely software.
