# Cut Image to Smalls by Size

## Purpose

This script is designed to cut the image to small ones with speicial size.

The cut begins from left/top pixels and scan from left/top to right/bottom.

To make the right/bottom pixels are included in the result, add additional scan from right/bottom to left/top in one col/row.

![raw](/in/own_example.jpg)

Result

![raw](/out/rgb_00000.jpg) ![raw](/out/rgb_00004.jpg) ![raw](/out/rgb_00008.jpg)

![raw](/out/rgb_00001.jpg) ![raw](/out/rgb_00005.jpg) ![raw](/out/rgb_00009.jpg)

![raw](/out/rgb_00002.jpg) ![raw](/out/rgb_00006.jpg) ![raw](/out/rgb_00010.jpg)

![raw](/out/rgb_00003.jpg) ![raw](/out/rgb_00007.jpg) ![raw](/out/rgb_00011.jpg)

## Install Package
```
python -m venv ut
source ut/bin/activate
pip install -r requirements.txt
```

## Run Example

```
python cut_img.py
```

## Change for Customer Images

```
    in_folder = 'in'        //Put input images
    in_file_type = "jpg"    //Input image extension type
    out_folder = "out"      //Output folder
    out_prefx = 'rgb_'      //Output image's prefix
    out_h = 50              //Output image height
    out_w = 150             //Output image width
```
