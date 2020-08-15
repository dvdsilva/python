import boto3

#s3 = boto3.resource('s3')
#for bucket in s3.bucket.all():
 #   print(bucket.name)

#s3 = boto3.client("s3")
#all_objects = s3.list_objects(Bucket = 'bucket-name')

s3.create_bucket(Bucket='mybucket_14323')

s3.create_bucket(Bucket='mybucket_14323', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-1'})


