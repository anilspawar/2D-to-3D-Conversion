# backend/app.py
from flask import Flask, request, jsonify
from utils.cad_converter import convert_dwg_to_svg
from utils.model_generator import generate_3d_model

app = Flask(__name__)

@app.route("/convert", methods=["POST"])
def convert_2d_to_3d():
    file = request.files["file"]
    file_path = f"samples/{file.filename}"
    file.save(file_path)

    svg_path = convert_dwg_to_svg(file_path)
    step_file = generate_3d_model(svg_path)

    return jsonify({"3d_mpodel": step_file})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
