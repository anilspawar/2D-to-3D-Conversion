# cloud/gcs_handler.py
from google.cloud import storage

def upload_file_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to Google Storage."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")
