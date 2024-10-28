# PNG to ICO Converter

This Python script converts PNG files from a specified folder into ICO files with multiple icon sizes. The converted ICO files are saved in a designated output folder, and a log file (`converted_files.txt`) records the details of each conversion.

## Features
- Converts all PNG files in the `pngs` folder to ICO format.
- Saves the converted ICO files in a folder called `converted_icons`.
- Records the conversion details in `converted_files.txt`.

## Requirements
- Python 3.x
- [Pillow](https://pillow.readthedocs.io/) library for image processing.

Install Pillow if not already installed:
```bash
pip install pillow
```

## Usage
1. Place your PNG files in the `pngs` folder.
2. Run the script:
   ```bash
   python convert_png_to_ico.py
   ```
3. The converted ICO files will be saved in the `converted_icons` folder, and `converted_files.txt` will be generated, listing the files that were converted.

## Folder Structure
- **pngs/**: Folder containing PNG files to be converted.
- **converted_icons/**: Folder where ICO files will be saved.
- **converted_files.txt**: Log file listing converted files.

## Example

After running the script:
```
pngs/
├── example1.png
├── example2.png
converted_icons/
├── example1.ico
├── example2.ico
converted_files.txt
```
