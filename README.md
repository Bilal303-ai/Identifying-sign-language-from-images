# About
This model interprets American-Sign-Language from images. The model takes images representing the consecutive letters in a sentence and return the sentence in the form of a string.
#### Input images:

![H](https://github.com/user-attachments/assets/97022b03-f99b-4136-bc67-14fbd7b0d2fb) ![I](https://github.com/user-attachments/assets/bd42a9e7-fb13-4be3-b974-b8f814c354ce)![space](https://github.com/user-attachments/assets/31a5b8fd-1b7c-4e87-a61f-e7bbcc241e63) ![H](https://github.com/user-attachments/assets/9914fd94-86d4-4d74-9658-ef97a5f49d73) ![O](https://github.com/user-attachments/assets/1149e922-ef1c-42e2-8a25-d141f754f98a) ![W](https://github.com/user-attachments/assets/7392e0d5-db74-47b3-85eb-0931b619e8a6) ![space](https://github.com/user-attachments/assets/cf55b0b8-e06e-4f44-aac3-8860fcb5ec3e) ![A](https://github.com/user-attachments/assets/f41a7098-1a46-4ff2-92ad-ca541ceb29aa) ![R](https://github.com/user-attachments/assets/5b62f266-27bb-4726-806e-861dbd271b34) ![E](https://github.com/user-attachments/assets/b61840a6-59b3-4b1b-86a5-ce2e28a5b048) ![space](https://github.com/user-attachments/assets/43b25ffd-94dd-4d4b-99ab-93bc3503db06) ![Y](https://github.com/user-attachments/assets/ebf5ba54-4962-46f8-b313-83e4e2e14d90) ![O](https://github.com/user-attachments/assets/c5b11206-6bb0-44ce-9800-c5382bae667f) ![U](https://github.com/user-attachments/assets/18533309-c28c-4e4b-a9e5-d2d4039d50f0)

#### Output:
"HI HOW ARE YOU"

The model was trained on [**ASL Alphabet**](https://www.kaggle.com/datasets/grassknoted/asl-alphabet) dataset.

# Setup instructions
1. Clone the repository:
   
   ```bash
   git clone https://github.com/Bilal303-ai/Interpreting-sign-language-from-images
   cd Identifying-sign-language-from-images
   ```
3. Install `Pillow`, `torch` and `torchvision`
4. Open `inference.py` and look up for the python list `paths = ['path_to_first_image', 'path_to_second_image', 'path_to_third_image',...]` and replace `'path_to_first_image', 'path_to_second_image', 'path_to_third_image',...` with actual file paths.
5. Run the following command:
   
   ```bash
   python inference.py
   ```











