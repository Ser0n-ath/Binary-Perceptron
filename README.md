# Binary-Perceptron

 Introduction
This interactive tool that lets you determine whether a given a color is bright or dim. The input is a rgb value and the output is determined by a single layer perceptron.
This is esentially a linear classifier with 2 classes (Bright or Dim).

Options:
-You can add you're own training data/set a custom model or use the pretrained model, and evaluate a colors to see if they are bright/dim using the built-in color picker. 
-A confusion matrix is also included in the app that tells you "how well" ur model does. 

Testing Data Format:
If you are applying your own testing data then provide a .txt file with with the RGB values on each line. Note: Invalid data formats will result in a failure prompt.
Example:
101 20 11
251 01 255
11 14 1
44 11 11

Output: You will get a .txt file with the the prediction result appended to the end of each line for example
101 20 11 1
251 01 255 -1
11 14 1 -1
44 11 11 -1

How the model works: 
:todo

How the interactive tool works: 
:todo

API Calls:
:todo


Libraries Used:

