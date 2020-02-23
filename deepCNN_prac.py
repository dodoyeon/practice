import torch
import torch.nn as nn
import torchvision.datasets as datasets
import torch.transforms as transforms

device = 'cuda' if torch.cuda.is_available() else 'cpu'

torch.manual_seed(777)
if device == 'cuda':
    torch.cuda.manual_seed_all(777)

learning_rate = 0.001
training_epochs = 15
batch_size = 10

mnist_train = datasets.MNIST(root='MNIST_data/',
                             train=True,
                             transform=transforms.ToTensor,
                             download=True)
mnist_test = datasets.MNIST(root='MNIST_data/',
                            train=False,
                            transform=transforms.ToTensor,
                            download=True)

DataLoader = torch.utils.DataLoader(datasets=mnist_train,
                                    batch_size=batch_size,
                                    shuffle=True,
                                    drop_last=True)


class deepCNN(nn.Module):
    def __init__(self):
        super(deepCNN, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, strie=1, padding=1),
            nn.Relu(),
            nn.MaxPool2d(2, 2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, strie=1, padding=1),
            nn.Relu(),
            nn.MaxPool2d(2, 2)
        )
        self.layer3 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, strie=1, padding=1),
            nn.Relu(),
            nn.MaxPool2d(2, 2)
        )
        self.fc1 = nn.Linear(4 * 4 * 128, 625, bias=True)
        torch.nn.init.xavier_uniform_(self.fc1.weight)
        self.layer4 = nn.Sequential(
            self.fc1,
            nn.ReLU(),
            nn.Dropout(p=1 - self.keep_prob)
        )
        self.fc2 = nn.Linear(625, 10, bias=True)
        torch.nn.init.xavier_uniform_(self.fc2.weight)
        self.softmax = nn.Softmax()

    def forward(self, input):
        out = self.layer1(input)
        out = self.layer2(out)
        out = self.layer3(out)

        out = out.view(out.size(0), -1)
        out = self.layer4(out)
        output = self.fc2(out)
        # output = self.softmax(out)-> 왜지??? 왜 소프트맥스 안써?
        return output


model = deepCNN().to(device)
criterion = nn.CrossEntropyLoss().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

total_batch = len(DataLoader)
print('총 배치수 {}'.format(total_batch))

for epoch in range(training_epochs):
    avg_cost = 0;
    for mini_batch, label in DataLoader:
        mini_batch = mini_batch.to(device)
        label = label.to(device)

        optimizer.zero_grad()
        hypothesis = model(mini_batch)
        cost = criterion(hypothesis, label)
        cost.backward()
        optimizer.step()

        avg_cost = cost / total_batch

    print('[Epoch : {:>4}]  cost = {:>.9}'.format(epoch + 1, avg_cost))

with torch.no_grad():
    mini_batch_test = mnist_test.test_data.view(len(mnist_test), 1, 28, 28).float().to(device)
    label_test = mnist_test.test_labels.to(device)

    prediction = model(mini_batch_test)
    correct_prediction = torch.argmax(prediction, 1) == label_test
    accuracy = correct_prediction.float().mean()
    print('Accuracy : ', accuracy.item())