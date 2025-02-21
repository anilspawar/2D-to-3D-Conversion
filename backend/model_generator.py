# backend/model_generator.py

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs


def generate_3d_model(svg_file):
    box = BRepPrimAPI_MakeBox(10, 10, 5).Shape()      # Placeholder shape
    step_writer = STEPControl_Writer()
    step_writer.Transfer(box, STEPControl_AsIs)

    step_file = svg_file.replace(".svg", ".step")
    step_writer.Write(step_file)
    return step_file