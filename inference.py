import torch
from torchvision import transforms
from PIL import Image

transform = transforms.Compose([
  transforms.Resize((200, 200)),
  transforms.ToTensor(),
])

def make_inference(paths):
  images = []
  for path in paths:
    img = Image.open(path)
    img_tensor = transform(img)
    images.append(img_tensor)
  img_tensors = torch.stack(images)
  
  model = torch.load(sign_language.pth)
  model.eval()

  with torch.no_grad():
    output = model(img_tensors.to(device))
  output = output.cpu()
  predicted_labels = output.argmax(1).numpy()
  predicted_classes = []
  for i in predicted_labels:
    predicted_classes.append(label_to_class[predicted_labels[i]])
  
  predicted_string = ''
  
  for i in predicted_classes:
    if i = 'space':
      predicted_string.append(' ')
    else:
      predicted_string.append(i)
  return predicted_string

result = make_inference(paths)

