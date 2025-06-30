# Smart-sorting
"Smart Sorting Using Transfer Learning(VGG16) for Fresh and Rotten Fruit Classification"

model link 🔗https://drive.google.com/file/d/162P3Q1cD9NKiSLx6AeiBUOpqHDgVMDf0/view?usp=drivesdk

## Demo Video link
[!demovideo]()

🧠 Smart Sorting: Transfer Learning for Identifying Rotten Fruits and Vegetables

Smart Sorting is an AI-powered system designed to detect and classify rotten fruits and vegetables using transfer learning with the VGG16 model. It helps automate quality checks in food processing, retail, and even smart homes to reduce food waste and enhance safety.

👉 Project Workflow :
1. Dataset Collection (from Kaggle - 28 classes)
2. Data Preprocessing & Augmentation
3. Split into Training & Testing
4. Load & Fine-tune VGG16
5. Train, Evaluate, Save (.h5)
6. Build Flask App + UI
7. Deploy Locally


  
🛠️ Tools & Technologies Used

👉 Development Tools:

Python : Core programming language for model and app logic.

Google Colab : For training the model and data preprocessing.

Visual Studio Code (VS Code) : For building and testing the Flask web app.

Flask	: To build the web interface (routes, HTML integration, etc.)

TensorFlow / Keras : Deep learning framework for model training and .h5 model loading.

Pillow (PIL): Image handling and preprocessing before feeding to the model.

NumPy	: Numerical operations and array manipulation.

👉 Frontend Tools:

HTML5 / CSS3	Structure and styling of the website

Responsive Design (Media Queries)	Ensures the website works on all screen sizes

Jinja2 Templating (in Flask)	Renders dynamic predictions in HTML pages

👉 AI/ML Tools:

VGG16	: Pre-trained model used for transfer learning

Transfer Learning	: Speeds up training by using learned features from pre-trained networks

Data Augmentation :(Optional)	Increases dataset diversity during training


👉 Deployment :

 GitHub	: Version control and project hosting

⭐ Applications:

1. Factories – Helps quickly find and remove bad fruits and vegetables on machines instead of doing it by hand.


2. Supermarkets – Checks if fruits and veggies are fresh before putting them on shelves.


3. Smart Fridge – Tells you on your phone if something inside your fridge is going bad.

📝 These are just a few practical examples — the technology can be applied in many more real-life situations.


## screenshots
![home page](https://github.com/Tarun25-dev/Smart-sorting/blob/main/static/assets/projectimg/Screenshot%20(16).png)

![upload page](https://github.com/Tarun25-dev/Smart-sorting/blob/main/static/assets/projectimg/Screenshot%20(17).png)

![predict page](https://github.com/Tarun25-dev/Smart-sorting/blob/main/static/assets/projectimg/Screenshot%20(18).png)

![while running flask](https://github.com/Tarun25-dev/Smart-sorting/blob/main/static/assets/projectimg/Screenshot%20(19).png)
