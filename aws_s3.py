import boto3

#Create connection 
def create_connection():
    try:
        client = boto3.client("s3")
        return client
    except Exception as e:
        print(str(e))

#Create S3 bucket 

def create_bucket():
    try:
        client = create_connection()
        response = client.create_bucket(
            ACL = 'private',
            Bucket = 'testboto3bucketcreeate'
        )
        print(response)

    except Exception as e:
        print(str(e))


#List the bucket
def list_buckets():
    try:
        client = create_connection()
        response = client.list_buckets()
        #buckets = [bucket['Name'] for bucket in response['Buckets']]
        #print("Bucket List: %s" % buckets)
        #print(response["Buckets"][0]["Name"])
        return response["Buckets"][0]["Name"]

        #print(response)

    except Exception as e:
        print(str(e))


#Upload a file in S3 Bucket 
def upload_file_in_s3():
    try:
        filename = "gowebapi.yaml"
        bucket_name = list_buckets()
        client = create_connection()
        response = client.upload_file(
            filename,
            bucket_name,
            filename
        )
        if response == None :
            print("File uploaded succesfully")
    except Exception as e:
        print(str(e))

#Download file from S3 bucket
def download_file_from_s3():
    try:
        client = create_connection()
        response = client.

    except Exception as e:
        print(str(e))

#create_connection()
#create_bucket()
#upload_file_in_s3()


