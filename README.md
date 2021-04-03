# CSE573-SWM-StockPrediction
Download the Processed CSV and pickle files from: 
https://drive.google.com/drive/folders/1dx7Nq3HDSbSzbnm9BfuLqyUaIOHigdJ1?usp=sharing

Note: Only pickle files are necessary. CSV files are only for reference.

Update from Naveen: I have added one gram features extraction code for both amazon and apple. Not uploading corresponding pickle file in drive because of its huge size. If you just run the 'n-gram-feature-extraction.ipynb' notebook in your local, it would generate the pickle files for features for respective company. That would hardly take 5 mins.

The two-gram feature extraction is working only for amazon data for now. It is failing for apple because of huge size of resultant dataset. I am still trying to find some workaround to get this ready. Use Amazon two-gram features till then. 
