We decided to make a Chatbot for our AI assignment. Like any standard chatbot, we made use of NLP. However the difference was that we had to make our chatbot contextual that is it must remember the intent behind the conversation. For example, if we ask to the chatbot what is the weather today? And then we simply ask tomorrow? Then the chatbot must understand that we have asked tomorrow in the context of weather and hence it must read out forecasts. 

The chatbot presented here tries to present this concept. The idea was taken from this link:

https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077

To make the chatbot truly contextual we would require a really huge dataset, so to demonstrate this concept we included one example: are you open today? Then type tomorrow? You will see that chatbot answers appropriately.

Otherwise, the chatbot does a fantastic job by using NLP to recognize which question the user is asking. This is done using a neural network classifier. Vikas helped to make training faster by using log error measure instead of simple error measure which I used earlier. But it was a big headache for me to get the code in tflearn given in the article to keras.

The dataset in this case is the intents.json file prepared by Shreyas along with Vikas and Shashank. It is then retrieved and processed by the chat_bot.ipynb file. I chose colab because it provides tensorflow preinstalled and hence we can avoid the hassles of installing it on our own system. 

The problem with tensorflow is that it is too big(1GB) to fit in any web server. For instance I deployed the back end of the chatbot in python anywhere which provides a storage capacity of only 512MB. Hence I converted the deep learning model into a tflite model which is essentially a lightweight model for use on devices or web servers. 

What I did was to seperate the backend and frontend of the chatbot. This makes development easier since the components are decoupled and hence easier to modify and debug. I can change the backend(that is the model) without changing the view and vice versa. Besides we simply integrate the frontend into any website and hence the system is portable. That is the reason why I deployed the model on a web server and designed a frontend that communicates with the model. The frontend folder contains the files that forms the frontend. To check the chatbot, simply download 
