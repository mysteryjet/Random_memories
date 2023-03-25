var randomNumber1 = Math.floor(Math.random()*6)+1; // dara un numero al azar de 1 al 6 para primer dado
var randomNumber2 = Math.floor(Math.random()*6)+1; // dara un numero al azar de 1 al 6 para segundo dado

var randomDiceImage = "dice" + randomNumber1+".png"; // dara como resultado un nombre de: dice1.png al dice6.png

var randomImageSource1 = "images/" + randomDiceImage; // da como resultado nombre: images/dice5.png
var randomImageSource2 = "images/dice" + randomNumber2 + ".png";

// se crean las variables que harán que se pongan las imagenes en dicho objeto
var image1 = document.querySelectorAll("img")[0];
var image2 = document.querySelectorAll("img")[1].setAttribute("src", randomImageSource2);

// se cambian los atributos estableciendolos con la nueva variable creada
image1.setAttribute("src", randomImageSource1);

if (randomNumber1 > randomNumber2){
    document.querySelector("h1").innerHTML = "☝🏼 Player 1 Wins";
} else if (randomNumber1 < randomNumber2){
    document.querySelector("h1").innerHTML = "Player 2 Wins ✌🏼";
} else {
    document.querySelector("h1").innerHTML= "🤙🏼 Draw 🤙🏼";
}