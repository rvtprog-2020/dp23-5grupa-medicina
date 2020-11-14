let Username = document.getElementById("loginVards");
let Password = document.getElementById("loginParole");
let loginSubmit = document.getElementById("loginSubmit");
let regUsername = document.getElementById("regVards");
let regPassword = document.getElementById("regPassword");
let Register = document.getElementById("register");
var Usernames = [];
var Passwords = [];
Register.addEventListener("click", function(){
    if (regUsername.value === ""){
        alert("Lūdzu ievadiet lietotājvārdu")
        if (regPassword.value === ""){
            alert("Lūdzu ievadiet paroli")
            return
        }
    }if (regPassword.value === ""){
     alert("Lūdzu ievadiet paroli")
     return
    }else{
        Usernames.push(regUsername)
        Passwords.push(regPassword)
        return
    }
});
loginSubmit.addEventListener("click", function(){
    if (Username.value === ""){
        alert("Lūdzu ievadiet lietotājvārdu")
        if (Password.value === ""){
            alert("Lūdzu ievadiet paroli")
            return
        }
    }if (Password.value === ""){
     alert("Lūdzu ievadiet paroli")
     return
    }else{
        //STARP ŠĪM LĪNIJĀM NOTIEK VISS ACTUAL KODS

        //STARP ŠĪM LĪNIJĀM NOTIEK VISS ACTUAL KODS
    }
})