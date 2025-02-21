# cloud/cloud_function.py
import funtions_framework
from google.cloud import storage
from backend.model_generator import generate_3d_model

@functions_framework.http
def process_2d_file(request):
    request_json = request.get_json()
    file_path = request_json["file_path"]

    step_file = generate_3d_model(file_path)
    return {"3d_model": step_file}