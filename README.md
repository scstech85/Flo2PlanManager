# Flo2PlanManager
Manage the dataset for the competition

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
conda install -c hcc pycocotools
```
Usage
-----

**Download images**

You need to download from the competion website the JSON file to download the dataset images.

In this repository you can find one JSON file (an example) to try the commands.

```bash
./download_dataset.py example_images.json --dir '.'
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
Each file has a **key**, the downloading result (**result**) and other informations related to the original URL image path. 
The values for result are **OK** or **KO**. If you find some items where result is **KO** this means 
you cannot download the related file from the specific URL. In this case, please contact us to have that images.

**Evaluate results**  
soon