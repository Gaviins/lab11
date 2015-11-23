import boto
import urllib2

key = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
keys = key.read();
key1, key2 = keys.split(':')

print boto.Version
print(key1)
print(key2)
