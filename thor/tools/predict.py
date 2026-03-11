import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.datasets import load_iris
import pandas as pd
from exp import brainneuralnetwork
from predictionmodels import models


def trainpredict_iris(m: str = 'predict'):
    
    all_data = load_iris(as_frame=True)

    data = pd.DataFrame(all_data.data).astype('Float32')
    target = pd.DataFrame(all_data.target).astype('Float32')


    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)
    
    x_train_tensor, x_test_tensor, y_train_tensor, y_test_tensor = torch.tensor(X_train.values), torch.tensor(X_test.values), torch.tensor(y_train.values), torch.tensor(y_test.values)


    if m == 'train':
          
        model = brainneuralnetwork()
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=0.01)

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
        
    else: 

        predictions = models.predict_iris(model=model, x_test=x_test_tensor)

        y_preds = [all_data.target_names[i] for i in predictions]
        y_tags = [all_data.target_names[int(i)] for i in y_test['target']]

        print(f'predictions: {predictions}')
        for item in list(zip(y_tags, y_preds)):
                print(item)
        print(f'accuracy: {accuracy_score(y_test, predictions)}')
        print(f'confusion: {confusion_matrix(y_test, predictions)}')
        print(f'score: {((predictions == y_test_tensor.long().squeeze()).sum().item()/len(y_test))*100}%')


if __name__ == '__main__':
     
     print('active')