from pycocotools.coco import COCO
import numpy as np
import skimage.io as io

import os



class ManageCOCO:
    def __init__(self, json_path, image_path):
        self.coco = COCO(json_path)
        self.image_path = image_path

    def getImageIds(self):
        imgIds = self.coco.getImgIds()
        return imgIds

    def searchByKey(self, key):
        ids = self.getImageIds()
        for img in self.coco.loadImgs(ids):
            k = img['file_name'].split('.')[0]
            if k == key:
                return img['id']
        raise Exception('Key %s: not valid'%(key))

    def getImagePath(self,img_id):
        img = self.coco.loadImgs([img_id])[0]
        return os.path.join(self.image_path, img['file_name'])

    def getImageAnnotations(self,img_id):
        img_path = self.getImagePath(img_id)

        annIds = self.coco.getAnnIds(imgIds=[img_id], iscrowd=None)

        anns = self.coco.loadAnns(annIds)
        new_anns = []
        for ann in anns:
            cat_id = ann['category_id']
            ann['category_name'] = self.getCategoryName(cat_id)

            new_anns.append(ann)


        return img_path, new_anns

    def getCategoryName(self, id_cat):
        cat = self.coco.loadCats([id_cat])[0]
        return cat['name']

    def getCategories(self):
        return self.coco.getCatIds()

    def getColorCategories(self):
        colors = {}
        for i in self.getCategories():
            c = (np.random.random((1, 3)) * 0.6 + 0.4)[0]

            colors[i] = (c * 255).astype(np.int)
            #print('--',colors[i])
        return colors

from PIL import Image, ImageDraw

def visual(img_path, anns, colors, show=False):

    image = Image.open(img_path).convert('RGBA')
    layer = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(layer)
    #eX, eY = 500, 150  # Size of Bounding Box for rectangle
    #bbox = (500, 600, 0, 750)  # endwidth,startheight,startwidth,endheight
    #draw.rectangle(bbox, fill=(255, 0, 0, 180))



    for ann in anns:
        category_name = ann['category_name']
        for seg in ann['segmentation']:
            poly = np.array(seg,dtype=np.int).reshape((int(len(seg) / 2), 2))
            #print(category_name, poly, poly.shape)
            c = colors[ann['category_id']]
            #print('col', c)
            #poly = np.array(seg).reshape((int(len(seg) / 2), 2))
            draw.polygon([(x,y) for x, y in poly],
                          fill=(c[0], c[1], c[2], 127), outline=(c[0], c[1], c[2], 255))

    image = Image.alpha_composite(image, layer)
    if show:
        image.show()

    return image