# IMG Flip and Face Blurring with OpenCV
#### -  Flipping and blurring an img by detecting faces using OpenCV and Python.   

 ---

- #### **Project Overview: Face Recognition and Gaussian Blur Processing using OpenCV**
  >This project focuses on utilizing OpenCV to detect faces in an image and applying Gaussian blur to achieve a smooth effect on the facial regions. The primary goal is to identify and locate faces in the user-provided image, subsequently enhancing the facial features by applying Gaussian blur.

- #### **Features and Highlights**
  >Face detection and position determination using OpenCV
  >Application of Gaussian blur to achieve a smooth effect on facial features
  >Additional functionality to rotate the facial regions, providing a creative twist to the visual effect
  
 - ### **Description and Purpose of this Project**  
   > This project uses OpenCV and Python to detect faces in images and apply blur processing to the corresponding areas. It also goes through the process of flipping the face area and reinserting into the image. These functions can make it difficult to identify individuals, enhancing privacy and data stability. Therefore, it can be used to anonymize faces or protect sensitive information in images. This project provides information on face detection and various image processing, and presents a foundation for wider range of fields.

- ### **Key Points**    
  ##### 1. **Steps**
    > a. Import Image: Use OpenCV to import the target image. 
    > b. Face detection: Use the Haar Cascade classifier to detect faces in images. 
    > c. Blur processing: Apply Gaussian blur processing to the detected face area.
    > d. Flip: Flip the detected face area horizontally.
    > e. Results: The flipped, blurry face will be applied to the original image.
   
  ##### 2. **Assumption**
  > The above code is based on face image detection.
  ##### 3. **Reference object properties**
    > a. Python must be installed.
    > b. OpenCV must be installed.
    > c. The Haar Cascade Classifier file (haarcascade_frontalface_default.xml) must exist.
   >d. A target image file is required to perform face detection and processing.
     (The image file must be located in the same directory as the code, or the image must be in the path specified in the code.)
- ### **Requirements (with versions)**      
  > 1. Python (3.8.13)  
  > 2. OpenCV (4.6.0)  

- ### **Results**  
  ![cha_image](https://github.com/chaete/opencv-python/assets/124789601/4bbb7b60-98de-414e-9689-89039cf3124b)
  ![cha_blur](https://github.com/chaete/opencv-python/assets/124789601/12444c35-5dab-45ec-ab34-1b6e6d6176bf)

  ![go_image](https://github.com/chaete/opencv-python/assets/124789601/290e2497-cd68-483f-a319-f84d0330740c)
  ![go_blur](https://github.com/chaete/opencv-python/assets/124789601/3af48e84-0df1-46d8-a0fe-4cee847306ba)


202133721 박채연 202135425 서혜주 202133725 성윤지 202235130 조혜린
