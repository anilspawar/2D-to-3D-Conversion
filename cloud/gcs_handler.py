# cloud/gcs_handler.py
from google.cloud import storage

client = stoarge.Client()
bucket_name = "my-2d-to-3d"

def upload_file(file_path):
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_path.split("/")[-1])
    blob.upload_from_filename(file_path)
    return f"gs://{bucket_name}/{blob.name}"