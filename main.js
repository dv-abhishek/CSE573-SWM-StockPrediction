function validateForm() {
    var news = "'" + document.getElementById("news").value + "'";
    var models = document.getElementsByName('ml_models');
    var model = "";
    for(i = 0; i < models.length; i++) {
        if(models[i].checked){
            model = models[i].value;
        }
    }
    
     var info = new FormData();
     info.append('news', news);
     info.append('ml_model', model);
     
     var xhr = new XMLHttpRequest();
     xhr.open('POST', "/CSE573-SWM-StockPrediction/index.php");
     xhr.onload = function () {
        console.log((this.response))
        $("#demo").html(this.response);
     };
     xhr.send(info);
     return false;
     
  }