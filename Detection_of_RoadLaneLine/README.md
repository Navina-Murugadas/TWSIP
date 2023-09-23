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
