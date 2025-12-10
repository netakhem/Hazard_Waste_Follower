import os
import shutil

main_folder = r"D:\FALL 2025\Intro_to_Robotics\Final_Project\neta310\all_data"
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tif", ".tiff"}

def is_image(filename):
    return os.path.splitext(filename)[1].lower() in IMAGE_EXTS

for subfolder in sorted(os.listdir(main_folder)):
    subfolder_path = os.path.join(main_folder, subfolder)
    if not os.path.isdir(subfolder_path):
        continue

    staging = os.path.join(subfolder_path, "__staging__")
    os.makedirs(staging, exist_ok=True)

    # Move all image files into staging to avoid name collisions
    moved = []
    for filename in sorted(os.listdir(subfolder_path)):
        src = os.path.join(subfolder_path, filename)
        if not os.path.isfile(src) or not is_image(filename):
            continue
        dst = os.path.join(staging, filename)
        # Ensure unique name in staging
        if os.path.exists(dst):
            base, ext = os.path.splitext(filename)
            i = 1
            while True:
                candidate = os.path.join(staging, f"{base}__m{i}{ext}")
                if not os.path.exists(candidate):
                    dst = candidate
                    break
                i += 1
        shutil.move(src, dst)
        moved.append(dst)

    # Rename sequentially while moving back from staging
    counter = 1
    for temp_path in sorted(os.listdir(staging)):
        src = os.path.join(staging, temp_path)
        if not os.path.isfile(src):
            continue
        ext = os.path.splitext(src)[1]
        new_name = f"{subfolder}_{counter:03d}{ext}"
        dest = os.path.join(subfolder_path, new_name)
        # Guarantee uniqueness (shouldn’t collide since parent is empty of images now)
        i = 1
        while os.path.exists(dest):
            dest = os.path.join(subfolder_path, f"{subfolder}_{counter:03d}__v{i}{ext}")
            i += 1
        shutil.move(src, dest)
        counter += 1

    # Remove staging if empty
    try:
        os.rmdir(staging)
    except OSError:
        pass  # leave it if something is still inside (e.g., non-image files)

print("Renaming complete: files are now SubfolderName_001, _002, ... with extensions preserved.")