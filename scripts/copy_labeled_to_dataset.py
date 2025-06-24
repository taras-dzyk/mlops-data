import os
import json
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_LABELED = os.path.abspath(os.path.join(BASE_DIR, "../../data-labeled"))
DATA_RAW = os.path.abspath(os.path.join(BASE_DIR, "../../data-raw"))
DATASET = os.path.abspath(os.path.join(BASE_DIR, "../dataset"))

os.makedirs(DATASET, exist_ok=True)

for fname in os.listdir(DATA_LABELED):
    file_path = os.path.join(DATA_LABELED, fname)
    
    if not os.path.isfile(file_path):
        continue

    with open(file_path, "rb") as f:
        start = f.read(4)
        if b"\x00" in start:
            print(f"Пропущено: {fname}")
            continue

    print(f"\nОбробка: {file_path}")


    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        print(f"Пропущено: невалідний JSON: {fname} — {e}")
        continue

    try:
        label = data["result"][0]["value"]["choices"][0]
        raw_image_url = data["task"]["data"]["image"]
        image_name = raw_image_url.split("data-raw/")[-1]
    except (KeyError, IndexError) as e:
        print(f"Пропущено: не знайдено 'choices' або 'image' у {fname}")
        continue


    src_image_path = os.path.join(DATA_RAW, image_name)
    dst_class_dir = os.path.join(DATASET, label)
    dst_image_path = os.path.join(dst_class_dir, image_name)


    if os.path.exists(src_image_path):
        os.makedirs(dst_class_dir, exist_ok=True)
        shutil.copy2(src_image_path, dst_image_path)
        print(f"{image_name} → {label}/")
    else:
        print(f"Зображення не знайдено: {src_image_path}")
