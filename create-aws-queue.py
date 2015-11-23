import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2
# Get the keys from a specific url and then use them to connect to AWS Service
key = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
keys = key.read();
key1, key2 = keys.split(':')

access_key_id = key1
secret_access_key = key2

# Set up a connection to the AWS service.
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

# Creating a new queue
name = sys.argv[1]
q = conn.create_queue(name)
