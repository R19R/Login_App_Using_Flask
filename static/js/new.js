function getName(){
    const username = document.getElementById("name").value;
    localStorage.setItem("NAME", username)
    return  false;
}

function getDisplayName(){
    document.getElementById("displayName").innerHTML=localStorage.getItem("NAME");
}