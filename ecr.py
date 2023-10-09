import boto3
import os

# Initialize an ECR client
ecr = boto3.client('ecr')

ecr_repository = 'my-cloud-native-repo'

response = ecr.create_repository(repositoryName=ecr_repository)

repository_uri = response['repository']['repositoryUri']

print(repository_uri)

image_tag = 'my-flask-app'
