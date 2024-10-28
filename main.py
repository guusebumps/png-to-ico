import os
from PIL import Image

def convert_png_to_ico(input_folder="pngs", output_folder="converted_icons", icon_sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)]):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    log_file_path = "converted_files.txt"

    with open(log_file_path, "w") as log_file:
        for file_name in os.listdir(input_folder):
            if file_name.lower().endswith(".png"):
                png_file_path = os.path.join(input_folder, file_name)
                try:
                    img = Image.open(png_file_path)
                    if img.mode != 'RGBA':
                        img = img.convert('RGBA')
                    icon_file_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.ico')
                    img.save(icon_file_path, format='ICO', sizes=icon_sizes)
                    log_file.write(f"{file_name} -> {icon_file_path}\n")
                    print(f"Converted {file_name} to {icon_file_path}")
                except Exception as e:
                    print(f"Error converting {file_name} to ICO: {e}")

    print(f"Conversion complete. Check {log_file_path} for details.")

convert_png_to_ico()
