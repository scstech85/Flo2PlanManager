import matplotlib.pyplot as plt
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import numpy as np
import skimage.io as io
import pylab
import os

dataDir='Flo2Plan/trainingset'
dataType='images'
train_file='train.json'

annFile = os.path.join(dataDir, train_file)
cocoGt=COCO(annFile)

#initialize COCO detections api
resFile='result.json'

cocoDt=cocoGt.loadRes(os.path.join(dataDir, resFile))

cocoEval = COCOeval(cocoGt,cocoDt, iouType='bbox')
cocoEval.params.maxDets = [100, 100, 100]
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()