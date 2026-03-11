import torch
import torch
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
from exp import brainneuralnetwork

class models():
    def __init__(self):
          pass
          
    def predict_iris(self, model, x_test):

            model.eval()
            with torch.no_grad():
                x_1, x_2, logits = model(x_test)
                print(logits)

            return torch.argmax(logits, dim=1)


if __name__ == '__models__':
    models()