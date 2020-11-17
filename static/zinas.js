let button = document.getElementById("zinasAdd");
let bilde = document.getElementById("bilde");
let virsraksts = document.getElementById("virsraksts");
let zinas = document.getElementById("zinas");
let datums = document.getElementById("datums");
button.addEventListener("click", function(){
    //foratejums
    let datumsValue = "<h5 style='text-color:gray;'>"+datums.value+"<h5>"
    let bildeValue = "<img src="+bilde.value+" style='height:100px;'>"
        
        //izvada visu kas tika izveidots augsa:
            let kopa = datumsValue + bildeValue
            let jaunsElements = document.createElement("li")
            jaunsElements.innerHTML = kopa;
            zinas.appendChild(jaunsElements);
            console.log("vēl strādā")
            
});
