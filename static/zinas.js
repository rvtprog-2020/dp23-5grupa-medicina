let datums = document.getElementById("datums");
let virsraksts = document.getElementById("virsraksts");
let bilde = document.getElementById("bilde");
let zinasAdd = document.getElementById("zinasAdd");
let zinas = document.getElementById("zinas");
console.log("datums")
zinasAdd.addEventListener("click", function(){
    zinas.innerHTML ="<li> <h4>5. novembris</h4> <img src="+bilde+"> </li>"
    datums.value = "";
    virsraksts.value = "";
    bildesUrl.value = "";
});
