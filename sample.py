import boto3
import sys

# secret_key = sys.argv[0]
# access_key = sys.argv[1]
# region     = sys.argv[2]

def list_instance():
	client  = boto3.client("ec2")
	res = client.describe_instances()
	print (res)


def main():
	list_instance()
main()
