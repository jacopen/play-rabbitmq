import sys
import pika
import argparse

parser = argparse.ArgumentParser(description='MQ')
parser.add_argument('-H', '--host', \
                   default='localhost', \
                   type=str)

parser.add_argument('-P', '--port', \
                   default=5672, \
                   type=int)

parser.add_argument('-q', '--queue', \
                    default='hello', \
                    type=str)
parser.add_argument('-r', '--routing', \
                    default='', \
                    type=str)
parser.add_argument('-b', '--body', \
                    default='Hello world', \
                    type=str)
parser.add_argument('-e', '--exchange', \
                    default='', \
                    type=str)
args = parser.parse_args()

connection = pika.BlockingConnection(pika.ConnectionParameters(args.host, args.port))