#%%
from cmath import log
from distutils.log import debug
import json
import numpy as np

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from nltk_utils import tokenize, stem, bag_of_words
from model import NeuralNet


with open('intents.json','r') as f:
    intents = json.load(f)

all_words = []  # list of all words
tags = []       #collect all patterns and different text they have
xy = []         #empty list containing all patterns and their text

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ['?', '!', '.', ',']

all_words = [stem(w) for w in all_words if w not in ignore_words]    # remove stop words ; list comprehension
all_words = sorted(set(all_words))  #removes duplicates
tags = sorted(set(tags))  #removes duplicates labels

print(tags)
# %%

X_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)       #CrossEntropyLoss

X_train = np.array(X_train)
y_train = np.array(y_train)

print(y_train)

#%%

#Hyperparameters
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(X_train[0])
print(input_size, len(all_words))
learning_rate = 0.01
num_epochs = 1000

class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    # support indexing such that dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # we can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_size, hidden_size, output_size).to(device)

#loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)


for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(device)

        #forward pass
        #log(words)
        outputs = model(words)
        loss = criterion(outputs, labels)

        #backward and optimize

        optimizer.zero_grad()
        #loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'epoch {epoch+1}/{num_epochs} loss {loss.item():.4f}')

#print(f'final loss, loss ={loss.items():.4f}')

# %%
