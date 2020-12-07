var pageContent = document.getElementById("adminzinas").innerHTML; 
sessionStorage.setItem("page1content", pageContent);
document.getElementById("zinas").innerHTML=sessionStorage.getItem("page1content");
