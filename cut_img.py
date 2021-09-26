import os, sys
import cv2
import glob

def save_img(img, out_folder, out_prefix, out_h, out_w, x, y, idx):
    crop_img = img[y:y+out_h, x:x+out_w]
    img_full_path = "{}/{}{:04d}.jpg".format(out_folder,out_prefix, idx)    
    print("save to {}".format(img_full_path))
    cv2.imwrite(img_full_path, crop_img)
    

def cut_image(idx, in_file, out_folder, out_prefix, out_h, out_w):
    img = cv2.imread(in_file)
    h, w, c=img.shape
    if h<out_h or w< out_w:
        print("in image {} is too smaller than output".format(in_file))
        return

    print("in size", img.shape)
    print("out size", out_h, out_w)    
    x=y=0
    for i in range(int(w/out_w)):
        for j in range(int(h/out_h)):
            x = i*out_w
            y = j*out_h
            save_img(img, out_folder, out_prefix, out_h, out_w, x, y, idx)
            idx += 1
        if h % out_h!=0:
            y = h-out_h
            save_img(img, out_folder, out_prefix, out_h, out_w, x, y, idx)
            idx += 1

    if w % out_w !=0:
        for j in range(int(h/out_h)):
            x = w-out_w
            y = j*out_h
            save_img(img, out_folder, out_prefix, out_h, out_w, x, y, idx)
            idx += 1
        if h % out_h!=0:
            y = h-out_h
            save_img(img, out_folder, out_prefix, out_h, out_w, x, y, idx)
            idx += 1

    return idx

def main():
    in_folder = 'in'
    out_folder = "out"
    out_prefx = 'rgb_'
    out_h = 50
    out_w = 150

    idx = 0
    for in_file in glob.glob('{}/*.jpg'.format(in_folder)):
        idx = cut_image(idx, in_file, out_folder, out_prefx, out_h, out_w)

if __name__=='__main__':    
    main()
