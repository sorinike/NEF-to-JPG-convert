import os
import glob
import rawpy
import imageio

def main(source_directory, output_directory):
    os.makedirs(output_directory, exist_ok=True)  # Create output directory if it doesn't exist

    # Search for .NEF and .NEF files recursively
    all_paths = glob.glob(f"{source_directory}/**/*.nef", recursive=True) + glob.glob(f"{source_directory}/**/*.NEF", recursive=True)
    all_paths = list(set(all_paths))  # Remove duplicates

    count = 0
    print("Total Number of Images: ", len(all_paths))

    for path in all_paths:
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
            
            # Handle duplicate filenames by adding a counter
            base_name = os.path.splitext(os.path.basename(path))[0]
            duplicate_count = sum(1 for f in os.listdir(output_directory) if base_name in f)
            new_name = f"{base_name}_{duplicate_count + 1}.jpg"
            jpg_path = os.path.join(output_directory, new_name)
            imageio.imwrite(jpg_path, rgb)
            count += 1

        print(count, '/', len(all_paths))

if __name__ == '__main__':
    source_directory = "E:/picture_nef"  # Input source folder, change it
    output_directory = "F:/picture_jpg"  # Output folder, change it
    main(source_directory, output_directory)
