# backend/cad_converter.py
import ezdxf

def convert_dwg_to_svg(dwg_file):
    doc = ezdxf.readfile(dwg_file)
    svg_path = dwg_file.replace(".dwg", ".svg")

    with open(svg_path, "w") as svg_file:
        for entity in doc.modelspace().query("LINE"):
            svg_file.write(f"<line x1='{entity.dxf.start.x}' y1='{entity.dxf.end.x}' y2='{entity.dxf.end.y}' stroke='black'/>\n")
    
    return svg_path 