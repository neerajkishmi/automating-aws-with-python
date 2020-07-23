# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2020-07-22T06:12:02.384Z', 'eventName': 'ObjectCreated:CompleteMultipartUpload', 'userIdentity': {'principalId': 'AWS:AIDAZUQBJYW6L45TDG4IB'}, 'requestParameters': {'sourceIPAddress': '67.190.189.38'}, 'responseElements': {'x-amz-request-id': '874830AC7E1A5ABC', 'x-amz-id-2': 'n0MKoyj2GKBQexr4+2qUkp9k4VTmMJ1q9WTuAxV2xK/XZAvOmTLTLD3zXWxiQkJiNg9CWdWcgFVV7M2BdsZa5T4Obl7gO7GR'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'd3b22b5a-34c8-4418-9b3b-6d6d89114b27', 'bucket': {'name': 'neerajvideolyzervideos12345', 'ownerIdentity': {'principalId': 'A3JVAH2ZFHOMJ8'}, 'arn': 'arn:aws:s3:::neerajvideolyzervideos12345'}, 'object': {'key': 'Pexels+Videos+4640.mp4', 'size': 10278716, 'eTag': '6bcf2e76121ff9d1c3bf616c49650be7-2', 'sequencer': '005F17D8A735CD067D'}}}]}
event
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
get_ipython().run_line_magic('save', '1-7 s3-event-example.py')
