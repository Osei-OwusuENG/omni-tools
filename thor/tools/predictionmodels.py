import torch
import torch
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
from exp import brainneuralnetwork

def predict(model, x_test):

        model.eval()
        with torch.no_grad():
            x_1, x_2, logits = model(x_test)
            print(logits)

        return torch.argmax(logits, dim=1)



if __name__ == '__main__':
    
    model = brainneuralnetwork()
    model.load_state_dict(torch.load('iris_brain.pth'))
    all_data = load_iris(as_frame=True)
    data = all_data.data
    target = all_data.target

    _, x_test, _, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

    x_test = pd.DataFrame(x_test)
    y_test = pd.DataFrame(y_test)
    x_test = x_test.astype('float32')
    y_test = y_test.astype('float32')
    x_test_tensor = torch.tensor(x_test.values)
    y_test_tensor = torch.tensor(y_test.values)

    predictions = predict(model=model, x_test=x_test_tensor)

    y_preds = [all_data.target_names[i] for i in predictions]
    y_tags = [all_data.target_names[int(i)] for i in y_test['target']]

    print(f'predictions: {predictions}')
    for item in list(zip(y_tags, y_preds)):
         print(item)
    print(f'accuracy: {accuracy_score(y_test, predictions)}')
    print(f'confusion: {confusion_matrix(y_test, predictions)}')
    print(f'score: {((predictions == y_test_tensor.long().squeeze()).sum().item()/len(y_test))*100}%')