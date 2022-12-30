import os
from pprint import pprint
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credenciales.json'

storage_client = storage.Client()

bucket_name = 'bucket_datapath_v10'

# creando un nuevo bucket
bucket = storage_client.bucket(bucket_name)
bucket.storage_class = 'COLDLINE' 
bucket.location = 'US' 
bucket = storage_client.create_bucket(bucket) # returns Bucket object

pprint(vars(bucket))

bucket.name
bucket._properties['selfLink']
bucket._properties['id']
bucket._properties['location']
bucket._properties['timeCreated']
bucket._properties['storageClass']
bucket._properties['timeCreated']
bucket._properties['updated']

"""
Get Bucket
"""

my_bucket = storage_client.get_bucket(bucket_name)
# pprint(vars(my_bucket))

"""
Upload File
"""
def upload_to_bucket(blob_name, file_path, bucket_name):

    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False


upload_to_bucket('leads_v1', 'leads.csv', bucket_name)

