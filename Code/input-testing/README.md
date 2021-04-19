For prediction, dump the input news article in 'test-input.txt' and then inside the current directory, simply run the following command:

python predict.py

Note: The following testing script expects the following trained model pickle files in model-training-and-testing directory
1. logistic_regression-pca-one-gram-one-day-mixed-data-model.pkl
2. random_forest-XGBoost-pca-one-gram-one-day-mixed-data-3k-30-model.pkl
3. random-forest-pca-one-gram-one-day-mixed-data-model.pkl
4. svm-pca-one-gram-one-day-mixed-data-model.pkl

The sizes of these trained models is in GBs so they could not been uploaded to git repo. These files can be instead downloaded from following drive link:
https://drive.google.com/drive/folders/15vqLDwFREx9gX7kcnJb68MgI4W20J0iF?usp=sharing