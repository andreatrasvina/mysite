let sliderInner = document.querySelector(".slider--inner");

let images = sliderInner.querySelectorAll("img");

let index = 1;

setInterval (function(){
    let porcentaje = index * -100
    sliderInner.style.transform = "translateX("+ porcentaje +"%)";
    if (index > images.length-2){
        index = 0;
    }
    index++;
}, 3000);