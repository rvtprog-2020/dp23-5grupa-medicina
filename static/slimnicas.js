






























let selectedRow = null
function onFormSubmit() {
        let formData = readFormData();
        if (selectedRow == null)
            insertNewRecord(formData);
        else
            updateRecord(formData);
        resetForm();
    }

function readFormData() {
    let formData = {};
    formData["slimnica12"] = document.getElementById("slimnica12").value;
    formData["location12"] = document.getElementById("location12").value;
    formData["darbalaikssakums"] = document.getElementById("darbalaikssakums").value;
    formData["darbalaiksbeigas"] = document.getElementById("darbalaiksbeigas").value;
    return formData;
}
function insertNewRecord(data) {
    let table = document.getElementById("slimtabula").getElementsByTagName('tbody')[0];
    let newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.slimnica12; 
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.location12;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.darbalaikssakums + data.darbalaiksbeigas;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = `<button class="b1" onClick="onEdit(this)">Rediģēt</button>
                       <button class="b1" onClick="onDelete(this)">Dzēst</button>`;
    
}

function resetForm() {
    document.getElementById("slimnica12").value = "";
    document.getElementById("location12").value = "";
    document.getElementById("darbalaikssakums").value = "";
    document.getElementById("darbalaiksbeigas").value = "";
    selectedRow = null;
}

function onEdit(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("slimnica12").value = selectedRow.cells[0].innerHTML;
    document.getElementById("location12").value = selectedRow.cells[1].innerHTML;
    document.getElementById("darbalaikssakums").value = selectedRow.cells[2].innerHTML;
    document.getElementById("darbalaiksbeigas").value = selectedRow.cells[2].innerHTML;
}
function updateRecord(formData) {
    selectedRow.cells[0].innerHTML = formData.slimnica12;
    selectedRow.cells[1].innerHTML = formData.location12;
    selectedRow.cells[2].innerHTML = formData.darbalaikssakums;
    selectedRow.cells[2].innerHTML = formData.darbalaiksbeigas;
}
function onDelete(td) {
    if (confirm('Vai jūs esat pārliecināts, ka vēlaties izdzēst šo ?')) {
        row = td.parentElement.parentElement;
        document.getElementById("slimtabula").deleteRow(row.rowIndex);
        resetForm();
    }
}
