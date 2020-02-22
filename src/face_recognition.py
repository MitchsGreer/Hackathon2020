from facenet_pytorch import MTCNN
from facenet_pytorch import InceptionResnetV1
from torch.utils.data import DataLoader
from torchvision import datasets
from PIL import Image
import numpy as np
import pandas as pd
import os
import torch


def collate_fn(x):
    return x[0]


def checkForFace(filepath):
    img = Image.open(filepath)

    # number of threads
    workers = 0 if os.name == 'nt' else 4

    # tell py torch what device
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print('Running on device: {}'.format(device))

    # create the "classifier"
    mtcnn = MTCNN(device=device)

    # Get the training for the classifier
    resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)

    _, prob = mtcnn(img, return_prob=True)

    return prob


def compare(img_1_filepath, img_2_filepath):

    img_1 = Image.open(img_1_filepath)
    img_2 = Image.open(img_2_filepath)
