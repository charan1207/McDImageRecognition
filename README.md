# McDImageRecognition

# Description
McDImageRecognition is a machine learning project focused on image classification for McDonald's fast food items, including Big Mac burgers, French fries, and nuggets. The project   utilizes a Support Vector Machine (SVM) model trained on a dataset of delicious fast food images. A Streamlit web application allows users to upload an image, and the trained model   predicts the category of the McDonald's item, providing a delightful and interactive experience for fast food enthusiasts. Explore the code for a hands-on understanding of image classification in the context of everyone's favorite golden arches.

## Technologies Used:
- **Python:** The primary programming language for the project.
- **scikit-learn:** Utilized for building and training the machine learning model. GridSearchCV is employed for hyperparameter tuning, optimizing SVM parameters (C and gamma).
- **Bing Image Downloader:** A Python library used to download images from Bing for creating the dataset.
- **streamlit:** A web application framework for creating interactive and user-friendly interfaces. The Streamlit app allows users to upload an image and receive predictions from the trained model.
- **numpy and matplotlib:** Used for array operations, data manipulation, and visualization.
- **PIL (Pillow):** Employed for handling image files and facilitating image-related operations.
- **pickle:** Used to serialize and deserialize the trained SVM model for easy storage and retrieval.

## Model Details:
- **Support Vector Machine (SVM):** SVM is a powerful supervised learning algorithm used for classification and regression tasks. In this project, an SVM classifier is employed for image classification.
- **Radial Basis Function (RBF) Kernel:** The RBF kernel is selected for its ability to handle non-linear relationships in the data, making it well-suited for image classification tasks.


## Steps:
1. **Data Collection:**
   In this step, images are collected from Bing using the Bing Image Downloader library. The search terms used for image retrieval are 'pretty sunflower,' 'ruby ball leather,' and 'Ice cream cone.' The images are downloaded and stored 
   in the 'images' directory.
   
  ![image](https://github.com/charan1207/McDImageRecognition/blob/main/ImgMacD/Data%20collection.png?raw=true)
  

2. **Preprocessing:**
   The collected images undergo preprocessing to make them suitable for model training. Each image is resized to a common size of 150x150 pixels with three color channels (RGB). Additionally, the images are flattened to create a one-dimensional array for each image.

   ![image](https://github.com/charan1207/McDImageRecognition/blob/main/ImgMacD/preprocessing.png?raw=true)

3. **Model Training:**
   A Support Vector Machine (SVM) classifier is employed for the image classification task. The scikit-learn library is used for          
   implementing the SVM model. Hyperparameter tuning is performed using GridSearchCV to find the optimal     
   values for the regularization parameter (C) and the kernel coefficient (gamma).
 ![image](https://github.com/charan1207/McDImageRecognition/assets/28255223/a3a69b6b-7811-4cc5-9e22-83b159600eca)
   
4. **Model Evaluation:**
   The trained model's performance is evaluated using a test set that was previously separated from the dataset. The accuracy score is calculated, and a confusion matrix is generated to assess the model's ability to correctly classify 
   images into the specified categories.
  ![image](https://github.com/charan1207/McDImageRecognition/assets/28255223/59acc845-2136-4ed8-a561-95cbda7a1a6e)


5. **Model Deployment:**
    The trained SVM model is saved for future use using the pickle library. This serialized model can be easily loaded and used to make predictions on new, unseen images without the need to retrain the model.
  ![image](https://github.com/charan1207/McDImageRecognition/assets/28255223/d0ee163e-4e67-44bf-9483-0dbf6738ff53)


6. **Streamlit Web App:**
    A user-friendly web application is developed using Streamlit. Users can interact with the application by uploading an image through the web interface. The uploaded image is then fed into the trained SVM model, and predictions with 
    probabilities for each class are displayed to the user.
   ![image](https://github.com/charan1207/McDImageRecognition/assets/28255223/3dfb0f8b-fe6b-4a95-8a39-77eb52c20033)

7. **Predicted output**
   The output will be a web application where users can upload an image, and the model will predict whether it belongs to one of the specified categories with associated probabilities. The last two lines seem to include a command for running the Streamlit app and exposing it through localtunnel, a tool for exposing local servers to the internet
   ![image](https://github.com/charan1207/McDImageRecognition/assets/28255223/d900c4b7-4568-4e11-8f2c-762bae446981)
    
## Instructions for Running the Streamlit App:
1. Install required dependencies using `pip install -r requirements.txt`.
2. Run the app using `streamlit run app.py`.
3. Upload an image and click the "Predict" button to see the model's predictions.


## UseCase
A use case for McDonald's could involve employing the image classification model created in the provided code to enhance customer experience and streamline operations. Here are a few potential use cases:

**1. Automated Menu Suggestions:**
Implement the image classification model in a mobile app or kiosk system within McDonald's outlets.
Customers can use the app to take a picture of their preferred food item, and the model predicts the category (e.g., big mac burger, french fries, nuggets).
Provide personalized menu suggestions based on the identified category, promoting a more tailored and user-friendly experience.

**2. Quality Control in Food Preparation:**
Integrate the image classification model into the kitchen's food preparation process.
Use cameras to capture images of prepared food items, and the model can verify if the items match the expected appearance.
Improve quality control by ensuring that the final products meet McDonald's standards in terms of presentation.

**3. Social Media Engagement:**
Leverage the image classification model to analyze and categorize images shared by customers on social media platforms.
McDonald's could use this information for social media marketing campaigns, engagement with user-generated content, and understanding customer preferences.

**4. Inventory Management:**
Integrate the model into the inventory management system to track and categorize ingredients and prepared food items.
This can help in optimizing inventory levels, reducing waste, and ensuring that popular items are adequately stocked.

**5. Drive-Through Optimization:**
Implement the model at drive-throughs to streamline order processing.
Customers can provide visual input of their desired menu items, and the system can use the model to quickly identify and process the order, potentially reducing order errors and wait times.



Feel free to explore and contribute to the project. If you have any questions or suggestions, please open an issue or reach out.




