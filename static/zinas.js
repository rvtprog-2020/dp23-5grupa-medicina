let button = document.getElementById("zinasAdd");
let bilde = document.getElementById("bilde");
let virsraksts = document.getElementById("virsraksts");
let zinas = document.getElementById("zinas");
let datums = document.getElementById("datums");
let adminbutt = document.getElementById("adminbutt");
let admindiv = document.getElementById("adminDiv");
let tirit = document.getElementById("tirit");
let irzinas = [];
tirit.addEventListener("click", function(){
    console.log("poga vel strada")
    zinas.removeChild(zinas.lastChild);
})
adminbutt.addEventListener("click", function(){
if (admindiv.style.display === "none"){
    admindiv.style.display = "block";
    tirit.style.display = "block";
}  else {
    admindiv.style.display = "none";
    tirit.style.display = "none";
}

})
//    button.addEventListener("click", function(){
//        //foratejums
//        let datumsValue = "<h5 style='text-color:gray;'>"+datums.value+"<h5>"
//        let bildeValue = "<img src="+bilde.value+" style='height:100px;'>"
//        let virsrakstsValue = "<h5 style='font-size:20px; text-color:gray;'>"+virsraksts.value+"<h5>"
//        let actkopa = ""
//           //izvada visu kas tika izveidots augsa:
//                let kopa = datumsValue + virsrakstsValue + bildeValue 
//                let jaunsElements = document.createElement("li")
//                jaunsElements.innerHTML = kopa;
//                zinas.appendChild(jaunsElements);
//                console.log("vēl strādā")
//                myStorage = window.localStorage;
//                localStorage.setItem(zinas);
//    });

button.addEventListener("click", function(){
    let zina = {
        zinDatums = datums.value,
        zinVirsraksts = virsraksts.value;
        zinBilde = bilde.value;
    }
    irzinas.push(zina);
})