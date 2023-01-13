This project was inspired by my attempt to directly access form responses stored in a google form for my Image Processing Assignment(for more details go to Academics section--> Image Processing)

Since my attendance project was based on a Colab file, I wanted to access the form through colab. Accessing form responses, however, is not straightforward. First we must have a google cloud account. Then we need to open a project in that account. After that we need to enable the Forms API and then obtain the credentials.json to enable us to access forms through our local system.

However, colab is not any system. Hence, the flow that works on our local system may not necessarily work on colab. This is precisely what happened here. I could not access forms API because the credentials flow does not occur properly in colab. However I could successfully connect to forms api through my local system. The Localsystem.py file contains the code that did this. 

