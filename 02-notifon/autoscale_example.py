# coding: utf-8
import boto3
session = boto3.Session(profile_name="pythonAutomation")
ec2 = session.resource('ec2')
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName='python_automation_key')
ami_name = 'amzn-ami-hvm-2018.03.0.20200602.1-x86_64-gp2'
filters = [{'Name':'name', 'Values':[ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
img = ec2.Image('ami-0e9089763828757e1')
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName='python_automation_key')
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
inst.security_groups[0]
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '67.190.189.38/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
inst.public_dns_name
session
as_client = session.client('autoscaling')
as_client.describe_auto_scaling_groups()
as_client.describe_policies()
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group Latest', PolicyName='Scale Down')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group Latest', PolicyName='Scale Up')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group Latest', PolicyName='Scale Up')
