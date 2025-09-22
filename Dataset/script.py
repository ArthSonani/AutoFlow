import os

# Path to your labels folder
labels_folder = "/Users/arthsonani/Desktop/AutoFlow/Dataset/labels/train"

auto_count = 0
total_count = 0

# Loop through all .txt files
for filename in os.listdir(labels_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(labels_folder, filename)
        
        with open(file_path, "r") as f:
            for line in f:
                # Get class id (first number in each line)
                class_id = line.strip().split()[0]
                
                if class_id == "0":  # auto
                    auto_count += 1
                total_count += 1

print(f"Total number of 'auto' (class 0): {auto_count}")
print(f"Total: {total_count}")
