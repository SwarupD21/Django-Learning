var lock = true 
var txt = document.getElementsByTagName('h1') 
console.log(txt[0].innerHTML)
const element = document.getElementsByClassName('btn')[0]

element.addEventListener("click",change);

function change(){
    if(lock===true){
        txt[0].innerHTML='hey i am swarup'
        lock=false
    }
    else{
        txt[0].innerHTML='Hello World'
        lock=true
    }
}