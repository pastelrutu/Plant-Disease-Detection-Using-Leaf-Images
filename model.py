import os
import cv2
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

def load_dataset(path):
    images=[]
    labels=[]
    classes=os.listdir(path)
    print(classes)
    print("Total Classes: ",len(classes))

    for folder in classes:
        folder_path=os.path.join(path,folder)
        if not os.path.isdir(folder_path):
            continue
        print(folder,":",len(os.listdir(folder_path)))
        for image_name in os.listdir(folder_path):
            image_path=os.path.join(folder_path, image_name)
            image=cv2.imread(image_path)
            if image is None:
                print("Skipped:", image_path)
                continue
            image=cv2.resize(image,(128,128))
            images.append(image)
            labels.append(folder)
    return images,labels


#Training & Testing Dataset============

dataset_path=r"C:/Users/mrutu/OneDrive/Desktop/Plant_Disease/Dataset"

images,labels=load_dataset(dataset_path)

print("Total Images:",len(images))
print("Total Labels:",len(labels))


# Split Dataset into Training and Testing

x_train,x_test,y_train,y_test=train_test_split(
    images,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)

print("Train Images:",len(x_train))
print("Train Labels:",len(y_train))

print("Test Images:",len(x_test))
print("Test Labels:",len(y_test))


# Convert Training Images

x_train=np.array(x_train)
x_train=x_train/255.0

print("Minimum Pixel Value: ",x_train.min())
print("Maximum Pixel Value: ",x_train.max())


# Convert Testing Images

x_test=np.array(x_test)
x_test=x_test/255.0


# Label Encoding

le=LabelEncoder()

y_train=le.fit_transform(y_train)
y_test=le.transform(y_test)

print("Classes:",le.classes_)
print("Total Classes:",len(le.classes_))

num_classes=len(le.classes_)


#Model CNN Section====

model=Sequential([
    Conv2D(32, kernel_size=(3,3), activation="relu", input_shape=(128,128,3)),
    MaxPooling2D(pool_size=(2,2)),        
    Conv2D(64,activation="relu", kernel_size=(3,3)),
    MaxPooling2D(pool_size=(2,2)),  
    Flatten(),
    Dense(128,activation="relu"),
    Dense(num_classes,activation="softmax")
])

#Compile & Fit Model ======

model.summary()
model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])
model.fit(x_train,y_train,epochs=10)

test_loss,test_accuracy=model.evaluate(x_test,y_test)
print("Test Loss :", test_loss)
print("Test Accuracy :", test_accuracy)


#predicting by one image

image=cv2.imread(r"C:/Users/mrutu/OneDrive/Desktop/Plant_Disease/corn_rust_disease.png")
image=cv2.resize(image,(128,128))
image=image/255.0
image=np.expand_dims(image,axis=0)
prediction=model.predict(image)
predicted_class=np.argmax(prediction)
print("Prediction Probabilities: ",prediction)
print("Predicted Disease: ",le.inverse_transform([predicted_class])[0])


#Saving model

model.save("Plant_Disease_Model.keras")
print("Model Saved Successfully!")