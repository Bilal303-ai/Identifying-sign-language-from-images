import torch.nn as nn

class ImageClassifier(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.convolution = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=16, kernel_size=5)
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2), #output_shape=(batch_size, 16, 98, 98)
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=5)
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2), #output_shape=(batch_size, 32, 47, 47)
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5)
            nn.ReLU(),
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=5)
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
            nn.Dropout(p=0.2),
            nn.Flatten(),
            nn.Linear(128 * 19 * 19, 128),
            nn.ReLU(),
            nn.Linear(128, num_classes),
        )
        
    def forward(self, x):
        logits = self.convolution(x)
        return logits
