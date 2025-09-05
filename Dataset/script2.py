import os
import xml.etree.ElementTree as ET

# Paths
xml_folder = "xmls_test"   # folder where XMLs are stored
output_folder = "val"     # folder to save YOLO TXT labels
os.makedirs(output_folder, exist_ok=True)

# Keep only vehicle classes
allowed_classes = ["Auto", "Bus", "Car"]   # 🚗 add more if needed (like 'Truck', 'Motorcycle')

# Step 1: Build filtered class list
classes = sorted(list(allowed_classes))
print("✅ Classes selected for training (Person excluded):")
for i, cls in enumerate(classes):
    print(f"  {i}: {cls}")

# Step 2: Convert XML to YOLO
for xml_file in os.listdir(xml_folder):
    if not xml_file.endswith(".xml"):
        continue
    
    tree = ET.parse(os.path.join(xml_folder, xml_file))
    root = tree.getroot()

    size = root.find("size")
    if size is None:
        continue
    w = int(size.find("width").text)
    h = int(size.find("height").text)

    txt_filename = os.path.join(output_folder, xml_file.replace(".xml", ".txt"))
    with open(txt_filename, "w") as f:
        for obj in root.findall("object"):
            cls = obj.find("name").text.strip()
            if cls not in classes:   # 🚫 skip "Person" or any unwanted class
                continue
            cls_id = classes.index(cls)

            xmlbox = obj.find("bndbox")
            xmin = int(xmlbox.find("xmin").text)
            ymin = int(xmlbox.find("ymin").text)
            xmax = int(xmlbox.find("xmax").text)
            ymax = int(xmlbox.find("ymax").text)

            # Convert to YOLO format (x_center, y_center, width, height) normalized
            x_center = ((xmin + xmax) / 2) / w
            y_center = ((ymin + ymax) / 2) / h
            bw = (xmax - xmin) / w
            bh = (ymax - ymin) / h

            f.write(f"{cls_id} {x_center:.6f} {y_center:.6f} {bw:.6f} {bh:.6f}\n")

# Save mapping for reference
with open("classes.txt", "w") as f:
    for i, cls in enumerate(classes):
        f.write(f"{i}: {cls}\n")

print("🎯 Conversion complete! Labels saved in 'labels/'")
print("📄 Class mapping saved to 'classes.txt'")
