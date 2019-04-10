#!/usr/bin/env python
import argparse
import numpy as np
from  manager.visual import ManageCOCO, visual
import os
import shutil
def run(json_path, img_path, key=None, show=True, save_file=False, save_path='local', type='segmentation'):


    manager = ManageCOCO(json_path, img_path)
    ids = manager.getImageIds()
    colors = manager.getColorCategories()
    if key is None:
        idx = [np.random.randint(0, len(ids))]
    elif key == 'ALL':
        idx = ids
        show = False
        save_file = True
    else:
        idx = [manager.searchByKey(key)]


    if save_file:
        if os.path.isdir(save_path):
            shutil.rmtree(save_path)
        os.makedirs(save_path)

    for id in idx:
        p, ann = manager.getImageAnnotations(id)

        print('Image path:', p)

        im = visual(p, ann, colors, show=show, type=type)
        if save_file:
            a, b = os.path.split(p)
            fpath = os.path.join(save_path, b)
            print('save overlayed image:', fpath)
            im.save(fpath)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename', nargs='?', help='instance dataset json file')
    parser.add_argument('-I', '--img_dir', default='.', help='images directory')
    parser.add_argument('-K', '--key_img', default=None, help='search by key')
    parser.add_argument('-S', '--show', default=True, help='show image')
    parser.add_argument('-W', '--save_file', default=False, help='show image')
    parser.add_argument('-D', '--save_path', default='local', help='local image directory')
    args = parser.parse_args()

    filename = args.filename
    img_dir = args.img_dir
    key = args.key_img

    run(filename, img_dir, key=key, show=args.show, save_file=args.save_file, save_path=args.save_path)

