//btn-outline-success
//btn-outline-secondary
console.log("ff")

let movieOne_button = document.getElementById("m1");
let fieldMovieOne = document.getElementById("fm1")
movieOne_button.addEventListener('click',() => {myfunction(movieOne_button,fieldMovieOne)})


let movieTwo_button = document.getElementById("m2");
let fieldMovieTwo = document.getElementById("fm2")
movieTwo_button.addEventListener('click',() => {myfunction(movieTwo_button,fieldMovieTwo)})


let timeOne_button = document.getElementById("t1");
let fieldTimeOne = document.getElementById("ft1")
timeOne_button.addEventListener('click',() => {myfunction(timeOne_button,fieldTimeOne)})


let timeTwo_button = document.getElementById("t2");
let fieldTimeTwo = document.getElementById("ft2")
timeTwo_button.addEventListener('click',() => {myfunction(timeTwo_button,fieldTimeTwo)})



function myfunction(m,f){
    m.classList.remove('btn-outline-secondary')
    m.classList.add('btn-outline-success')
    f.setAttribute('value','clicked')
}









