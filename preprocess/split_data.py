import os
import shutil
import random
import glob

def split_dataset(image_dir, label_dir, output_dir,
                  train_ratio=0.6, val_ratio=0.2, test_ratio=0.2):
    assert abs(train_ratio + val_ratio + test_ratio - 1.0) < 1e-6

    # Get all image files with matching label files
    image_files = [f for f in os.listdir(image_dir)
                   if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    paired_files = [f for f in image_files
                    if os.path.exists(os.path.join(label_dir, os.path.splitext(f)[0] + '.txt'))]

    random.shuffle(paired_files)
    total = len(paired_files)
    train_end = int(train_ratio * total)
    val_end = train_end + int(val_ratio * total)

    splits = {
        'train': paired_files[:train_end],
        'val': paired_files[train_end:val_end],
        'test': paired_files[val_end:]
    }

    for split_name, files in splits.items():
        img_out = os.path.join(output_dir, split_name, "images")
        lbl_out = os.path.join(output_dir, split_name, "labels")
        os.makedirs(img_out, exist_ok=True)
        os.makedirs(lbl_out, exist_ok=True)

        for file in files:
            base = os.path.splitext(file)[0]
            src_img = os.path.join(image_dir, file)
            src_lbl = os.path.join(label_dir, base + ".txt")

            dst_img = os.path.join(img_out, file)
            dst_lbl = os.path.join(lbl_out, base + ".txt")

            shutil.copy2(src_img, dst_img)
            shutil.copy2(src_lbl, dst_lbl)

    print(f"Dataset split completed:")
    print(f"  Train: {len(splits['train'])}")
    print(f"  Val:   {len(splits['val'])}")
    print(f"  Test:  {len(splits['test'])}")


def rename_dataset(image_dir, label_dir, prefix="img"):
    """
    Renames images and corresponding YOLO label files to shorter, cleaner names (e.g., img_001.jpg).
    """
    image_exts = ['.jpg', '.jpeg', '.png', '.webp']
    images = [f for f in os.listdir(image_dir) if os.path.splitext(f)[1].lower() in image_exts]
    images.sort()  # ensure consistent order

    for i, img_name in enumerate(images):
        base, ext = os.path.splitext(img_name)
        new_base = f"{prefix}_{i:04d}"
        new_img_name = new_base + ext.lower()

        old_img_path = os.path.join(image_dir, img_name)
        new_img_path = os.path.join(image_dir, new_img_name)

        # Rename image
        try:
            os.rename(old_img_path, new_img_path)
        except Exception as e:
            print(f"Failed to rename image: {old_img_path} -> {new_img_path} | Error: {e}")
            continue

        # Rename label
        old_label_path = os.path.join(label_dir, base + ".txt")
        new_label_path = os.path.join(label_dir, new_base + ".txt")
        if os.path.exists(old_label_path):
            try:
                os.rename(old_label_path, new_label_path)
            except Exception as e:
                print(f"Failed to rename label: {old_label_path} -> {new_label_path} | Error: {e}")
        else:
            print(f"[Warning] Label not found for image: {img_name}")

    print("Renaming completed successfully.")


def change_number_in_files(folder_path, f):
    # Check valid folder
    if not os.path.isdir(folder_path):
        print(f"Folder is {folder_path} invalid!")
        return
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                # Read all files in folder
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                
                # Process line
                new_lines = []
                for line in lines:
                    numbers = line.strip().split()
                    # Check yolo label structure file
                    if len(numbers) == 5:
                        # Change the label in file
                        numbers[0] = str(f)
                        new_lines.append(" ".join(numbers) + "\n")
                    else:
                        new_lines.append(line)
                
                # Write file
                with open(file_path, 'w') as file:
                    file.writelines(new_lines)
                print(f"Changed {filename}")
                
            except Exception as e:
                print(f"Error in {filename}: {str(e)}")

if __name__ == "__main__":
    image_dir = "./dataset/helmet/images"
    label_dir = "./dataset/helmet/labels"
    output_dir = "./dataset/data"
    split_dataset(image_dir, label_dir, output_dir)