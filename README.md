# Bangkit, Assignment#5
This is our team's repository for completing on the fifth assignment about MLCC of Bangkit Course.

Our member are:
1. R. Arif Firdaus Lazuardi
2. Kadek Suar Wibawa
3. I Komang Tryana Mertayasa

## Directory Structure 
- dataset
  - mnist
- doc
- source
  - mnist
- workspace
  - notebook
  - cli

Explanation:
- dataset = mnist dataset that has been downloaded. Local use purpose.
- doc = snaps note and for put all docs about our code
- source = classes/moudules/functions can be used in multiple workspaces
- workspace/notebook = all of jupyter notebook files (save as google colab as notebook)
- workspace/cli = all of cli (command line interface) apps


## runing and testing on google colabs.
Create Colab on Google Drive :
 - On google drive, click New --> More --> Google Colaboratory 
 - Running colab, Right click *.ipynb --> open with --> Colaboratory 
 - GPU Setup, from menubar click Edit --> netbook settings --> on Hardware accelerator choose GPU --> Save

Clone project into drive for archive
 - On Google colab rung script : !git clone https://github.com/your-username/your-project.git 'drive/My Drive/your-path' --> click run
 
Running project into colab
 - Select your *.ipynb project specific your path project workspace -- notebook --> biginner.ipynb --> right click --> open with     
   google colaburatory
 - running scrip from google.colab import drive drive.mount('/content/drive/your porject') --> go to url browser and select your google    acount and allow to access drive --> copy code authorize and enter
 - Select runtime on menu bar and run all

Running result
Epoch 1/5
1875/1875 [==============================] - 4s 2ms/step - loss: 0.2990 - accuracy: 0.9128
Epoch 2/5
1875/1875 [==============================] - 4s 2ms/step - loss: 0.1438 - accuracy: 0.9576
Epoch 3/5
1875/1875 [==============================] - 4s 2ms/step - loss: 0.1073 - accuracy: 0.9674
Epoch 4/5
1875/1875 [==============================] - 4s 2ms/step - loss: 0.0893 - accuracy: 0.9720
Epoch 5/5
1875/1875 [==============================] - 4s 2ms/step - loss: 0.0756 - accuracy: 0.9765
<tensorflow.python.keras.callbacks.History at 0x7f14938dd048>

The image classifier is now trained to ~98% accuracy on this dataset


