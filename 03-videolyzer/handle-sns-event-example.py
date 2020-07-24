# coding: utf-8
event = {'JobId': 'de818133a79755c5c98db83a9de4b0a92aff0425e48cc98844ee9bde673ab21e', 'ResponseMetadata': {'RequestId': 'b344a96e-ef8f-456e-a1c6-4623a6ca0214', 'HTTPStatusCode': 200, 'HTTPHeaders': {'content-type': 'application/x-amz-json-1.1', 'date': 'Fri, 24 Jul 2020 03:35:11 GMT', 'x-amzn-requestid': 'b344a96e-ef8f-456e-a1c6-4623a6ca0214', 'content-length': '76', 'connection': 'keep-alive'}, 'RetryAttempts': 0}}
event
event_1 = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:662501443004:handleLabelDetectionTopic:bd636388-1de7-40c5-a4ca-79ebe50d8032', 'Sns': {'Type': 'Notification', 'MessageId': '4c0eed08-6588-586a-85b5-ba9c3cda7d80', 'TopicArn': 'arn:aws:sns:us-east-1:662501443004:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"de818133a79755c5c98db83a9de4b0a92aff0425e48cc98844ee9bde673ab21e","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1595561746288,"Video":{"S3ObjectName":"Pexels Videos 4640.mp4","S3Bucket":"neerajvideolyzervideos12345"}}', 'Timestamp': '2020-07-24T03:35:46.372Z', 'SignatureVersion': '1', 'Signature': 'XXkRSEiEaqzPXXeKDrhgHR65/msp5luJ5JoDxVP3L5Db5NcKeOF3trHlUAw3YhswvM6xxh3A4Uq5hvBcunLJdJ1oo4Zkw3gJMcaTaizjMoq/kO+T740OdvKiKiZvoNpFfJn03SYKC1FYZW8DHlOzunYgvBG4cmEztB5CPmG+7Eu6ZZ80R9izbZnLQflJrzq9oQuB05QRooQKlFbYSVRwPZiig4F0nEANuZUtEfcroLQy7XbhUEG8NYYFFEgpzyiBqe7vnJfpahMpl1MTju9aUlH3Ll2ELIikMSChraiHLEl2/LVBaOQTxAbPnuYy6YhwYhvMEWOxGfynTsPjM6SnUw==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-a86cb10b4e1f29c941702d737128f7b6.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:662501443004:handleLabelDetectionTopic:bd636388-1de7-40c5-a4ca-79ebe50d8032', 'MessageAttributes': {}}}]}
event_1
event_2 = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:662501443004:handleLabelDetectionTopic:bd636388-1de7-40c5-a4ca-79ebe50d8032', 'Sns': {'Type': 'Notification', 'MessageId': '273c082a-9e5e-5f3b-b412-5fbe2b0c7b53', 'TopicArn': 'arn:aws:sns:us-east-1:662501443004:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"bb0e9adeac76bd1e1ff1267590b48947dace44091982bebf070bee6aa97e109b","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1595585298239,"Video":{"S3ObjectName":"Pexels Videos 4640.mp4","S3Bucket":"neerajvideolyzervideos12345"}}', 'Timestamp': '2020-07-24T10:08:18.351Z', 'SignatureVersion': '1', 'Signature': 'ZcO7zp0JjkKd8++UEWKSrGzHQGJ9vbG/1PfSiu3bFEQHBVVq8X5ZW7Nyypz2Q/RM9fRtQAqm+T6dW6yd6QH+nYKbpW49U2R24ixwBTuq1c+18Q9UWaimJnvmO+DuntjAyupEiwYRgg3p1kRxSlwLET9wD6INmgS8ybTl1slswxAzaWs3izy6raF+xeJnmOajZhVj2k9/KQKPUP3C70AnSSF+k36ML7jTPQYXpGzNGGFWif7LW2Duzl7QQ8Is5v1KSlYFFNrCJBDHWhm5HnN89dZ3TA/fQ9QLhH1n6VKQVe9ZYCmKafywwhSe4GrkgAUaeNzbZlYrqs/ZMoiRWd8ZRg==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-a86cb10b4e1f29c941702d737128f7b6.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:662501443004:handleLabelDetectionTopic:bd636388-1de7-40c5-a4ca-79ebe50d8032', 'MessageAttributes': {}}}]}
event.keys()
event_2.keys()
event_2['Records'][0]
event_2['Records'][0].keys()
event_2['Records'][0]['EventSource']
event_2['Records'][0]['EventVersion']
event_2['Records'][0]['EventSubscriptionArn']
event_2['Records'][0]['Sns']
event_2['Records'][0]['Sns'].keys()
event_2['Records'][0]['Sns']['Message']
event_2['Records'][0]['Sns']['Message'].keys()
import json
json.loads(event_2['Records'][0]['Sns']['Message'])
json.loads(event_2['Records'][0]['Sns']['Message']).keys()
json.loads(event_2['Records'][0]['Sns']['Message'])['JobId']
json.loads(event_2['Records'][0]['Sns']['Message'])['Video']
json.loads(event_2['Records'][0]['Sns']['Message'])['Video']['S3ObjectName']
json.loads(event_2['Records'][0]['Sns']['Message'])['Video']['S3Bucket']
json.loads(event_2['Records'][0]['Sns']['Message'])['JobId']
