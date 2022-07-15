import glob
import json
import numpy

ff = {}
list_of_files = glob.glob(r'C:\Users\kshir\OneDrive\Desktop\PCR-master\MSRA-TD500\test\*.gt')
list_of_files_seg = glob.glob(r'C:\Users\kshir\OneDrive\Desktop\PCR-master\MSRA-TD500\test\*.txt')

list_of_images = glob.glob(r'C:\Users\kshir\OneDrive\Desktop\PCR-master\MSRA-TD500\test\*.jpg')
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
        # li[j]['image_id'] = j + 1
        if lb[j] == 'text':
            li[j]['category_id'] = 0
        else:
            li[j]['category_id'] = 0
    annotations.extend(li)

null = None

ff = {"info": {"year": "", "version": "", "description": "Exported from FiftyOne", "contributor": "",
               "url": "https://voxel51.com/fiftyone",
               "date_created": "2022-03-16T17:05:23"}, "licenses": [],
      "categories": [{"id": 0, "name": "text", "supercategory": null},
                     {"id": 1, "name": "no_text", "supercategory": null}],
      "images": [
          {"id": 1, "file_name": "IMG_0059-2.JPG", "height": 1280, "width": 1920, "license": null, "coco_url": null},
          {"id": 2, "file_name": "IMG_0080-2.JPG", "height": 1280, "width": 1920, "license": null, "coco_url": null},
          {"id": 3, "file_name": "IMG_0103-2.JPG", "height": 864, "width": 1296, "license": null, "coco_url": null},
          {"id": 4, "file_name": "IMG_0156-2.JPG", "height": 864, "width": 1296, "license": null, "coco_url": null},
          {"id": 5, "file_name": "IMG_0158-2.JPG", "height": 864, "width": 1296, "license": null, "coco_url": null},
          {"id": 6, "file_name": "IMG_0172-2.JPG", "height": 864, "width": 1296, "license": null, "coco_url": null},
          {"id": 7, "file_name": "IMG_0445-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 8, "file_name": "IMG_0449-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 9, "file_name": "IMG_0461-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 10, "file_name": "IMG_0462-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 11, "file_name": "IMG_0468-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 12, "file_name": "IMG_0475-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 13, "file_name": "IMG_0477-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 14, "file_name": "IMG_0478-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 15, "file_name": "IMG_0482-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 16, "file_name": "IMG_0485-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 17, "file_name": "IMG_0491-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 18, "file_name": "IMG_0505-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 19, "file_name": "IMG_0507-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 20, "file_name": "IMG_0509-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 21, "file_name": "IMG_0513-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 22, "file_name": "IMG_0520-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 23, "file_name": "IMG_0521-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 24, "file_name": "IMG_0545-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 25, "file_name": "IMG_0554-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 26, "file_name": "IMG_0592-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 27, "file_name": "IMG_0599-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 28, "file_name": "IMG_0604-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 29, "file_name": "IMG_0607-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 30, "file_name": "IMG_0610-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 31, "file_name": "IMG_0612-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 32, "file_name": "IMG_0616-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 33, "file_name": "IMG_0625-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 34, "file_name": "IMG_0638-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 35, "file_name": "IMG_0659-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 36, "file_name": "IMG_0666-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 37, "file_name": "IMG_0667-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 38, "file_name": "IMG_0668-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 39, "file_name": "IMG_0670-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 40, "file_name": "IMG_0671-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 41, "file_name": "IMG_0672-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 42, "file_name": "IMG_0675-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 43, "file_name": "IMG_0678-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 44, "file_name": "IMG_0680-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 45, "file_name": "IMG_0698-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 46, "file_name": "IMG_0711-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 47, "file_name": "IMG_0714-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 48, "file_name": "IMG_0716-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 49, "file_name": "IMG_0721-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 50, "file_name": "IMG_0739-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 51, "file_name": "IMG_0742-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 52, "file_name": "IMG_0745-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 53, "file_name": "IMG_0760-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 54, "file_name": "IMG_0763-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 55, "file_name": "IMG_0765-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 56, "file_name": "IMG_0770-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 57, "file_name": "IMG_0779-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 58, "file_name": "IMG_0781-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 59, "file_name": "IMG_0790-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 60, "file_name": "IMG_0793-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 61, "file_name": "IMG_0799-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 62, "file_name": "IMG_0802-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 63, "file_name": "IMG_0803-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 64, "file_name": "IMG_0807-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 65, "file_name": "IMG_0820-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 66, "file_name": "IMG_0829-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 67, "file_name": "IMG_0830-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 68, "file_name": "IMG_0831-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 69, "file_name": "IMG_0833-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 70, "file_name": "IMG_0836-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 71, "file_name": "IMG_0839-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 72, "file_name": "IMG_0844-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 73, "file_name": "IMG_0846-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 74, "file_name": "IMG_0851-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 75, "file_name": "IMG_0866-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 76, "file_name": "IMG_0875-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 77, "file_name": "IMG_0886-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 78, "file_name": "IMG_0887-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 79, "file_name": "IMG_0888-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 80, "file_name": "IMG_0891-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 81, "file_name": "IMG_0898-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 82, "file_name": "IMG_0912-2.JPG", "height": 1296, "width": 1728, "license": null, "coco_url": null},
          {"id": 83, "file_name": "IMG_1543-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 84, "file_name": "IMG_1546-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 85, "file_name": "IMG_1556-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 86, "file_name": "IMG_1557-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 87, "file_name": "IMG_1563-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 88, "file_name": "IMG_1564-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 89, "file_name": "IMG_1568-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 90, "file_name": "IMG_1578-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 91, "file_name": "IMG_1581-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 92, "file_name": "IMG_1587-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 93, "file_name": "IMG_1598-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 94, "file_name": "IMG_1599-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 95, "file_name": "IMG_1605-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 96, "file_name": "IMG_1607-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 97, "file_name": "IMG_1620-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 98, "file_name": "IMG_1621-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 99, "file_name": "IMG_1626-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 100, "file_name": "IMG_1627-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 101, "file_name": "IMG_1628-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 102, "file_name": "IMG_1646-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 103, "file_name": "IMG_1652-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 104, "file_name": "IMG_1654-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 105, "file_name": "IMG_1657-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 106, "file_name": "IMG_1668-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 107, "file_name": "IMG_1671-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 108, "file_name": "IMG_1674-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 109, "file_name": "IMG_1675-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 110, "file_name": "IMG_1679-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 111, "file_name": "IMG_1689-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 112, "file_name": "IMG_1691-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 113, "file_name": "IMG_1696-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 114, "file_name": "IMG_1699-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 115, "file_name": "IMG_1706-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 116, "file_name": "IMG_1715-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 117, "file_name": "IMG_1718-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 118, "file_name": "IMG_1721-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 119, "file_name": "IMG_1722-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 120, "file_name": "IMG_1726-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 121, "file_name": "IMG_1729-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 122, "file_name": "IMG_1732-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 123, "file_name": "IMG_1749-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 124, "file_name": "IMG_1751-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 125, "file_name": "IMG_1757-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 126, "file_name": "IMG_1764-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 127, "file_name": "IMG_1766-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 128, "file_name": "IMG_1767-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 129, "file_name": "IMG_1772-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 130, "file_name": "IMG_1789-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 131, "file_name": "IMG_1791-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 132, "file_name": "IMG_1800-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 133, "file_name": "IMG_1802-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 134, "file_name": "IMG_1806-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 135, "file_name": "IMG_1811-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 136, "file_name": "IMG_1814-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 137, "file_name": "IMG_1825-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 138, "file_name": "IMG_1836-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 139, "file_name": "IMG_1839-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 140, "file_name": "IMG_1846-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 141, "file_name": "IMG_1864-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 142, "file_name": "IMG_1865-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 143, "file_name": "IMG_1867-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 144, "file_name": "IMG_1869-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 145, "file_name": "IMG_1903-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 146, "file_name": "IMG_1923-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 147, "file_name": "IMG_1926-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 148, "file_name": "IMG_1933-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 149, "file_name": "IMG_1936-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 150, "file_name": "IMG_1937-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 151, "file_name": "IMG_1940-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 152, "file_name": "IMG_1943-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 153, "file_name": "IMG_1952-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 154, "file_name": "IMG_1953-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 155, "file_name": "IMG_1954-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 156, "file_name": "IMG_1964-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 157, "file_name": "IMG_1969-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 158, "file_name": "IMG_1970-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 159, "file_name": "IMG_1972-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 160, "file_name": "IMG_1992-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 161, "file_name": "IMG_1994-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 162, "file_name": "IMG_2002-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 163, "file_name": "IMG_2008-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 164, "file_name": "IMG_2009-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 165, "file_name": "IMG_2010-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 166, "file_name": "IMG_2013-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 167, "file_name": "IMG_2018-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 168, "file_name": "IMG_2025-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 169, "file_name": "IMG_2030-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 170, "file_name": "IMG_2032-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 171, "file_name": "IMG_2033-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 172, "file_name": "IMG_2034-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 173, "file_name": "IMG_2035-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 174, "file_name": "IMG_2041-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 175, "file_name": "IMG_2044-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 176, "file_name": "IMG_2047-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 177, "file_name": "IMG_2061-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 178, "file_name": "IMG_2069-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 179, "file_name": "IMG_2074-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 180, "file_name": "IMG_2076-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 181, "file_name": "IMG_2082-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 182, "file_name": "IMG_2090-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 183, "file_name": "IMG_2095-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 184, "file_name": "IMG_2096-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 185, "file_name": "IMG_2099-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 186, "file_name": "IMG_2102-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 187, "file_name": "IMG_2106-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 188, "file_name": "IMG_2115-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 189, "file_name": "IMG_2120-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 190, "file_name": "IMG_2125-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 191, "file_name": "IMG_2126-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 192, "file_name": "IMG_2166-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 193, "file_name": "IMG_2177-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 194, "file_name": "IMG_2181-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 195, "file_name": "IMG_2183-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 196, "file_name": "IMG_2215-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 197, "file_name": "IMG_2218-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 198, "file_name": "IMG_2220-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 199, "file_name": "IMG_2221-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null},
          {"id": 200, "file_name": "IMG_2257-2.JPG", "height": 1200, "width": 1600, "license": null,
           "coco_url": null}],
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

print(len(ff.get('annotations')))
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
        if ff.get('annotations')[i].get('id') == 64:
            lid.append(lid[-1] + 3)
            k = k + 3
        elif ff.get('annotations')[i].get('id') == 110:
            lid.append(lid[-1] + 2)
            k = k + 2
        else:
            lid.append(lid[-1] + 1)
            k = k + 1
        c = 0

fil.append({"id": 200, "file_name": "IMG_2257-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null})
fil.append({"id": 200, "file_name": "IMG_2257-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null})
fil.append({"id": 200, "file_name": "IMG_2257-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null})
fil.append({"id": 200, "file_name": "IMG_2257-2.JPG", "height": 1200, "width": 1600, "license": null, "coco_url": null})

lf = len(fil)
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
with open("msra_val_instance.json", "w") as outfile:
    json.dump(ff1, outfile)
