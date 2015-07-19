from urllib import request

url='http://www.python.org'

connection=request.urlopen(url)

print(connection.read())
