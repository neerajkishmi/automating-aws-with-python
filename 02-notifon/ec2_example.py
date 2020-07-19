# coding: utf-8
import boto3
session = boto3.Session(profile_name="pythonAutomation")
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
get_ipython().run_line_magic('ls', '-ltr python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-ltr python_automation_key.pem')
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-922914f7')
img.name
img = ec2.Image('ami-0e9089763828757e1')
img.name
ecs2_apse = session.resource('ec2',region_name'ap-southeast-2')
ecs2_apse = session.resource('ec2', region_name='ap-southeast-2')
ecs2_apse = session.resource('ec2', region_name='ap-southeast-2')
img_apse=ec2_apse.Image('ami-0e9089763828757e1')
img_apse=ecs2_apse.Image('ami-0e9089763828757e1')
img_apse=ecs2_apse.Image('ami-0e9089763828757e1')
img_apse.name
img.name
img.name
ami_name = 'amzn-ami-hvm-2018.03.0.20200602.1-x86_64-gp2'
filters = [{'Name':'name', 'Values':[ami_name]}]
type(ami_name)
list(ec2.images.filter(Owner=['amazon'], Filters=filters))
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
list(ecs2_apse.images.filter(Owners=['amazon'], Filters=filters))
img
img
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('pprint', '(filters)')
import pprint from pprint
from pprint import pprint
from pprint import pprint
pprint(filters)
key
key.key_name
img.id
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
instances
ec2.Instance(id='i-03b7591e5926ae5d8')
inst = instances[0]
inst
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
type(inst.security_groups)
type(inst.security_groups)
inst.security_groups[0]
type(inst.security_groups[0])
inst.security_groups[0]['GroupId']
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, IpProtocol='TCP', 'IpRanges': [{'CidrIp': '2601:282:4103:14d0:310a:9ac:f99d:340a/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol'='TCP', 'IpRanges': [{'CidrIp': '2601:282:4103:14d0:310a:9ac:f99d:340a/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '2601:282:4103:14d0:310a:9ac:f99d:340a/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol':'TCP', 'Ipv6Ranges': [{'CidrIp': '2601:282:4103:14d0:310a:9ac:f99d:340a/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '2601:282:4103:14d0:310a:9ac:f99d:340a/64'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '2601:282:4103:14d0:310a:9ac:f99d:340a/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '67.190.189.38/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
inst.public_dns_name
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ec2_example.py 1-80')
