// Tipos primitivos 
// boolean 
var boolean = false;
console.log("Texto " + boolean + " texto");
// template string
console.log(`A variável ${boolean} tem o tipo ${typeof(boolean)} `);

var numero = 1;
console.log(`A variável ${numero} tem o tipo ${typeof(numero)} `);
//ctrl D = seleciona o proximo item com o mesmo valor e duplica o cursor

    // var; //variável global ou local - valor inicial pode ser nulo
    // let; //variável local de bloco - valor inicial pode ser nulo
    // const; // variável local de bloco - valor inicial é obrigatório

    // var prof = "Lucas";
    // var prof = "Lucas Sousa";

    // let sobrenome = "Sousa";

    // sobrenome = "Borges de Sousa";

    // const profissao = "Professor";

    // profissao = "Programador";

    // const profissao = "Testador";


// usando variável global
var nome = "Nicolas";

//usando variável local
function nomeDaFuncao() {
    var sobrenome = "Prestelo";
    console.log(sobrenome);
}

console.log(nome);
nomeDaFuncao();

// operadores de comparação
var comparacao = "0" == 0;
console.log(comparacao);

var comparacaoIdentica = "0" === 0;
console.log(comparacaoIdentica);

// operadores aritméticos 
// +, -, *, /, %, **
var mult = 5 * 9;
console.log(mult);

var divisao = 15 / 3 ;
console.log(divisao);

// operadores relacionais
// >, <, >=, <=, !=
// maior ou igual
var maiorOuIgual = 5 >= 16;
console.log(maiorOuIgual);

var diferente = 5 != 8;
console.log(diferente);

// operadores logicos 
// && - E, || - OU, ! - Não
var e = true && true && true;
console.log(e);

var ou = true || false;
console.log(ou);

var nao = !true;
console.log(nao);