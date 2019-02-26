from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import os

dataDir='Flo2Plan/trainingset'
dataType='images'
train_file='train.json'

annFile = os.path.join(dataDir, train_file)
coco=COCO(annFile)

cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))

imgIds = coco.getImgIds();

img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]

I = io.imread(os.path.join(dataDir, dataType, img['file_name']))
plt.axis('off')
plt.imshow(I)
plt.show()

plt.imshow(I); plt.axis('off')
annIds = coco.getAnnIds(imgIds=img['id'], iscrowd=None)
print(annIds)
anns = coco.loadAnns(annIds)
print(anns)
#coco.showAnns(anns, draw_bbox=True)
coco.showAnns(anns)

plt.show()