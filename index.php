<?php
$text = $_POST["news"];
$model = $_POST["ml_model"];
//echo("/Users/mounavi/opt/anaconda3/bin/python /Users/mounavi/Sites/CSE573-SWM-StockPrediction/Code/input-testing/predict.py $text $model 2>&1");
exec("/Users/mounavi/opt/anaconda3/bin/python /Users/mounavi/Sites/CSE573-SWM-StockPrediction/Code/input-testing/predict.py $text $model 2>&1", $output);
//exec('pwd 2>&1', $output);
print_r(end($output));
?>
