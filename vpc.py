import boto3

# Create VCP and List VPCs id
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#client

def client_connect():
    try:
        connection = boto3.client("ec2")
        return connection
    except Exception as e:
        print(str(e))

def create_vpc():
    try:
        client = client_connect()
        response = client.create_vpc(
            CidrBlock = "10.2.0.0/16",
            TagSpecifications = [{
                "ResourceType":"vpc",
                "Tags": [
                         {
                            "Key": "Name",
                            "Value": "Test_VPC"
                         },
                         {
                            "Key": "env",
                            "Value":"dev" 
                         }
                        ]
            }]
        )
        print(response)
    except Exception as e:
        print(str(e))

#create_vpc()

#Create Subnet
def list_vpc():
    try:
        client = client_connect()
        response = client.describe_vpcs(
            Filters = [{
                "Name":"tag:Name",
                "Values":["Test_VPC"]
            }]
        )
        print(response)
        return response["Vpcs"][0]["VpcId"]
    except Exception as e:
        print(str(e)) 

#list_vpc()
def create_sub():
     try:
         vpc_id = list_vpc()
         client = client_connect()
         response1 = client.create_subnet(
             TagSpecifications = [{
                 "ResourceType": "subnet",
                 "Tags": [
                     {
                        "Key":"Name",
                        "Value":"My-Subnet"
                     },
                     {
                         "Key": "Env",
                         "Value": "Dev"
                     }
                 ]

             }],
             CidrBlock = "10.2.1.0/24",
             VpcId = vpc_id

         )
         print(response1)
     except Exception as e:
        print(str(e))

#create_sub()

