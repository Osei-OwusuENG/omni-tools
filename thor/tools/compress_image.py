#import needed libraries
from PIL import Image
import os
import argparse


# create compress image function
def compress_image(input_path, output_path, quality=65):

    try:
        #open image file
        with Image.open(input_path) as img:

            # check for the type of image | jpeg, jpg, png, webp
            ext = os.open.splitext(output_path)[1].lower()

            # compress jpeg and jpg
            if ext in ['.jpeg', '.jpg']:

                if img.mode in ('RGBA', 'P'):
                    
                    img = img.convert('RGB')
                
                # save compress file
                img.save(output_path, 'JPEG', optimize=True, quality=quality)
            
            # comress png image file
            elif ext == '.png':
                #save compress file

                img.save(output_path, 'PNG', compress_level=9)

            # comress webp image files
            elif ext == '.webp':

                #save compress file
                img.save(output_path, 'webp', optimize=True)
            
            else:
                img.save(output_path, quality=quality)
    
    except Exception as e:
        print(f'error{e}')


        print(f'Done compressing of {input_path} -> {output_path}')
        print(f'compressed by {(1-os.path.getsize(output_path)/os.path.getsize(input_path))*100}')



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='A simple command line compress file')
    parser.add_argument('input', help='enter the file name to be compress')
    parser.add_argument('output', help='enter the file name compressed file should be saved in')
    parser.add_argument('-q', '--quality', help='enter the amount you want to compress by', default=65)

    arg = parser.parse_args()

    compress_image(arg.input, arg.output, arg.quality)

