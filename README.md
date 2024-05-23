# Project Goal
My  goal is to bu-ld the model that supports the "behind the scene" of the mobile application, which uses **deep learning** and **convolutional neural network**.


<img width="530" alt="image" src="https://github.com/Sumbati10/Potato-Disease-Classification-Using-CNN/assets/105505214/56231b7a-b3da-41f5-acf6-37951195e9a1">



## Process
#### :one:   Data Acquisition
### :two:   Data Preparation

- **tf dataset**

- **Resize & Scale**

- **Data augmentation**

<details>
<summary> Data Splitting </summary>

- Create function `get_dataset_partitions_tf()` to split data into **train, validate, test**

 Test prepare function

- Check the size of each dataset
     ```sh
     len(train), len(validate), len(test)
     ```
- Call the function, and cache e the 3 data samples
     ```sh
    train = train.cache().shuffle(1000).prefetch(buffer_size = tf.data.AUTOTUNE)
    validate = validate.cache().shuffle(1000).prefetch(buffer_size = tf.data.AUTOTUNE)
    test = test.cache().shuffle(1000).prefetch(buffer_size = tf.data.AUTOTUNE)
     ```
</details>

#### :three:    Modeling
- Define neural network architecture

- Build model on training dataset and evaluate on train and validate

- Use optimizer to compile

- Fit model on test dataset on evaluate model based on accuracy

- Plot accuracy and loss function of train and validate datasets from all 50 epochs.

- Make prediction on test dataset and save model

- Ajdust neural network architecture and optimizer, using steps above to generate and save new mdoel

- Deploy the top performing model

## Conclusion
The neurol network model has an accuracy of 99% on test dataset, and it's expected to perform with the equivalent accuracy level on future onseen data.

<img width="401" alt="image" src="https://github.com/Sumbati10/Potato-Disease-Classification-Using-CNN/assets/105505214/56eeacbb-2417-45cd-a946-a0471c84d8b8">



# Potato Disease Classifier
A web application to predict the disease in an infected potato plant using it's leaf and Convolutional Neural Networks.<br>


# Run 🎯
### 1. Download or clone the repository
### 2. Open cmd or terminal
### 3. change directory (cd) to `plant-disease-classifier`
### 4. Enter `pip install -r requirements.txt`
### 5. Enter `python app.py`

# Tools✅
**Python 3.7** <br>
**Flask**<br>
**Tensorflow 2.16.1**<br>
**Numpy**<br>
**Matplotlib**<br>
**HTML**<br>
**CSS**<br>
**Bootstrap**<br>
**IDE: VScode**<br>

# Tour!🎯
#### Home page

<img width="958" alt="Screenshot 2024-05-22 223426" src="https://github.com/Sumbati10/Potato-Disease-Classification-Using-CNN/assets/105505214/70e84b94-3f98-4fad-a1d3-ff80aec3af18">



#### About page

![Alt text](<images/Screenshot 2024-05-22 223450.png>)

#### Result page

<img width="545" alt="Screenshot 2024-05-22 222449" src="https://github.com/Sumbati10/Potato-Disease-Classification-Using-CNN/assets/105505214/3ec2e1b3-e905-4559-9a3a-a07877ae14b4">


