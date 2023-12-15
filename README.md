# IMG Face Blurring with OpenCV
#### - Blurring and intensity control of blur an img by detecting faces using OpenCV and Python. 

 ---   

 ### Contents   

 1. [Description and purpose of this project](#Description-and-purpose-of-this-project)
 2. [Key Points](#Key-Points)
 3. [Requirements (with versions)](#Requirements-(with-versions))
 4. [Results](#Results)

 - ### **Description and purpose of this project** 
> This project uses OpenCV and Python to detect faces in images and apply blur processing to those areas. In addition, we have added the ability to control the intensity of blur using shortcuts, as well as just blur processing. These functions make it difficult to identify people, which can increase privacy and data stability. Therefore, they can be used to anonymize faces or protect sensitive information in images. The project provides information on face detection and various image processing, and provides a foundation for a wider range of areas.

- ### **Key Points**    
  ##### 1. **Steps**
    > a. Import Image
    > - Use OpenCV to import the target image.
    > - Convert the imported image to black and white (cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)).  
    >
    > b. Face detection
    > - Use the Haar Cascade classifier to detect faces in images.
    >
    > c. Mouse Envent
    > - Register the 'mouse_callback'function to handle mouse click events.
    > - When the left mouse button is clicked, it identifies the face area associated with the clicked image and stores the index in the selected_face variable.
    > 
    > d. Blur processing
    > - The adjust_blur_strength function is defined so that blur processing may be performed on the selected area by applying the Gaussian effect.
    > - Apply the blur effect only to the selected face and apply it only if the face area is clicked.
    > 
    > e. Key Event
    > - 'q' key is pressed, exit the program.
    > - 'b' key is pressed, decrease the blur intensity
    > - 'n' key is pressed, increase it.
  ##### 2. **Assumption**
    > The above code is based on face image detection.
  ##### 3. **Reference object properties**
    > a. Python must be installed.  
    > b. OpenCV must be installed.  
    > c. The Haar Cascade Classifier file (haarcascade_frontalface_default.xml) must exist.  
    > d. A target image file is required to perform face detection and processing.  
     (The image file must be located in the same directory as the code, or the image must be in the path specified in the code.)
- ### **Requirements (with versions)**      
  > 1. Python (3.8.13)  
  > 2. OpenCV (4.6.0)
- ### **Results**  
  ![cha_image](https://github.com/chaete/opencv-python/assets/124789601/4bbb7b60-98de-414e-9689-89039cf3124b)
  ![cha_blur](https://github.com/chaete/opencv-python/assets/144206101/c6e160e9-e82d-4d2d-afa1-1fa7d6e260c1)
  ![cha_gif](https://github.com/chaete/opencv-python/assets/144206101/1e32578c-edbc-4d99-bef6-3fbf652ed0cd)


202133721 박채연 202135425 서혜주 202133725 성윤지 202235130 조혜린
