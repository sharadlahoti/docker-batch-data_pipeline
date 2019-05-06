
# coding: utf-8
#"Submit a job to AWS Batch and then submit another job which depends on the first job completion"

import boto3


jq= #Enter the queue name
jdef1= #Enter the first job definition
jdef2= #Enter the 2nd job definition



batch = boto3.client('batch')



response1 = batch.submit_job(jobName='test-job1',
                             jobQueue=jq, 
                             jobDefinition=jdef1, 
                             containerOverrides={
                                 "command": ['python3', 'ist_scripts/s3-boto-read-write.py'], 
                             }
                            )

print("Job ID is {}.".format(response1['jobId']))



response2 = batch.submit_job(jobName='test-job2', 
                            jobQueue=jq, # sufficient for most jobs
                            jobDefinition=jdef2, # use a real job definition
                            dependsOn=[{'jobId':response1['jobId']}],
                            containerOverrides={
                                "command": ['python3', 'ist_scripts/s3-boto-read-write.py'], 
                            })

print("Job ID is {}.".format(response2['jobId']))

