# CSE573-SWM-StockPrediction
Download the Processed CSV and pickle files from: 
https://drive.google.com/drive/folders/1dx7Nq3HDSbSzbnm9BfuLqyUaIOHigdJ1?usp=sharing

Note: Only pickle files are necessary. CSV files are only for reference.  

Link for google collab which contains the code to obtain the tweets data related to stocks of AMZN and AAPL:
https://colab.research.google.com/drive/1uWemb2sNdLnid-GuIsxZecFlqBgYsKEE?usp=sharing

To run the testing UI and get the results please follow the following steps: (Tested on Mac PC) 

0. To use the trained models directly, please ensure that you have downloaded the trained models' pickle files as mentioned in './Code/input-testing/' folder readme.
1. Open the terminal and run the command sudo apachectl start.
2. Now run the command sudo nano /etc/apache2/httpd.conf.
3. Delete the # from #LoadModule php7_module libexec/apache2/libphp7.so
4. Now restart the apachet server with the command sudo apachectl restart.
5. Create a folder named Sites in your home directory and copy the working SWM project folder to the Sites folder.
6. Now in terminal run the command sudo nano /etc/apache2/httpd.conf and replace /Library/WebServer/Documents with the path of your Sites folder
7. Restart the apache server again as mentioned on step 4 and you can open the main.html page in Google chrome serving at the localhost 80.


