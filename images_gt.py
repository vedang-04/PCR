import glob
import json
# import fiftyone as fo
import numpy

ff = {}
list_of_files = glob.glob(r'C:\Users\kshir\OneDrive\Desktop\PCR-master\MSRA-TD500\train\*.gt')
list_of_files_seg = glob.glob(r'C:\Users\kshir\OneDrive\Desktop\PCR-master\MSRA-TD500\train\*.txt')

list_of_images = glob.glob(r'C:\Users\kshir\OneDrive\Desktop\PCR-master\MSRA-TD500\train\*.jpg')
list_of_dict = []

# Ex: your custom label format
annotations = []
for i in range(len(list_of_images)):
    file = open(list_of_files[i], 'r')
    file_seg = open(list_of_files_seg[i], 'r')
    text = file.read()
    text_seg = file_seg.read()
    list_text = text.split('\n', )
    list_seg = text_seg.split('\n', )
    cl = []
    lb = []
    for cord in list_seg:
        cord_split = cord.split(',', )
        if len(cord_split[0]) != 0:
            cord_list = []
            for c in cord_split:
                if c[-1] != 't':
                    cord_list.append(int(c))
                else:
                    lb.append(c)
            cl.append(cord_list)
    assert len(cl) == len(lb)
    li = []
    for t in list_text:
        vals = t.split(' ', )
        if len(t) != 0:
            area = int(float(vals[4]) * float(vals[5]))
            d1 = {"bbox": [int(vals[2]), int(vals[3]), int(float(vals[2]) + float(vals[4])),
                           int(float(vals[3]) + float(vals[5]))],
                  "iscrowd": int(vals[1]), "area": area}
            li.append(d1)
    for j in range(len(li)):
        li[j]['segmentation'] = [cl[j]]
        li[j]['label'] = 'text'
        li[j]['id'] = i + 1
        if lb[j] == 'text':
            li[j]['category_id'] = 0
        else:
            li[j]['category_id'] = 0
    annotations.extend(li)

print(len(annotations))

null = None

ff = {"info": {"year": "", "version": "", "description": "Exported from FiftyOne", "contributor": "",
               "url": "https://voxel51.com/fiftyone", "date_created": "2022-03-16T16:50:23"}, "licenses": [],
      "categories": [{"id": 0, "name": "text", "supercategory": null},
                     {"id": 1, "name": "no_text", "supercategory": null}],
      "images": [
          {"id": 1, "file_name": "IMG_0030-2.JPG", "height": 1152, "width": 1728, "license": null, "coco_url": null},
          {"id": 2, "file_name": "IMG_0063-2.JPG", "height": 1280, "width": 1920, "license": null, "coco_url": null},
          {"id": 3, "file_name": "IMG_0064-2.JPG", "height": 1280, "width": 1920, "license": null, "coco_url": null},
          {"id": 4, "file_name": "IMG_0081-2.JPG", "height": 1280, "width": 1920, "license": null, "coco_url": null},
          {"id": 5, "file_name": "IMG_0155-2.JPG", "height": 864, "width": 1296, "license": null, "coco_url": null},
          {"id": 6, "file_name": "IMG_0183-2.JPG", "height": 864, "width": 1296, "license": null, "coco_url": null},
          {"id": 7, "file_name": "IMG_0451-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 8, "file_name": "IMG_0452-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 9, "file_name": "IMG_0455-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 10, "file_name": "IMG_0456-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 11, "file_name": "IMG_0457-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 12, "file_name": "IMG_0463-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 13, "file_name": "IMG_0469-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 14, "file_name": "IMG_0472-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 15, "file_name": "IMG_0476-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 16, "file_name": "IMG_0479-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 17, "file_name": "IMG_0481-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 18, "file_name": "IMG_0486-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 19, "file_name": "IMG_0487-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 20, "file_name": "IMG_0489-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 21, "file_name": "IMG_0495-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 22, "file_name": "IMG_0496-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 23, "file_name": "IMG_0497-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 24, "file_name": "IMG_0504-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 25, "file_name": "IMG_0506-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 26, "file_name": "IMG_0511-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 27, "file_name": "IMG_0514-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 28, "file_name": "IMG_0515-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 29, "file_name": "IMG_0518-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 30, "file_name": "IMG_0523-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 31, "file_name": "IMG_0530-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 32, "file_name": "IMG_0531-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 33, "file_name": "IMG_0541-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 34, "file_name": "IMG_0570-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 35, "file_name": "IMG_0571-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 36, "file_name": "IMG_0577-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 37, "file_name": "IMG_0582-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 38, "file_name": "IMG_0594-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 39, "file_name": "IMG_0595-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 40, "file_name": "IMG_0596-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 41, "file_name": "IMG_0597-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 42, "file_name": "IMG_0601-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 43, "file_name": "IMG_0602-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 44, "file_name": "IMG_0603-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 45, "file_name": "IMG_0605-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 46, "file_name": "IMG_0608-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 47, "file_name": "IMG_0611-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 48, "file_name": "IMG_0613-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 49, "file_name": "IMG_0617-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 50, "file_name": "IMG_0620-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 51, "file_name": "IMG_0621-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 52, "file_name": "IMG_0626-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 53, "file_name": "IMG_0628-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 54, "file_name": "IMG_0633-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 55, "file_name": "IMG_0635-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 56, "file_name": "IMG_0649-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 57, "file_name": "IMG_0650-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 58, "file_name": "IMG_0652-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 59, "file_name": "IMG_0653-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 60, "file_name": "IMG_0655-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 61, "file_name": "IMG_0656-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 62, "file_name": "IMG_0658-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 63, "file_name": "IMG_0660-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 64, "file_name": "IMG_0664-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 65, "file_name": "IMG_0665-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 66, "file_name": "IMG_0669-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 67, "file_name": "IMG_0686-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 68, "file_name": "IMG_0687-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 69, "file_name": "IMG_0690-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 70, "file_name": "IMG_0692-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 71, "file_name": "IMG_0694-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 72, "file_name": "IMG_0697-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 73, "file_name": "IMG_0700-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 74, "file_name": "IMG_0702-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 75, "file_name": "IMG_0704-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 76, "file_name": "IMG_0707-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 77, "file_name": "IMG_0709-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 78, "file_name": "IMG_0719-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 79, "file_name": "IMG_0722-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 80, "file_name": "IMG_0723-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 81, "file_name": "IMG_0726-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 82, "file_name": "IMG_0728-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 83, "file_name": "IMG_0730-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 84, "file_name": "IMG_0733-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 85, "file_name": "IMG_0735-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 86, "file_name": "IMG_0738-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 87, "file_name": "IMG_0746-2.JPG", "height": 1152, "width": 1728, "license": null, "coco_url": null},
          {"id": 88, "file_name": "IMG_0747-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 89, "file_name": "IMG_0748-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 90, "file_name": "IMG_0750-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 91, "file_name": "IMG_0752-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 92, "file_name": "IMG_0753-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 93, "file_name": "IMG_0758-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 94, "file_name": "IMG_0759-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 95, "file_name": "IMG_0764-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 96, "file_name": "IMG_0769-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 97, "file_name": "IMG_0780-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 98, "file_name": "IMG_0784-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 99, "file_name": "IMG_0787-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 100, "file_name": "IMG_0791-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 101, "file_name": "IMG_0792-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 102, "file_name": "IMG_0794-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 103, "file_name": "IMG_0795-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 104, "file_name": "IMG_0809-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 105, "file_name": "IMG_0810-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 106, "file_name": "IMG_0812-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 107, "file_name": "IMG_0814-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 108, "file_name": "IMG_0815-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 109, "file_name": "IMG_0818-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 110, "file_name": "IMG_0821-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 111, "file_name": "IMG_0826-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 112, "file_name": "IMG_0827-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 113, "file_name": "IMG_0840-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 114, "file_name": "IMG_0842-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 115, "file_name": "IMG_0845-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 116, "file_name": "IMG_0848-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 117, "file_name": "IMG_0849-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 118, "file_name": "IMG_0850-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 119, "file_name": "IMG_0855-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 120, "file_name": "IMG_0858-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 121, "file_name": "IMG_0859-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 122, "file_name": "IMG_0861-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 123, "file_name": "IMG_0864-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 124, "file_name": "IMG_0865-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 125, "file_name": "IMG_0868-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 126, "file_name": "IMG_0870-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 127, "file_name": "IMG_0873-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 128, "file_name": "IMG_0884-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 129, "file_name": "IMG_0885-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 130, "file_name": "IMG_0890-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 131, "file_name": "IMG_0892-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 132, "file_name": "IMG_0893-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 133, "file_name": "IMG_0896-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 134, "file_name": "IMG_0899-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 135, "file_name": "IMG_0903-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 136, "file_name": "IMG_0907-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 137, "file_name": "IMG_0910-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 138, "file_name": "IMG_0916-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 139, "file_name": "IMG_0917-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 140, "file_name": "IMG_0918-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 141, "file_name": "IMG_1539-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 142, "file_name": "IMG_1540-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 143, "file_name": "IMG_1544-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 144, "file_name": "IMG_1545-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 145, "file_name": "IMG_1547-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 146, "file_name": "IMG_1549-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 147, "file_name": "IMG_1550-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 148, "file_name": "IMG_1553-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 149, "file_name": "IMG_1558-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 150, "file_name": "IMG_1561-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 151, "file_name": "IMG_1562-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 152, "file_name": "IMG_1567-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 153, "file_name": "IMG_1569-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 154, "file_name": "IMG_1570-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 155, "file_name": "IMG_1571-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 156, "file_name": "IMG_1572-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 157, "file_name": "IMG_1576-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 158, "file_name": "IMG_1579-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 159, "file_name": "IMG_1582-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 160, "file_name": "IMG_1586-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 161, "file_name": "IMG_1591-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 162, "file_name": "IMG_1592-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 163, "file_name": "IMG_1593-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 164, "file_name": "IMG_1595-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 165, "file_name": "IMG_1596-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 166, "file_name": "IMG_1600-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 167, "file_name": "IMG_1601-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 168, "file_name": "IMG_1614-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 169, "file_name": "IMG_1615-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 170, "file_name": "IMG_1616-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 171, "file_name": "IMG_1619-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 172, "file_name": "IMG_1625-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 173, "file_name": "IMG_1629-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 174, "file_name": "IMG_1641-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 175, "file_name": "IMG_1645-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 176, "file_name": "IMG_1667-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 177, "file_name": "IMG_1672-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 178, "file_name": "IMG_1673-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 179, "file_name": "IMG_1676-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 180, "file_name": "IMG_1677-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 181, "file_name": "IMG_1678-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 182, "file_name": "IMG_1683-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 183, "file_name": "IMG_1685-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 184, "file_name": "IMG_1687-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 185, "file_name": "IMG_1688-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 186, "file_name": "IMG_1692-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 187, "file_name": "IMG_1701-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 188, "file_name": "IMG_1705-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 189, "file_name": "IMG_1709-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 190, "file_name": "IMG_1712-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 191, "file_name": "IMG_1714-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 192, "file_name": "IMG_1719-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 193, "file_name": "IMG_1723-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 194, "file_name": "IMG_1724-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 195, "file_name": "IMG_1725-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 196, "file_name": "IMG_1730-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 197, "file_name": "IMG_1736-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 198, "file_name": "IMG_1748-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 199, "file_name": "IMG_1753-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 200, "file_name": "IMG_1754-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 201, "file_name": "IMG_1756-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 202, "file_name": "IMG_1758-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 203, "file_name": "IMG_1760-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 204, "file_name": "IMG_1761-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 205, "file_name": "IMG_1763-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 206, "file_name": "IMG_1768-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 207, "file_name": "IMG_1770-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 208, "file_name": "IMG_1771-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 209, "file_name": "IMG_1778-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 210, "file_name": "IMG_1783-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 211, "file_name": "IMG_1785-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 212, "file_name": "IMG_1786-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 213, "file_name": "IMG_1797-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 214, "file_name": "IMG_1799-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 215, "file_name": "IMG_1805-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 216, "file_name": "IMG_1808-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 217, "file_name": "IMG_1809-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 218, "file_name": "IMG_1815-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 219, "file_name": "IMG_1817-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 220, "file_name": "IMG_1822-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 221, "file_name": "IMG_1823-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 222, "file_name": "IMG_1824-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 223, "file_name": "IMG_1826-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 224, "file_name": "IMG_1832-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 225, "file_name": "IMG_1835-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 226, "file_name": "IMG_1862-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 227, "file_name": "IMG_1866-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 228, "file_name": "IMG_1872-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 229, "file_name": "IMG_1883-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 230, "file_name": "IMG_1904-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 231, "file_name": "IMG_1905-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 232, "file_name": "IMG_1916-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 233, "file_name": "IMG_1920-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 234, "file_name": "IMG_1922-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 235, "file_name": "IMG_1935-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 236, "file_name": "IMG_1939-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 237, "file_name": "IMG_1941-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 238, "file_name": "IMG_1946-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 239, "file_name": "IMG_1947-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 240, "file_name": "IMG_1949-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 241, "file_name": "IMG_1951-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 242, "file_name": "IMG_1955-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 243, "file_name": "IMG_1957-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 244, "file_name": "IMG_1960-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 245, "file_name": "IMG_1965-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 246, "file_name": "IMG_1966-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 247, "file_name": "IMG_1967-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 248, "file_name": "IMG_1971-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 249, "file_name": "IMG_1975-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 250, "file_name": "IMG_1977-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 251, "file_name": "IMG_1983-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 252, "file_name": "IMG_1986-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 253, "file_name": "IMG_1989-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 254, "file_name": "IMG_1991-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 255, "file_name": "IMG_1995-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 256, "file_name": "IMG_2011-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 257, "file_name": "IMG_2014-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 258, "file_name": "IMG_2024-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 259, "file_name": "IMG_2028-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 260, "file_name": "IMG_2029-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 261, "file_name": "IMG_2031-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 262, "file_name": "IMG_2040-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 263, "file_name": "IMG_2046-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 264, "file_name": "IMG_2049-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 265, "file_name": "IMG_2051-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 266, "file_name": "IMG_2055-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 267, "file_name": "IMG_2060-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 268, "file_name": "IMG_2062-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 269, "file_name": "IMG_2075-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 270, "file_name": "IMG_2077-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 271, "file_name": "IMG_2078-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 272, "file_name": "IMG_2080-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 273, "file_name": "IMG_2081-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 274, "file_name": "IMG_2083-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 275, "file_name": "IMG_2085-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 276, "file_name": "IMG_2086-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 277, "file_name": "IMG_2088-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 278, "file_name": "IMG_2091-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 279, "file_name": "IMG_2093-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 280, "file_name": "IMG_2097-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 281, "file_name": "IMG_2100-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 282, "file_name": "IMG_2101-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 283, "file_name": "IMG_2103-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 284, "file_name": "IMG_2112-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 285, "file_name": "IMG_2113-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 286, "file_name": "IMG_2124-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 287, "file_name": "IMG_2127-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 288, "file_name": "IMG_2130-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 289, "file_name": "IMG_2160-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 290, "file_name": "IMG_2163-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 291, "file_name": "IMG_2165-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 292, "file_name": "IMG_2172-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 293, "file_name": "IMG_2174-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 294, "file_name": "IMG_2184-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 295, "file_name": "IMG_2199-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 296, "file_name": "IMG_2205-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 297, "file_name": "IMG_2208-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 298, "file_name": "IMG_2213-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 299, "file_name": "IMG_2222-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 300, "file_name": "IMG_2224-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null}],
      'annotations': annotations}

for d1 in ff.get('images'):
    if '-2' in d1.get('file_name'):
        s = d1.get('file_name')
        s = s.replace('-2', '')
        d1['file_name'] = s

c = 0
i = 0
lid = [1]
iid = []
fil = []
k = 0

print(len(ff.get('images')))

while i < len(ff.get('annotations')):
    if ff.get('annotations')[i].get('id') == lid[-1]:
        c = c + 1
        i = i + 1
    else:
        if c == 0:
            print(ff.get('annotations')[i].get('id'))
        assert c != 0
        for j in range(c):
            fil.append(ff.get('images')[k])
        if (ff.get('annotations')[i].get('id') == 58) | (ff.get('annotations')[i].get('id') == 159) | (
                ff.get('annotations')[i].get('id') == 88) | (ff.get('annotations')[i].get('id') == 63) | (
                ff.get('annotations')[i].get('id') == 171) | (ff.get('annotations')[i].get('id') == 254):
            lid.append(lid[-1] + 2)
            k = k + 2
        else:
            lid.append(lid[-1] + 1)
            k = k + 1
        c = 0
fil.append({"id": 300, "file_name": "IMG_2224.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null})

lf = len(fil)
print(lf)
filf = []
fa = []

for i in range(lf):
    d = fil[i]
    d1 = d.copy()
    d1['id'] = i + 1
    filf.append(d1)
    d2 = annotations[i]
    d3 = d2.copy()
    d3['id'] = i + 1
    fa.append(d3)

ff1 = {"info": {"year": "", "version": "", "description": "Exported from FiftyOne", "contributor": "",
                "url": "https://voxel51.com/fiftyone", "date_created": "2022-03-16T16:50:23"}, "licenses": [],
       "categories": ff.get('categories'),
       'images': filf, 'annotations': fa}

json_object = json.dumps(ff1)
with open("msra_train_instance.json", "w") as outfile:
    json.dump(ff1, outfile)
