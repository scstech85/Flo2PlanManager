import json
import os
import shutil
from urllib.request import *
import tempfile


from PIL import Image

#/extra1/student-home/Dropbox/Floorplan/GFPlans/desc.csv


def save(im, dest):
    #png = Image.open(object.logo.path)


    #if im.mode == "RGB" or im.mode == "L":
        #final = im.convert('L')


    if im.mode == 'RGBA':
        im.load()  # required for png.split()
        final = Image.new("RGB", im.size, (255, 255, 255))
        final.paste(im, mask=im.split()[3])  # 3 is the alpha channel
        #final = final.convert('RGB')
    elif  im.mode == 'P':
        final = im.convert('L')
    elif im.mode == 'CMYK':
        final = im.convert('RGB')
    else:
        final = im

    final.save(dest, 'PNG',optimize=True)
    #return im.mode



class ManageData:
    def __init__(self, json_file):
        with open(json_file, 'r') as myfile:
            data = myfile.read()
            self.dataset = json.loads(data)

    def download(self, base_path='.'):

        def download_action(url, tmp_loc_dir):
            req = Request(url, headers=headers)
            raw_img = urlopen(req).read()

            type = url.split('.')[-1]
            if type not in extensions:
                type = "jpg"

            loc_out_file = os.path.join(tmp_loc_dir, 'tmp'+'.'+type)

            print(os.path.isdir(tmp_loc_dir), loc_out_file)

            with open(loc_out_file, 'wb') as f_out:
                f_out.write(raw_img)

            print(loc_out_file, os.path.isfile(loc_out_file))
            im = Image.open(loc_out_file)
            return im

        def save_action(im, images_dir, fpath):

            trg_file = os.path.join(images_dir, fpath)

            # row['fname'] = os.path.join(trg_dir, path)

            print(trg_file)
            save(im, trg_file)


        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

        extensions = {"jpg", "jpeg", "png", "gif"}

        tmp_loc_dir = 'TMP_LOCAL'

        if not os.path.isdir(tmp_loc_dir):
            os.makedirs(tmp_loc_dir)
            print(tmp_loc_dir)

        target, images_dir = self.create_directory(base_path)
        results  = []
        ok = []
        ko = []
        for row in self.dataset['images']:
            url = row['url']
            key = row['key']
            fpath = row['fpath']

            line = {'key':key}



            try:
                #output_img_file = os.path.join(images_dir, fpath)
                #urllib.request.urlretrieve(url, output_img_file)
                im = download_action(url, tmp_loc_dir)
                im_mode = im.mode
                line['image_mode'] = im_mode
                try:
                    save_action(im, images_dir, fpath)
                    line['result'] = 'OK'
                    ok.append(key)
                except Exception as ex:
                    raise ex

            except Exception as ex:
                #print(ex)
                line['result'] = 'KO'
                line['url'] = url
                line['message'] = str(ex)
                ko.append(key)


            print(line)
            results.append(line)

        print('ok', len(ok), 'ko', len(ko))
        if len(ko)>0:
            print('KOs', ko)


        with open(os.path.join(target, 'output.json'), 'w') as fd:
            data = json.dumps(results, indent=2)
            fd.write(data)

        shutil.rmtree(tmp_loc_dir)





    def create_directory(self, base_path):
        name = self.dataset['name']
        type = self.dataset['type']
        target = os.path.join(base_path, name)
        if os.path.isdir(target):
            shutil.rmtree(target)

        target = os.path.join(target, type)
        os.makedirs(target)
        images_dir = os.path.join(target, 'images')
        os.makedirs(images_dir)
        return target, images_dir


#manager = ManageData('/home/scstech/DATASET/DATASET/Flo2PI/training_set_v1.json')

#manager.download()

