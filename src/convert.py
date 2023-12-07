# https://www.kaggle.com/datasets/kumaresanmanickavelu/lyft-udacity-challenge?datasetId=27201&sortBy=voteCount

import os, glob
import numpy as np
import supervisely as sly
from supervisely.io.fs import get_file_name, get_file_name_with_ext
from cv2 import connectedComponents
from dotenv import load_dotenv
import supervisely as sly
import os
from dataset_tools.convert import unpack_if_archive
import src.settings as s
from urllib.parse import unquote, urlparse
from supervisely.io.fs import get_file_name, get_file_size, dir_exists
import shutil

from tqdm import tqdm


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "RELLIS-3D"
    splits_path = "/home/grokhi/rawdata/rellis-3d-rgb"
    images_folder = "/home/grokhi/rawdata/rellis-3d-rgb/Rellis-3D"
    masks_folder = "/home/grokhi/rawdata/rellis-3d-rgb/Rellis-3D"
    batch_size = 30

    def create_ann(image_path):
        labels = []

        mask_path = image_path_to_mask_path[image_path]
        ann_np = sly.imaging.image.read(mask_path)[:, :, 0]
        img_height = ann_np.shape[0]
        img_wight = ann_np.shape[1]
        unique_idx = np.unique(ann_np)

        for i in unique_idx:
            obj_mask = ann_np == i
            ret, curr_mask = connectedComponents(obj_mask.astype("uint8"), connectivity=8)
            for j in range(1, ret):
                obj_mask = curr_mask == j
                curr_bitmap = sly.Bitmap(obj_mask)
                if curr_bitmap.area > 50:
                    curr_obj_class = idx_to_obj_class[i]
                    curr_label = sly.Label(curr_bitmap, curr_obj_class)
                    labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    void = sly.ObjClass("void", sly.Bitmap, color=(0, 0, 0))
    dirt = sly.ObjClass("dirt", sly.Bitmap, color=(108, 64, 20))
    grass = sly.ObjClass("grass", sly.Bitmap, color=(0, 102, 0))
    tree = sly.ObjClass("tree", sly.Bitmap, color=(0, 255, 0))
    pole = sly.ObjClass("pole", sly.Bitmap, color=(0, 153, 153))
    water = sly.ObjClass("water", sly.Bitmap, color=(0, 128, 255))
    sky = sly.ObjClass("sky", sly.Bitmap, color=(0, 0, 255))
    vehicle = sly.ObjClass("vehicle", sly.Bitmap, color=(255, 255, 0))
    object_class = sly.ObjClass("object", sly.Bitmap, color=(255, 0, 127))
    asphalt = sly.ObjClass("asphalt", sly.Bitmap, color=(64, 64, 64))
    building = sly.ObjClass("building", sly.Bitmap, color=(255, 0, 0))
    log = sly.ObjClass("log", sly.Bitmap, color=(102, 0, 0))
    person = sly.ObjClass("person", sly.Bitmap, color=(204, 153, 255))
    fence = sly.ObjClass("fence", sly.Bitmap, color=(102, 0, 204))
    bush = sly.ObjClass("bush", sly.Bitmap, color=(255, 153, 204))
    concrete = sly.ObjClass("concrete", sly.Bitmap, color=(170, 170, 170))
    barrier = sly.ObjClass("barrier", sly.Bitmap, color=(41, 121, 255))
    puddle = sly.ObjClass("puddle", sly.Bitmap, color=(134, 255, 139))
    mud = sly.ObjClass("mud", sly.Bitmap, color=(99, 66, 34))
    rubble = sly.ObjClass("rubble", sly.Bitmap, color=(110, 22, 138))

    idx_to_obj_class = {
        0: void,
        1: dirt,
        3: grass,
        4: tree,
        5: pole,
        6: water,
        7: sky,
        8: vehicle,
        9: object_class,
        10: asphalt,
        12: building,
        15: log,
        17: person,
        18: fence,
        19: bush,
        23: concrete,
        27: barrier,
        31: puddle,
        33: mud,
        34: rubble,
    }

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=list(idx_to_obj_class.values()))
    api.project.update_meta(project.id, meta.to_json())

    for curr_file in os.listdir(splits_path):
        if dir_exists(os.path.join(splits_path, curr_file)):
            continue
        ds_name = get_file_name(curr_file)

        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        curr_split_path = os.path.join(splits_path, curr_file)
        image_path_to_mask_path = {}

        with open(curr_split_path) as f:
            content = f.read().split("\n")
            for row in content:
                if len(row) > 0:
                    im_path = os.path.join(images_folder, row.split(" ")[0])
                    mask_path = os.path.join(masks_folder, row.split(" ")[1])
                    image_path_to_mask_path[im_path] = mask_path

        images_pathes = list(image_path_to_mask_path.keys())
        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_pathes))

        for img_pathes_batch in sly.batched(images_pathes, batch_size=batch_size):
            img_names_batch = [get_file_name_with_ext(im_path) for im_path in img_pathes_batch]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(img_names_batch))
    return project
