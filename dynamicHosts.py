#!/bin/python
import boto3
import json

def get_hosts(ec2,fv1):
    #f={{'Name':'tag:ApigeeEnv','Values':[fv1]},{'Name':'tag:ClusterPurpose','Values':[fv2]}}
    f={'Name':'tag:InstanceRole','Values':[fv1]}
    hosts=[]
    for each_in in ec2.instances.filter(Filters=[f]):
        #print each_in.private_ip_address
        if each_in.private_ip_address is not None:
          hosts.append(each_in.private_ip_address)
        #when: each_in.private_ip_address is defined
        #when: each_in.private_ip_address.stderr | length > 0
    return hosts

def main():
    ec2=boto3.resource("ec2")
    msNodes=get_hosts(ec2,"buildServer")
    mpNodes=get_hosts(ec2,"appServer")
    allNodes= {
        'buildServer': {
            'hosts': buildServer,
            'vars': {
                'group_name': 'buildServer'
            }
        },
        'appServer': {
            'hosts': appServer,
            'vars': {
                'group_name': 'appServer'
            }
        }
    }
    print json.dumps(allNodes)

if __name__=="__main__":
    main()
