# <span style="color:blue">Bosse: Manual Laboring Automation</span>
[![GitHub Repository 1](https://img.shields.io/badge/GitHub-Explore%20the%20Code-blue?logo=github)](https://github.com/NoahMeissner/bosse)

<span style="color:blue">Effortlessly generating datasets without manual labelling, our innovative solution combines the SICK 3D camera, webcam, and ABB GoFa arm, making it ideal for use in production lines.
</span>

## <span style="color:blue">Table of Contents</span>

<details>
  <summary><span style="color:blue">Click to Expand</span></summary>
  <ol>
    <li><a href="#team"><span style="color:blue">Team</span></a></li>
    <li><a href="#abstract"><span style="color:blue">Abstract</span></a></li>
    <li><a href="#how-it-works"><span style="color:blue">How It Works</span></a></li>
    <li><a href="#technologies-used"><span style="color:blue">Technologies Used</span></a></li>
    <li><a href="#advantages"><span style="color:blue">Advantages</span></a></li>
    <li><a href="#acknowledgments"><span style="color:blue">Acknowledgments</span></a></li>
  </ol>
</details>

## <span style="color:blue">Team</span>

<span style="color:blue">Meet the game-changers who brought Bosse to life:</span>

- <span style="color:blue">**Michael Khalfin**</span>
  - <span style="color:blue">Organization: Rice University</span>
  - <span style="color:blue">Email: [mlk15@rice.edu](mailto:mlk15@rice.edu)</span>
  - <span style="color:blue">LinkedIn: [Profile](https://www.linkedin.com/in/michael-khalfin-87551b20b/)</span>

- <span style="color:blue">**Noah Meissner**</span>
  - <span style="color:blue">Organization: University Regensburg</span>
  - <span style="color:blue">LinkedIn: [Profile](https://www.linkedin.com/in/noah-mei%C3%9Fner-7391a2245/)</span>

- <span style="color:blue">**Joseph Wright**</span>
  - <span style="color:blue">Organization: Drexel University</span>
  - <span style="color:blue">Email: [jrw435@drexel.edu](mailto:jrw435@drexel.edu)</span>
  - <span style="color:blue">LinkedIn: [Profile](linkedin.com/in/joseph~wright)</span>

- <span style="color:blue">**Harsh Dhillon**</span>
  - <span style="color:blue">Organization: Magna International</span>
  - <span style="color:blue">Email: [harshpartap2001@gmail.com](mailto:harshpartap2001@gmail.com)</span>
  - <span style="color:blue">LinkedIn: [Profile](https://www.linkedin.com/in/harsh-dhillon-92aa14196/)</span>

- <span style="color:blue">**Jingyan Yang**</span>
  - <span style="color:blue">Organization: Technical University of Denmark</span>
  - <span style="color:blue">Email: [jingyanyang94@gmail.com](mailto:jingyanyang94@gmail.com)</span>
  - <span style="color:blue">LinkedIn: [Profile](https://www.linkedin.com/in/jingyan-yang/)</span>

### <span style="color:blue">Abstract</span>

<span style="color:blue">As an logistics worker, your crucial responsibility is to track and ship a wide range of products. Traditionally, this involved labor-intensive tasks like manually labeling images by outlining objects, which could eat up hours of your day or necessitate additional staff.

But now, enter Bosse, the innovation of the future. With Bosse, we've automated this entire process. As products glide down the production line, a precision robotic arm gracefully rotates and captures them from multiple angles. Using cutting-edge technology like computer vision and a 3D camera, Bosse swiftly identifies object coordinates with precision. Your role as a logistics worker? Just answer a few quick questions about the type of object – Bosse's advanced technology handles the rest. It ensures objects are never scanned twice, and deep learning is automatically applied for future identifications.

Bosse: simplifying logistics, streamlining your work, and optimizing efficiency – all in a day's work. </span>

### <span style="color:blue">How It Works</span>

[![Demo](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=(https://youtu.be/PGkN7vxiy3s))


<span style="color:blue">We ensure precision in our image processing by capturing objects from multiple angles. Our cutting-edge computer vision technology automates the task of outlining objects by identifying approximately 500 high-contrast points in each image. To enhance accuracy, we eliminate outlier points, retaining only those that contribute to forming lines or curves.

We input roughly 50 images per object, each of which features labeled regions of interest, into the Ultralytics YOLOv8 Nano model. This model utilizes a small batch size of 1 and is trained over 4 epochs, a careful approach to avoid overfitting the region of interest. This strategy optimizes key metrics such as precision-recall, confidence, and loss.

With this method, we ensure that we never segment the same image twice, and our deep learning model, securely stored locally on your device, is applied seamlessly during future encounters with the object. This meticulous process assures unparalleled accuracy, guaranteeing that your shipments meet the highest quality standards.</span>

### <span style="color:blue">Technologies Used</span>

<span style="color:blue">Bosse was developed using a powerful combination of technologies, including:</span>
- <span style="color:blue">**Python**: Python was the main language we used for our frontend and backend.</span>
- <span style="color:blue">**PyQt6**: PyQt6 was our native GUI toolkit of choice.</span>
- <span style="color:blue">**Robot Operating System (ROS) & Raspberry Pi**: ROS and a Raspberry Pi Model 4B were used for connecting devices across a 5G network.</span>
- <span style="color:blue">**3D Camera & Webcam**: The Visionary-T Mini camera, sponsored by SICK, was responsible for imaging the object every 4 seconds; then we could view the output using a webcam.</span>
- <span style="color:blue">**ABB GoFa Arm**: The arm, sponsored by ABB, rotated the object in front of the camera, completing the hardware stack.</span>

### <span style="color:blue">Advantages</span>
- **Enhanced Efficiency:** Our innovative approach streamlines the image capture and object outlining process, saving valuable time and reducing manual effort.
- **Precision and Reliability:** Our computer vision technology ensures meticulous identification of key points, resulting in highly accurate object segmentation and reduced errors.
- **Optimized Model Training:** By carefully managing batch sizes and epochs, our Ultralytics YOLOv8 Nano model achieves optimal performance, enhancing precision, recall, and overall accuracy.
- **Elimination of Redundancy:** Our approach guarantees that the same image is never segmented twice, preventing duplication and ensuring an efficient workflow.
- **Local Deep Learning Integration:** The locally stored deep learning model simplifies future object identifications, contributing to a seamless and efficient process.
- **High-Quality Shipments:** The result of our meticulous process is impeccable shipments that consistently meet the highest quality standards.
- **Dynamically Sample Products:** Painlessly generate new input for the model if it hasn't seen the object before.
- **Transparent Analysis and Communication:** We maintain a commitment to transparency by providing users with insights into our processes, ensuring you have a clear understanding of the technology and its applications.

### <span style="color:blue">Acknowledgments</span>
We would like to thank the SICK Solution Hackathon team and all the corporate sponsors at this event. We had a blast spending the week at the SICK SIA Campus, 
AG Distribution Center, and Super8 Hotel. The Hackathon was a wonderful opportunity to work with people from around the world specializing in a variety of disciplines.
Additionally, we would like to thank the coaches, who helped a lot, and our family, friends, and mentors who supported us through this journey.
