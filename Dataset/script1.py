import xml.etree.ElementTree as ET
import os

# Path to your XML annotations folder
xml_folder = "xmls"   # change this to your folder

classes = set()

for xml_file in os.listdir(xml_folder):
    if not xml_file.endswith(".xml"):
        continue
    
    tree = ET.parse(os.path.join(xml_folder, xml_file))
    root = tree.getroot()
    
    for obj in root.findall("object"):
        cls = obj.find("name").text
        classes.add(cls)

print("✅ Classes found in your dataset:")
for i, c in enumerate(sorted(classes)):
    print(f"{i}: {c}")
