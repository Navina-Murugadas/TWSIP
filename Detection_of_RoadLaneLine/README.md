# DETECTION OF ROAD LANE LINES
Road lane line detection using OpenCV is a fundamental component of many autonomous vehicle systems. This project demonstrates the practical application of computer vision techniques in enhancing road safety and improving the driving experience by assisting drivers in staying within their lanes. It also serves as a foundation for more advanced projects in the field of autonomous driving and ADAS.
The project aims to develop a system that can automatically detect and highlight road lane lines in images or videos using computer vision techniques. This system can be a crucial component in autonomous vehicles and lane-keeping assistance systems.

# Tools/Technologies used:
1. Jupyter Notebook
2. Python language
3. Numpy library
4. Pandas - Data Cleaning
5. Matplotlib - Data Visualization
6. OpenCV - Open Source Computer Vision Library
7. Gray Scale
8. Gaussian Smoothing
9. Canny Edge Detector
10. Region of Interest Masking
11. Hough Transform

# Prerequisites:
1. A prior knowledge of Python programming language along with its libraries for data science such as Numpy, Pandas, Matplotlib, Seaborn, SkLearn is needed.
2. Knowledge of OpenCV, Gaussian Smoothing, Canny Edge Detection, Region of Interest, Hough Transform
3. Installation of required libraries

# Process:
1. GRAY SCALE CONVERSION: Convert the images to grayscale to simplify processing.
2. GAUSSIAN SMOOTHING: Apply Gaussian blur to reduce noise and smooth the image.
3. CANNY EDGE DETECTION: Detect edges in the image using the Canny edge detector.
4. REGION OF INTEREST (ROI) MASKING : Define a polygon mask to isolate the region where lane lines are expected.
5. HOUGH TRANSFORM: Apply the Hough Transform to detect lines or line segments in the ROI.
6. LINE FILTERING: Filter and group the detected lines based on slope and position to identify left and right lane lines.
7. LINE EXTRAPOLATION: Extend the detected line segments to cover the full length of the lane lines.
8. VISUALIZATION: Draw the detected lane lines on the original image or video frames.

# Output:
![Road1](https://github.com/Navina-Murugadas/TWSIP/assets/72821323/b2da4d70-66c1-4379-ad8c-fef04460e3c6)
![Road2](https://github.com/Navina-Murugadas/TWSIP/assets/72821323/484733b4-6000-40b2-9745-45a545b84437)
![Road3](https://github.com/Navina-Murugadas/TWSIP/assets/72821323/07adcbfd-5812-4e55-8cdd-69c3409ffc60)
![Road4](https://github.com/Navina-Murugadas/TWSIP/assets/72821323/bcbd9c56-ace9-4b2c-bc7a-7647442e8f0e)
![Road5](https://github.com/Navina-Murugadas/TWSIP/assets/72821323/faeb3cc0-f030-4aed-9220-f6ce8947e811)
![Road6](https://github.com/Navina-Murugadas/TWSIP/assets/72821323/01aea8de-5cf8-444e-81d0-dcf1d9cc95c2)
![Road7](https://github.com/Navina-Murugadas/TWSIP/assets/72821323/966fb03f-d877-4050-8cbf-5c3324082610)


