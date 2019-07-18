import cv2
import shutil

import ospa
import os
from collections import Counter

from tqdm import tqdm


def check_id(*args):
    lists = []
    for item in args:
        lists.append([])
        for file_ in item:
            lists[-1].append(int(os.path.split(file_)[-1].split('_')[0]))
    for item in lists:
        item.sort()
    for item in lists:
        for item2 in lists:
            assert item == item2, 'incorrect id lists'


def check_type(files):
    current_set = set()
    for file_ in files:
        filename = os.path.split(file_)[-1]
        current_set.add(filename.split('_')[2].split('.')[0])
    assert len(current_set) == 1, f'wrong set {current_set}'
    print(current_set)


def check_devices(*args):
    lists = []
    for item in args:
        lists.append([])
        for file_ in item:
            lists[-1].append(os.path.split(file_)[-1].split('_')[1])
    for item in lists:
        item.sort()

    for item in lists:

        for item2 in lists:
            assert item == item2, 'incorrect device lists'
    cnt = Counter(lists[-1])
    dev = []
    for item in cnt.most_common(100):
        print(f'{item[0]}: {item[1]}')
        dev.append(item[0])
    for item in sorted(dev):
        print(item)
    print(len(dev))


def replace_device_names(files):
    replace_dict = {
        'NIKON-3400-18-55mm': 'NIKON-D3400-18-55MM',
        'NIKON-3400-35mm': 'NIKON-D3400-35MM',
        'HONOR7X': 'HONOR-7X',
        'HONOR10': 'HONOR-10',
        'HONOR9': 'HONOR-9',
        'IPHONE7': 'IPHONE-7',
        'REDMI-3S': 'XIAOMI-REDMI-3S',
        'PRESIGIO-MULTI-PHONE': 'PRESTIGIO-MULTI-PHONE',
        'SAMSUNG-A3': 'SAMSUNG-GALAXY-A3',
        'SAMSUNG-A5': 'SAMSUNG-GALAXY-A5',
        'SAMSUNG-A6': 'SAMSUNG-GALAXY-A6',
        'SAMSUNG-A8': 'SAMSUNG-GALAXY-A8',
        'SAMSUNG-J7': 'SAMSUNG-GALAXY-J7',
        'XT1710-09': 'MOTOROLA-MOTO-Z2-PLAY',
        'XIAOMI-REDMI-NOT-4X': 'XIAOMI-REDMI-NOTE-4X',
        'XIAOMI-MI-8-LITE': 'XIAOMI-MI8-LITE',
        'XIAOMI-MI8SE': 'XIAOMI-MI8-SE',
        'XIAOMI-MI-8SE': 'XIAOMI-MI8-SE',
        'SAMSUNG-GALAXY-A8+': 'SAMSUNG-GALAXY-A8-PLUS',
        'SAMSUMG-A700F': 'SAMSUNG-GALAXY-A8',
        'HUAWEIP20': 'HUAWEI-P20',
        'HUASWEI-P20-LITE': 'HUAWEI-P20-LITE',
        'XIAOMI-REDMI-NOTE7': 'XIAOMI-REDMI-NOTE-7',
        'NIKON-3400-35MM': 'NIKON-D3400-35MM',
        'NIKON-3400-18-55MM': 'NIKON-D3400-18-55MM'
        }
    for file_ in files:
        dir_, filename = os.path.split(file_)
        id_, device, end = filename.split('_')
        if device in replace_dict:
            print(f'I\'ll replace {filename} with device {device} to {replace_dict[device]}')
            new_filename = f'{id_}_{replace_dict[device]}_{end}'
            new_full_path = os.path.join(dir_, new_filename)
            shutil.move(file_, new_full_path)


def parse_folder(src_folder,
                 sharp_folder='sharp',
                 defocused_folder='defocused_blurred',
                 motion_folder='motion_blurred'):
    sharp_images = ospa.listdir(os.path.join(src_folder, sharp_folder))
    defocused_images = ospa.listdir(os.path.join(src_folder, defocused_folder))
    motion_images = ospa.listdir(os.path.join(src_folder, motion_folder))
    check_id(sharp_images, defocused_images, motion_images)
    check_type(sharp_images)
    check_type(defocused_images)
    check_type(motion_images)
    check_devices(sharp_images, defocused_images, motion_images)
    replace_device_names(sharp_images)
    replace_device_names(defocused_images)
    replace_device_names(motion_images)


def check_folders_exist(dst_folder, sharp_folder, defocused_folder, motion_folder):
    if not os.path.exists(dst_folder):
        os.mkdir(dst_folder)
    if not os.path.exists(os.path.join(dst_folder, sharp_folder)):
        os.mkdir(os.path.join(dst_folder, sharp_folder))
    if not os.path.exists(os.path.join(dst_folder, defocused_folder)):
        os.mkdir(os.path.join(dst_folder, defocused_folder))
    if not os.path.exists(os.path.join(dst_folder, motion_folder)):
        os.mkdir(os.path.join(dst_folder, motion_folder))


def move_bad_ids(src_folder,
                 dst_folder,
                 bad_ids,
                 sharp_folder='sharp',
                 defocused_folder='defocused_blurred',
                 motion_folder='motion_blurred'):
    sharp_images = ospa.listdir(os.path.join(src_folder, sharp_folder), full_path=False)
    defocused_images = ospa.listdir(os.path.join(src_folder, defocused_folder), full_path=False)
    motion_images = ospa.listdir(os.path.join(src_folder, motion_folder), full_path=False)
    check_folders_exist(dst_folder, sharp_folder, defocused_folder, motion_folder)

    for images, folder in zip([sharp_images, defocused_images, motion_images],
                              [sharp_folder, defocused_folder, motion_folder]):
        for file_ in images:
            id_ = int(file_.split('_')[0])
            if id_ in bad_ids:
                print(f'I\'ll move {file_}')
                shutil.move(os.path.join(src_folder, folder, file_),
                            os.path.join(dst_folder, folder, file_))


def fix_id(src_folder,
           dst_folder,
           sharp_folder='sharp',
           defocused_folder='defocused_blurred',
           motion_folder='motion_blurred'):
    id_dict = {}
    check_folders_exist(dst_folder, sharp_folder, defocused_folder, motion_folder)
    sharp_images = ospa.listdir(os.path.join(src_folder, sharp_folder), full_path=False)
    defocused_images = ospa.listdir(os.path.join(src_folder, defocused_folder), full_path=False)
    motion_images = ospa.listdir(os.path.join(src_folder, motion_folder), full_path=False)
    for image in sharp_images:
        id_ = int(image.split('_')[0])
        if id_ not in id_dict:
            id_dict[id_] = [-1, -1, -1]
        id_dict[id_][0] = '_'.join(image.split('_')[1:])
    for image in defocused_images:
        id_ = int(image.split('_')[0])
        if id_ not in id_dict:
            id_dict[id_] = [-1, -1, -1]
        id_dict[id_][1] = '_'.join(image.split('_')[1:])
    for image in motion_images:
        id_ = int(image.split('_')[0])
        if id_ not in id_dict:
            id_dict[id_] = [-1, -1, -1]
        id_dict[id_][2] = '_'.join(image.split('_')[1:])

    print(id_dict)
    print(len(id_dict))

    for index, (key, item) in enumerate(id_dict.items()):
        sharp_image_new = os.path.join(dst_folder, sharp_folder, f'{index}_{item[0]}')
        defocused_image_new = os.path.join(dst_folder, defocused_folder, f'{index}_{item[1]}')
        motion_image_new = os.path.join(dst_folder, motion_folder, f'{index}_{item[2]}')
        sharp_image_old = os.path.join(src_folder, sharp_folder, f'{key}_{item[0]}')
        defocused_image_old = os.path.join(src_folder, defocused_folder, f'{key}_{item[1]}')
        motion_image_old = os.path.join(src_folder, motion_folder, f'{key}_{item[2]}')
        print(sharp_image_new)
        print(defocused_image_new)
        print(motion_image_new)
        print(sharp_image_old)
        print(defocused_image_old)
        print(motion_image_old)
        shutil.move(sharp_image_old, sharp_image_new)
        shutil.move(defocused_image_old, defocused_image_new)
        shutil.move(motion_image_old, motion_image_new)


def check_sizes(src_folder,
                sharp_folder='sharp',
                defocused_folder='defocused_blurred',
                motion_folder='motion_blurred'):
    sharp_images = ospa.listdir(os.path.join(src_folder, sharp_folder))
    defocused_images = ospa.listdir(os.path.join(src_folder, defocused_folder))
    motion_images = ospa.listdir(os.path.join(src_folder, motion_folder))
    print(len(sharp_images), len(defocused_images), len(motion_images))
    for sharp, defocused, motion in tqdm(zip(sharp_images, defocused_images, motion_images),
                                         total=len(sharp_images)):
        sharp_image = cv2.imread(sharp)
        defocused_image = cv2.imread(defocused)
        motion_image = cv2.imread(motion)
        if sharp_image.shape != defocused_image.shape or sharp_image.shape != motion_image.shape:
            print('before', sharp, sharp_image.shape, defocused_image.shape, motion_image.shape)
            min_y = min(sharp_image.shape[0], defocused_image.shape[0], motion_image.shape[0])-1
            min_x = min(sharp_image.shape[1], defocused_image.shape[1], motion_image.shape[1])-1
            sharp_image = sharp_image[:min_y, :min_x]
            defocused_image = defocused_image[:min_y, :min_x]
            motion_image = motion_image[:min_y, :min_x]
            print('after', sharp, sharp_image.shape, defocused_image.shape, motion_image.shape)
            cv2.imwrite(sharp, sharp_image)
            cv2.imwrite(defocused, defocused_image)
            cv2.imwrite(motion, motion_image)


def scale_base_to(src_folder,
                  dst_folder,
                  dst_size=1024,
                  sharp_folder='sharp',
                  defocused_folder='defocused_blurred',
                  motion_folder='motion_blurred'):

    check_folders_exist(dst_folder, sharp_folder, defocused_folder, motion_folder)

    sharp_images = ospa.listdir(os.path.join(src_folder, sharp_folder))
    defocused_images = ospa.listdir(os.path.join(src_folder, defocused_folder))
    motion_images = ospa.listdir(os.path.join(src_folder, motion_folder))
    print(len(sharp_images), len(defocused_images), len(motion_images))
    for sharp, defocused, motion in tqdm(zip(sharp_images, defocused_images, motion_images),
                                         total=len(sharp_images)):
        sharp_image = cv2.imread(sharp)
        defocused_image = cv2.imread(defocused)
        motion_image = cv2.imread(motion)
        scale = dst_size/max(sharp_image.shape)
        sharp_image = cv2.resize(sharp_image, (0, 0), fx=scale, fy=scale)
        defocused_image = cv2.resize(defocused_image, (0, 0), fx=scale, fy=scale)
        motion_image = cv2.resize(motion_image, (0, 0), fx=scale, fy=scale)
        cv2.imwrite(os.path.join(dst_folder, sharp_folder, os.path.split(sharp)[-1]),
                    sharp_image)
        cv2.imwrite(os.path.join(dst_folder, defocused_folder, os.path.split(defocused)[-1]),
                    defocused_image)
        cv2.imwrite(os.path.join(dst_folder, motion_folder, os.path.split(motion)[-1]),
                    motion_image)


if __name__ == '__main__':
    parse_folder(r'G:\_datasets\blur_dataset')
    # bad_id = [10, 86, 121, 164, 192, 195, 17, 36, 47, 53, 89, 106, 154, 44, 46,
    #           48, 87, 88, 94, 97, 104, 110, 128, 136, 139,  143, 170, 175, 205,
    #           218, 255, 298, 301, 306, 317, 335, 347, 379, 206, 222, 234, 295, 296, 309]
    #
    # move_bad_ids(r'G:\_datasets\blur_dataset', r'G:\_datasets\blur_dataset_tmp', bad_id)
    # parse_folder(r'G:\_datasets\blur_dataset')
    # fix_id(r'G:\_datasets\blur_dataset', r'G:\_datasets\blur_dataset_fix_id')
    check_sizes(r'G:\_datasets\blur_dataset')
    scale_base_to(r'G:\_datasets\blur_dataset', r'G:\_datasets\blur_dataset_scaled')


