# Flo<sup>2</sup>Plan Dataset Manager
***Flo***rence ***Flo***or Plan is an image dataset for ORF competition (). 
This tool is useful to manage the dataset and evaluate the results.


Requirements
------------
- Anaconda 3
- COCO Tools

Installation
------------
**Anaconda**

You need install [Anaconda](https://www.continuum.io/downloads), then run below:

```bash

# python3

conda create --name flo2 python=3.6
source activate flo2
#pycocotools (https://github.com/cocodataset/cocoapi/tree/master/PythonAPI)
conda install -c hcc pycocotools
```
Usage
-----

**Download images**

You can find the list of image files on the competion website as a JSON file. Having that JSON file, it is possible to download the imageset using the next command:
```
#command
./download_dataset.py <json_file> --dir <local_dir>
```
In this repository you can find one JSON file (an example) to try the command.

```
#run the example:
./download_dataset.py example_images.json --dir .
```

In this way you can download the images and create the dataset directories inside your local path.
In your local path you will find a directory named **Flo2Plan**:
```
# list of files
./Flo2Plan
./Flo2Plan/Images
./Flo2Plan/Images/G0375.png
./Flo2Plan/Images/G0423.png
./Flo2Plan/Images/G0592.png
./Flo2Plan/output.json
```
The file named **output.json** contains all the information about each downloaded images
```
#output.json
[
  {
    "key": "G0592",
    "image_mode": "RGB",
    "result": "OK"
  },
  {
    "key": "G0375",
    "image_mode": "RGB",
    "result": "OK"
  },
  {
    "key": "G0423",
    "image_mode": "P",
    "result": "OK"
  }
]
```
Each file has a **key**, the downloading result (**result**) and other information related to the original URL image path. 
The values for result are **OK** or **KO**. If you find some items where result is **KO** this means 
you cannot download the related file from the specific URL. In this case, please contact us.

**Visualize Instances**

It is possible to visualize the instances on image using the following script:
```
#visualize
./visual_instances_image.py <instances_json_file> --img_dir <image_dir_path> --key <image_key>
```
The key_img is the image key which you can find inside the JSON file to download files (example: example_image.json).
If you use the key_img as ALL you can create a local directory where the script will save the overlayed image with instance masks.
Otherwise, if key_img is empy, the script will sample a random key from the ground truth.
```
#random image from dataset
./visual_instances_image.py example_instances.json --img_dir Flo2Plan/trainingset/images
```

```
#image with key G0423
/visual_instances_image.py example_instances.json --img_dir Flo2Plan/trainingset/images --key G0423
```

```
#salve all the overlayed images in local directory
/visual_instances_image.py example_instances.json --img_dir Flo2Plan/trainingset/images --key ALL --save_path local
```

**Evaluate results**  
In order to evaluate your results, you can use the following script:
```
#evaluate
./evaluation_results.py ....... ??? ......
```
coming soon