from facenet_pytorch import MTCNN
from facenet_pytorch import InceptionResnetV1
from torch.utils.data import DataLoader
from torchvision import datasets
import facenet_pytorch
from PIL import Image
import numpy as np
import pandas as pd
import os
import torch
import face_recognition


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

    known_image = Image.open(img_1_filepath)
    unknown_image = Image.open(img_2_filepath)

    img_1_encoding = face_recognition.face_encodings(known_image)[0]
    img_2_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces(
        [biden_encoding], unknown_encoding, tolerance=0.5)


print(compare("data/test_images/imgMitch.jpeg", "data/test_images/imgMitch.jpeg"))
