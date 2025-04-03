import os
import shutil
import argparse
from PIL import Image
from pathlib import Path

def convert_to_webp(input_path, output_path, backup_path, use_original_names):
    # Create output and backup directories if they don't exist
    os.makedirs(output_path, exist_ok=True)
    os.makedirs(backup_path, exist_ok=True)
    
    # Supported image formats
    supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}
    
    # Get all image files in the input directory
    image_files = []
    for root, _, files in os.walk(input_path):
        for file in files:
            if any(file.lower().endswith(fmt) for fmt in supported_formats):
                image_files.append(os.path.join(root, file))
    
    # Process each image file
    for i, image_path in enumerate(image_files, 1):
        try:
            # Open the image
            with Image.open(image_path) as img:
                # Determine new filename
                if use_original_names:
                    # Use original filename but change extension to .webp
                    original_name = os.path.basename(image_path)
                    new_filename = os.path.splitext(original_name)[0] + '.webp'
                else:
                    # Use sequential number
                    new_filename = f"image{i:03d}.webp"
                
                # Get relative path to maintain directory structure
                rel_path = os.path.relpath(image_path, input_path)
                rel_dir = os.path.dirname(rel_path)
                
                # Create corresponding output and backup directories
                output_dir = os.path.join(output_path, rel_dir)
                backup_dir = os.path.join(backup_path, rel_dir)
                os.makedirs(output_dir, exist_ok=True)
                os.makedirs(backup_dir, exist_ok=True)
                
                # Save as WebP
                output_file = os.path.join(output_dir, new_filename)
                img.save(output_file, 'WEBP', quality=90)
                
                # Copy original to backup
                backup_file = os.path.join(backup_dir, os.path.basename(image_path))
                shutil.copy2(image_path, backup_file)
                
                print(f"Converted: {image_path} -> {output_file}")
                print(f"Backed up: {backup_file}")
                
        except Exception as e:
            print(f"Error processing {image_path}: {str(e)}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert images to WebP format')
    parser.add_argument('input_dir', help='Input directory containing images to convert')
    parser.add_argument('--output-dir', help='Output directory for WebP images (default: input_dir_webp)')
    parser.add_argument('--backup-dir', help='Backup directory for original images (default: input_dir_backup)')
    parser.add_argument('--use-original-names', action='store_true', 
                      help='Use original filenames instead of sequential numbers')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Get absolute path of input directory
    input_path = os.path.abspath(args.input_dir)
    
    # Set default output and backup directories if not provided
    if args.output_dir:
        output_path = os.path.abspath(args.output_dir)
    else:
        output_path = f"{input_path}_webp"
        
    if args.backup_dir:
        backup_path = os.path.abspath(args.backup_dir)
    else:
        backup_path = f"{input_path}_backup"
    
    # Convert images
    convert_to_webp(input_path, output_path, backup_path, args.use_original_names)
    print("Conversion complete!") 