For prediction, dump the input news article in 'test-input.txt' and then inside the current directory, simply run the following command:

python predict.py

Note: The predict.py testing script expects the following trained model pickle files in 'model-training' directory
1. logistic_regression-pca-one-gram-one-day-mixed-data-model.pkl
2. random_forest-XGBoost-pca-one-gram-one-day-mixed-data-3k-30-model.pkl
3. random-forest-pca-one-gram-one-day-mixed-data-model.pkl
4. svm-pca-one-gram-one-day-mixed-data-model.pkl

The sizes of these trained models are in GBs so they could not be uploaded to git repo. These files can be instead downloaded from the following drive link: (permission granted for ASU logins only)
https://drive.google.com/drive/folders/15vqLDwFREx9gX7kcnJb68MgI4W20J0iF?usp=sharing