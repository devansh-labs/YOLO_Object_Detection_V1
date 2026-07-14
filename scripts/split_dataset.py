import os
import random
import shutil

# Dataset path
dataset_path = r"D:\YOLO_Dataset"

images_path = os.path.join(dataset_path, "images")
labels_path = os.path.join(dataset_path, "labels")

# Output folders
splits = {
    "train": 0.8,
    "valid": 0.1,
    "test": 0.1
}

# Create folders
for split in splits:
    os.makedirs(os.path.join(dataset_path, split, "images"), exist_ok=True)
    os.makedirs(os.path.join(dataset_path, split, "labels"), exist_ok=True)

# Supported image extensions
extensions = (".jpg", ".jpeg", ".png")

images = [f for f in os.listdir(images_path) if f.lower().endswith(extensions)]

random.seed(42)
random.shuffle(images)

n = len(images)
train_end = int(0.8 * n)
valid_end = train_end + int(0.1 * n)

train_imgs = images[:train_end]
valid_imgs = images[train_end:valid_end]
test_imgs = images[valid_end:]

split_data = {
    "train": train_imgs,
    "valid": valid_imgs,
    "test": test_imgs
}

for split, img_list in split_data.items():
    for img in img_list:
        shutil.copy2(
            os.path.join(images_path, img),
            os.path.join(dataset_path, split, "images", img)
        )

        label = os.path.splitext(img)[0] + ".txt"

        src_label = os.path.join(labels_path, label)

        if os.path.exists(src_label):
            shutil.copy2(
                src_label,
                os.path.join(dataset_path, split, "labels", label)
            )

print("=" * 40)
print("Dataset successfully split!")
print(f"Train: {len(train_imgs)}")
print(f"Valid: {len(valid_imgs)}")
print(f"Test : {len(test_imgs)}")
print("=" * 40)