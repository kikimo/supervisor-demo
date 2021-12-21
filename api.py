# coding: utf-8

from xmlrpc import client
import pdb

server_url = 'http://localhost:9001/RPC2'
server = client.ServerProxy(server_url)
print('server status:')
print(server.supervisor.getState())

print('server methods:')
print(server.system.listMethods())

print('foo process info:')
print(server.supervisor.getProcessInfo('foo'))

print('stop foo process:')
print(server.supervisor.stopProcess('foo'))

print('start foo process:')
print(server.supervisor.startProcess('foo'))

