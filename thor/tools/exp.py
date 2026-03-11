import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd


class brainneuralnetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(4, 12)
        self.hidden2 = nn.Linear(12, 24)
        self.output = nn.Linear(24, 3)

    def forward(self, x):

        x1 = torch.relu(self.hidden(x))
        x2 = self.hidden2(x1)
        x3 = self.output(x2)

        return x1, x2, x3
    


if __name__ == '__main__':

    print('active')