import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
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

    model = brainneuralnetwork()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    all_data = load_iris(as_frame=True)

    data = pd.DataFrame(all_data.data).astype('Float32')
    target = pd.DataFrame(all_data.target).astype('Float32')


    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)
   
    # X_train, X_test, y_train, y_test = pd.DataFrame(X_train), pd.DataFrame(X_test), pd.DataFrame(y_train), pd.DataFrame(y_test)
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    y_train = y_train.astype('float32')
    y_test = y_test.astype('float32')

    x_train_tensor, x_test_tensor, y_train_tensor, y_test_tensor = torch.tensor(X_train.values), torch.tensor(X_test.values), torch.tensor(y_train.values), torch.tensor(y_test.values)


    for epoch in range(0, 500, 1):

        x1, x2, x3 = model(x_train_tensor)
        # print(f'x1: {x1[:4]}\nx2: {x2[:4]}\nx3: {x3[:4]}')

        optimizer.zero_grad()

        loss = criterion(x3, y_train_tensor.long().squeeze())
        loss.backward()

        optimizer.step()

        if epoch % 10 == 0:
            print(f'epoch {epoch} -> loss ({loss.item()})')
    


    torch.save(model.state_dict(), 'iris_brain.pth')

    













    # dic = [('name1', 'kofi'), ('name2', 'kwame'), ('name3', 'yaw'), ('name4', 'kwasi')]

    # t = [*dic]

    # li, la = zip(*dic)

    # print(t)
    # print(li, la)


    # y = np.random.rand(5, 2)*100
    # print(y)
    # y = torch.tensor(y)
    # print(y.dtype)
    # print(y)
    # x = torch.tensor([1., 1.])
    # print(f'hello: {x}')