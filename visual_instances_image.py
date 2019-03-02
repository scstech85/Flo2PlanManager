#!/usr/bin/env python
import argparse
import numpy as np
from  manager.visual import ManageCOCO, visual

def run(json_path, img_path, key=None):
    manager = ManageCOCO(json_path, img_path)
    ids = manager.getImageIds()
    colors = manager.getColorCategories()
    if key is None:
        idx = np.random.randint(0, len(ids))
    else:
        idx = manager.searchByKey(key)

    p, ann = manager.getImageAnnotations(idx)

    print('Image path:', p)

    visual(p, ann, colors, show=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename', nargs='?', help='instance dataset json file')
    parser.add_argument('-I', '--img_dir', default='.', help='images directory')
    parser.add_argument('-K', '--key_img', default=None, help='search by key')
    args = parser.parse_args()

    filename = args.filename
    img_dir = args.img_dir

    run(filename, img_dir)

