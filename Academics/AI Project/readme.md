## Update: LocalSystem.py file now automatically extracts credentials after authentication flow and stores it in the required directory.

Convert audio to text(google assistant) and then display.

Like any standard chatbot, I made use of NLP. HoIver the difference was that I had to make our chatbot contextual that is it must remember the intent behind the conversation. For example, if I ask to the chatbot what is the weather today? And then I simply ask tomorrow? Then the chatbot must understand that I have asked tomorrow in the context of weather and hence it must read out forecasts. 

The chatbot presented here tries to present this concept. The idea was taken from this link:

https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077

To make the chatbot truly contextual I would require a really huge dataset, so to demonstrate this concept I included one example: are you open today? Then type tomorrow? The chatbot responds contextually in the context of 'day' i.e. open that day or not(Refer intents.json for one question I have context-set:"day" and for another I have context-filter:"day"). Like this I can add more contextual information.

Otherwise, the chatbot does a fantastic job by using NLP to recognize which question the user is asking. This is done using a neural network classifier. it was difficult to get the code in tflearn given in the article to keras.

The dataset is retrieved and processed by the chat_bot.ipynb file. I chose colab because it provides tensorflow preinstalled and hence I can avoid the hassles of installing it on our own system. 

The problem with tensorflow is that it is too big(1GB) to fit in any web server. For instance I deployed the back end of the chatbot in python anywhere which provides a storage capacity of only 512MB. Hence I converted the deep learning model into a tflite model which is essentially a lightIight model for use on devices or Ib servers. 

What I did was to seperate the backend and frontend of the chatbot. This makes development easier since the components are decoupled and hence easier to modify and debug. I can change the backend(that is the model) without changing the view and vice versa. Besides I simply integrate the frontend into any website and hence the system is portable. That is the reason why I deployed the model on a web server and designed a frontend that communicates with the model. The frontend folder contains the files that forms the frontend. To check the chatbot, simply download the frontend.zip file and extract it. Then open the base.html and you will find the chatbot button at bottom right. You can then experiment with it.

At first it was just a matter of loading the tflite model along with other files such as c.pkl for reloading the classes, i.pkl for intents and w.pkl for words. And then using flask to obtain requests from the user, calling the model and then returning the response to the user. I used this tutorial for achieving this:

https://github.com/patrickloeber/chatbot-deployment

Steps in pythonanywhere console. Very important to use python 3.9 only since tflite not there for 3.10. Flask cors is for cross origin requests required to access the backend from anywhere in the world:

mkvirtualenv --python=3.9 name_of_virtualenv

pip install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime

pip install Flask-Cors

I remembered Google Assistant; how it handles informal discussions to quite a good extent. I thought why not leverage this existing feature? Thus I integrated google assistant into the web app. To do this involved a number of steps. Followed this tutorial:

https://developers.google.com/assistant/sdk/guides/service/python

The standard google tutorial for integrating google assistant making use of the command: google-oauthlib-tool --client-secrets ..... is outdated due to the below problem:

https://developers.googleblog.com/2022/02/making-oauth-flows-safer.html#dates-oob

Hence in order to solve that problem, I used the code of my CloudAPI colab project to generate credentials. Refer LocalSystem.py. HoIver the crdentials generated are different from those obtained by google oauthlib tool. I found this out while trying to run the sample code in the tutorial. I also found out that I must place the credentials in a specific direcort determined by the address in: google-oauthlib-tool --help. I placed the credentials there, ran the sample code again and again to determine the differences betIen them, deleted several fields and finally obtained the required file. 

'access_token', 'client_id', 'client_secret', 'refresh_token', 'token_expiry', 'token_uri', 'user_agent', 'revoke_uri', 'id_token', 'id_token_jwt', 'token_response', 'scopes', 'token_info_uri', 'invalid', '_class', '_module'  ---> initial file

'client_id', 'client_secret', 'refresh_token', 'token_uri', 'id_token', 'scopes'  ---> final file. 

This is the file that I eventually placed in my python anywhere web server in the location determined by google outhlib tool. Then there is no need to perform credential flow and hence the assistant is ready to be used. However, some error related to version may throw up. I used these to solve:

pip install --upgrade click
pip install protobuf==3.19.6

Then I also had to modify the google samples library(especially to the textInput.py file)

In python anywhere I had to make certain modifications to the google samples library itself. The textInput and browser_helpers files that I had in my local system are missing there. Hence I added it there. Then I again had to modify the textInput file with respect to the installation in python anywhere. Finally, I was able to integrate google assistant into my web app. There was just one catch. Since google assistant is originally used to deal with voice inputs and return voice output, all text questions may not be responded to. There may be just a blank response. 

One day in youtube I hit upon ChatGPT. I was easily able to integrate ChatGPT into my webapp. The above limitation of google assistant is easily overcome but the catch here is that the service of ChatGPT expires after a free trial.

The final web app is given by the final_app.py file. Hence this project tested my developer skills to the extreme while also taught me an ocean of concepts like ML, Keras, pickle, tflite, flask, google assistant, google cloud, virtual environment, modifying packages, learning about colab, OAuth and credentials flow. 

The chatbot is now integrated with my website at the bottom right corner:

http://roger123.pythonanywhere.com/

I trained the Chatbot using the tango_intents.json. Tango refers to my Django Ibsite mentioned in the above link.

You can ask the following questions.
1. website info
2. frontend
3. backend
4. framework
5. Features
6. deployment
7. Purpose
8. Developer
<p>To test its contextuality you can ask about deployment. For example type where is the website deployed? Then type why? The chatbot answers the question in the context of deployment.</p>
<p>If you ask any other question, then based on the words the chatbot will either take it to be a question related to one of the above categories or it will activate ChatGPT(or Google Assistant depending on Availability) to try to answer the question. For example if you ask FIFA scores, it will answer to you like the normal assistant. Hence the chatbot is a best effort QA service.</p>

python -m googlesamples.assistant.grpc.textinput --device-model-id <device_model_id> --device-id .
