This project was inspired by my attempt to directly access form responses stored in a google form for my Image Processing Assignment(for more details go to Academics section--> Image Processing)

Since my attendance project was based on a Colab file, I wanted to access the form through colab. Accessing form responses, however, is not straightforward. First we must have a google cloud account. Then we need to open a project in that account. After that we need to enable the Forms API and then obtain the credentials.json to enable us to access forms through our local system.

However, colab is not any system. Hence, the flow that works on our local system may not necessarily work on colab. This is precisely what happened here. I could not access forms API because the credentials flow does not occur properly in colab. However I could successfully connect to forms api through my local system. The Localsystem.py file contains the code that did this. 

Basically, after a successful credentials flow(authorization), the authorization service gives us a set of credentials to access the service. I could get the credentials in my local system but not in colab. Hence, I decided to use a simple logic: Transfer the credentials from my local system to colab.

To do that, we simply make use of the pickle moduly in python, which is used to store data structures. Since our credentials is also a data structure, I simply dump those credentials into a pickle file. I then upload that file onto colab and then load those credentials without having to perform credentials flow. That's it! I now have access to forms API in Colab. Not just forms API but a wide variety of services which may otherwise not be available on colab due to its nature can now be used. However it is obvious that this is a security concern; having your credentials unsecured. Hence this must be performed personally and not with any other person.

The two images show the output of the colab file.
