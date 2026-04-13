
// function verificaPar() {
//     let numero = parseInt(prompt("Digite um número inteiro: "));

//     if (isNaN(numero)) {
//         alert("Por favor, digite um número válido: ");
//         return;
//     }
//     else if (numero % 2 == 0) {
//         alert(`O número ${numero} é par.`);
//     }
//     else{
//         alert(`O número ${numero} é ímpar.`);
//     }
// }
// verificaPar();  

// var resultado = 0;

// function somar (primeiroNumero, segundoNumero) {
//     resultado = primeiroNumero + segundoNumero;
// }

// function mostrar(mensagem) {
//     console.log(`A soma é o parâmetro ${mensagem}`);
// }
// somar(6, 3);
// mostrar(resultado);

// let n1 = parseInt(prompt("Digite o primeiro número: "))
// let n2 = parseInt(prompt("Digite o segundo número: "))
// let op = prompt("Digite qual operação deseja realizar: \n+\n-\n*\n/\n")

// function calculadora (primeiroNumero, segundoNumero, operacao) {
//     if (operacao == "+") {
//         return primeiroNumero + segundoNumero;
//     }
//     else if (operacao == "-") {
//         return primeiroNumero - segundoNumero;
//     }
//     else if (operacao == "*") {
//         return primeiroNumero * segundoNumero;
//     }
//     else if (operacao == "/") {
//         if (segundoNumero == 0) {
//             console.log("ERRO: Não é possível dividir por zero.")
//         }
//         else {
//             return primeiroNumero / segundoNumero;
//         }
//     }
//     else {
//         return 0;
//     }
// }
// alert(calculadora(n1, n2, op))

// let n1 = parseInt(prompt("Digite o primeiro número: "))
// let n2 = parseInt(prompt("Digite o segundo número: "))

// function verificaMaior (n1, n2) {
//     if (n1 > n2) {
//         return n1 - n2;
//     }
//     else{
//         return n2 - n1;
//     }
// }
// console.log(`A subtração do maior pelo menor é ${verificaMaior(n1, n2)}`)

let n1 = parseInt(prompt("Digite o primeiro número: "))
let n2 = parseInt(prompt("Digite o segundo número: "))
let op = prompt("Digite qual operação deseja realizar: \n+\n-\n*\n/\n")

let somar = (n1, n2) => n1 + n2;
let subtrair = (n1, n2) => n1 - n2;
let multiplicar = (n1, n2) => n1 * n2;
let dividir = (n1, n2) => n1 / n2;

let resultado;

if (op == "+") {
   resultado = somar(n1, n2);
}
else if (op == "-") {
   resultado = subtrair(n1, n2);
}
else if (op == "*") {
   resultado = multiplicar(n1, n2);
}
else if (op == "/") {
   resultado = dividir(n1, n2);
} else {
   alert("Operação inválida!");
}

alert(`O resultado é ${resultado}`);