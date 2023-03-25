var selPlayer =parseInt(prompt("Escoge una opción: piedra, papel o tijeras."));

// var selPlayer = Math.floor(Math.random()*3)+1; //dara un numeroo al azar entre 1 y 3
var randomComp = Math.floor(Math.random() * 3)+1;

//piedra = p1 
//papel = p2 
//tijera = p3
var randomImage = "p" + selPlayer + ".png";

var randomImageSource1 = "images/" + randomImage; 
var randomImageSource2 = "images/p" + randomComp + ".png";

//se crean las variables que harán que se pongan las imagenes en dicho objeto
var image1 = document.querySelectorAll("img")[0];
var image2 = document.querySelectorAll("img")[1].setAttribute("src", randomImageSource2);

//se cambian los atributos establecidos con la nueva variable creada
image1.setAttribute("src", randomImageSource1);

// se cambia el texto para mostrar si hay ganador o empate
if (selPlayer === randomComp){
    document.querySelector("h1").innerHTML = "🤙🏼 Empate 🤙🏼";
} else if ((selPlayer === 1&& randomComp ===3)||(selPlayer === 3 && randomComp===2)||(selPlayer === 2 && randomComp===1)) {
    document.querySelector("h1").innerHTML = "☝🏼 Has ganado!!";
}else {
    document.querySelector("h1").innerHTML = "Perdiste... ✌🏼";
}

var selPlayer = document.querySelectorAll(".img1").length;

for(var i = 0; i < selPlayer; i++){
    document.querySelectorAll(".img1")[i].addEventListener("click", function(){
        var imgInnerHTML = this.innerHTML;
        console.log("hola");1
    })
}

function imgAnimation(click){
    var activeImg = document.querySelector("."+click);
    activeImg.classList.add("pressed");

    setTimeout(function(){
        activeImg.classList.remove("pressed");
    }, 100);
}