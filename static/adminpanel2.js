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
    formData["slimnica22"] = document.getElementById("slimnica22").value;
    formData["profesija"] = document.getElementById("profesija").value;
    formData["arstavards"] = document.getElementById("arstavards").value;
    formData["arstalaiks"] = document.getElementById("arstalaiks").value;
    return formData;
}
function insertNewRecord(data) {
    let table = document.getElementById("arstainfo11").getElementsByTagName('tbody')[0];
    let newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.slimnica22; 
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.profesija;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.arstavards;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.arstalaiks;
    cell5 = newRow.insertCell(4);
    cell5.innerHTML = `<button class="b1" onClick="onEdit(this)">Rediģēt</button>
                       <button class="b1" onClick="onDelete(this)">Dzēst</button>`;
    
}

function resetForm() {
    document.getElementById("slimnica22").value = "";
    document.getElementById("profesija").value = "";
    document.getElementById("arstavards").value = "";
    document.getElementById("arstalaiks").value = "";
    selectedRow = null;
}

function onEdit(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("slimnica22").value = selectedRow.cells[0].innerHTML;
    document.getElementById("profesija").value = selectedRow.cells[1].innerHTML;
    document.getElementById("arstavards").value = selectedRow.cells[2].innerHTML;
    document.getElementById("arstalaiks").value = selectedRow.cells[3].innerHTML;
}
function updateRecord(formData) {
    selectedRow.cells[0].innerHTML = formData.slimnica22;
    selectedRow.cells[1].innerHTML = formData.profesija;
    selectedRow.cells[2].innerHTML = formData.arstavards;
    selectedRow.cells[3].innerHTML = formData.arstalaiks;
}
function onDelete(td) {
    if (confirm('Vai jūs esat pārliecināts, ka vēlaties izdzēst šo ?')) {
        row = td.parentElement.parentElement;
        document.getElementById("arstainfo11").deleteRow(row.rowIndex);
        resetForm();
    }
}
