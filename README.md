# CSE573-SWM-StockPrediction
Download the Processed CSV and pickle files from: 
https://drive.google.com/drive/folders/1dx7Nq3HDSbSzbnm9BfuLqyUaIOHigdJ1?usp=sharing

Note: Only pickle files are necessary. CSV files are only for reference.

Update from Naveen: I have added one gram features extraction code for both amazon and apple. 
If you just run the 'n-gram-feature-extraction.ipynb' notebook in your local, it would generate the pickle files for features for respective company. That would hardly take 5 mins.

In your local, please directly use the files put up by Abhishek in drive as it takes lots of time in preprocessing.  

Update from Mounavi:
I am adding the link for google collab which contains the code to obtain the tweets data related to stocks of AMZN and AAPL.

https://colab.research.google.com/drive/1uWemb2sNdLnid-GuIsxZecFlqBgYsKEE?usp=sharing

Update from Naveen:
Please update the cumulative info about your test in following sheet: 
https://docs.google.com/spreadsheets/d/1y2zzZLYs_7U2vcR_DQS3VK-J6BWuluwOXD17g_-BP4k/edit?usp=sharing

Update from Nagarjuna:

Tokenized preprocessed data using google news vectors [GloveVectorizeTokens.ipynb]
Trained the tokens on different machine learning models using [model-training-glove-1-day.ipynb and model-training-glove-4-hrs.ipynb]

Update from Mounavi:
To run the html file and get the results please follow the following steps mentioned and the steps being mentioned work on MAC: 
1. Open the terminal and run the command sudo apachectl start.
2. Now run the command sudo nano /etc/apache2/httpd.conf.
3. Delete the # from #LoadModule php7_module libexec/apache2/libphp7.so
4. Now restart the apachet server with the command sudo apachectl restart.
5. Create a folder named Sites in your home directory and copy the working SWM project folder to the Sites folder.
6. Now in terminal run the command sudo nano /etc/apache2/httpd.conf and replace /Library/WebServer/Documents with the path of your Sites folder
7. Restart the apache server again as mentioned on step 4 and you can open the main.html page in Google chrome serving at the localhost 80.


