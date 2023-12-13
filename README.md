# IMG Face Blurring with OpenCV
#### - Blurring and intensity control of blur an img by detecting faces using OpenCV and Python. 

 ---

 - ### **Description and purpose of this project** 
> This project uses OpenCV and Python to detect faces in images and apply blur processing to those areas. In addition, we have added the ability to control the intensity of blur using shortcuts, as well as just blur processing. These functions make it difficult to identify people, which can increase privacy and data stability. Therefore, they can be used to anonymize faces or protect sensitive information in images. The project provides information on face detection and various image processing, and provides a foundation for a wider range of areas.

- ### **Key Points**    
  ##### 1. **Steps**
    > a. Import Image: Use OpenCV to import the target image.
    >                  Convert the imported image to black and white (cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)).
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
