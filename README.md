# SimpleGoApp
Simple Go App CICD

Below tasks can be performed by code in this repo
1. IAAC : Setup build server and application server
2. Pull code from GitHub and perform build, push artefacts to S3 bucket (CI)
3. Pull build artefacts from S3 bucket and deploy application (CD)

Pre-requisties
AWS account set-up
Ansible controller is setup with boto3
Internet access to EC2 instances
Before running Make sure aws creds are updated in .boto file
2 EC2 instances are created 1 for build server and another for App server with tag InstanceRole=buildServer and InstanceRole=appServer

To setup build server execute below runbook at root
ansible-playbook -i dynamicHosts.py setupBuildServer.yml --extra-vars "node_filter=buildServer"

To perform build execute below runbook at root
ansible-playbook -i dynamicHosts.py buildApp.yml --extra-vars "node_filter=buildServer"

To setup application server execute below runbook at root
ansible-playbook -i dynamicHosts.py setupAppServer.yml --extra-vars "node_filter=appServer"

To perform build execute below runbook at root
ansible-playbook -i dynamicHosts.py deployApp.yml --extra-vars "node_filter=appServer"
