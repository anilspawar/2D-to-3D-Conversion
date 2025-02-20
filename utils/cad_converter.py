# utils/cad_converter.py
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox

def create_step_model(output_filename):
    box = BRepPrimAPI_MakeBox(10, 20, 30).Shape()
    step_writer = STEPControl_Writer()
    step_writer.Transfer(box, STEPControl_AsIs)
    step_writer.Write(output_filename)
    print(f"3D model saved as {output_filename}.")
