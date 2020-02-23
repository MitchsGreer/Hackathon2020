from facenet_pytorch import MTCNN
from facenet_pytorch import InceptionResnetV1
from PIL import Image
import os
import torch


def checkForFace(filepath):

    img = Image.open(filepath)

    # number of threads
    workers = 0 if os.name == 'nt' else 4

    # tell py torch what device
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    # create the "classifier"
    mtcnn = MTCNN(device=device)

    # Get the training for the classifier
    resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)

    _, prob = mtcnn(img, return_prob=True)

    return prob
