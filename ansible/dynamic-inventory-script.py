#!/usr/bin/env python
import boto3
import json

# AWSの認証情報を設定
aws_access_key = $AWS_ACCESS_KEY_ID
aws_secret_key = $AAWS_SECRET_ACCESS_KEY
aws_region = $AWS_DEFAULT_REGION

# EC2クライアントの作成
ec2 = boto3.client('ec2', region_name=aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# タグに基づいてインスタンスを検索
response = ec2.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': ['raisetech13']}])

# Ansibleのインベントリ情報を生成
inventory = {'raisetech13': {'hosts': []}}

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        private_ip = instance['PublicIpAddress']
        inventory['raisetech13']['hosts'].append(private_ip)

print(json.dumps(inventory))