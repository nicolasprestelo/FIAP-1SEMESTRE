// for (let i = 1; i <= 10; i ++) {
//     console.log(i);
// }


/*
let numero = parseInt(prompt("Insira número: "));

for (let i = 1; i <= 10; i++) {
    let tabuada = numero * i;
    console.log(`${numero} x ${i} = ${tabuada}`)
}
*/


// Ex01
/*
let numero = parseInt(prompt("Insira um número de 1 a 10: "))

for (let i = numero; i > 0; i --) {
    console.log(i)
}


let repetir = true;

while (repetir) {
    console.log("Ao infinito e ... Além!")
}
*/

/*
let entrada = prompt("Inserir um dado");


while (entrada != "sair") {
    alert("O usuário inseriu " + entrada);

    entrada = prompt("Inserir outro dado");
}
*/

// Ex02

// let numero = parseInt(prompt("Insira um número: "))
// let resultado = 1;
// let i = numero;

// while (i > 1) {
//     resultado *= i
//     i --
// }
// console.log(`O fatorial de ${numero} é ${resultado}`)




//Ex03

let numero = parseInt(prompt("Insira um número de 1 a 100: "))

switch (true) {
    case (numero >= 1 && numero < 10):
        alert("O resultado será 'fámilia do 1'");
        break;
    case (numero >= 10 && numero < 20):
        alert("O resultado será 'fámilia do 10'");
        break;
    case (numero >= 20 && numero < 30):
        alert("O resultado será 'fámilia do 20'");
        break;
    case (numero >= 30 && numero < 40):
        alert("O resultado será 'fámilia do 30'");
        break;
    case (numero >= 40 && numero < 50):
        alert("O resultado será 'fámilia do 40'");
        break;
    case (numero >= 50 && numero < 60):
        alert("O resultado será 'fámilia do 50'");
        break;
    case (numero >= 60 && numero < 70):
        alert("O resultado será 'fámilia do 60'");
        break;
    case (numero >= 70 && numero < 80):
        alert("O resultado será 'fámilia do 70'");
        break;
    case (numero >= 80 && numero < 90):
        alert("O resultado será 'fámilia do 80'");
        break;
    case (numero >= 90 && numero <= 99):
        alert("O resultado será 'fámilia do 90'");   
        break;  
}