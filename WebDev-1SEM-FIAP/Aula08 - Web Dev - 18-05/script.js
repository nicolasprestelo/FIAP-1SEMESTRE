// const alunos = ["Ana", "Carlos", "Mariana"];

// console.log(`tenho uma lista: ${alunos} e a primeira posição, usando [0], é :${alunos[0]}`);

// console.log(`A quantidade de itens na lista é ${alunos.length}`); // Comprimento da lista

// alunos.push("Pedro");   // Insere um novo item no final da lista
// console.log(`A lista atualizada com o .push() fica assim: ${alunos}`);

// alunos.unshift("Lucas");    //Insere um novo item no inicio da lista
// console.log(`A lista atualizada com o .unshift() fica assim: ${alunos}`);

// alunos.shift(); // Remove o primeiro item da lista
// console.log(`A lista atualizada com o .shift() fica assim: ${alunos}`); 

// alunos.pop(); // Remove o ultimo item da lista
// console.log(`A lista atualizada com o .pop() fica assim: ${alunos}`); 

// alunos.splice(1, 1); // Posição inicial e a quantidade de itens para ser deletado
// console.log(`A lista atualizada com o .splice(1, 1) fica assim: ${alunos}`);

// alunos.splice(1, 0, "Carlos");   // Inicio na posição 1, não removo nada e adiciono "Carlos"
// console.log(`A lista atualizada com o .splice(1, 0, 1) fica assim: ${alunos}`);

// const primeiros = alunos.slice(0, 2); 
// // Pega o valor do indice inicial e para no valor do indice final
// console.log(`%ctenho uma lista chamada alunos: ${alunos}`, 
//     "color: white; background:#007bff; padding: 8px; border-radius: 4px; font-size: 16px;");

// console.log(`Usando o .slice(0, 2) na lista alunos, tenho uma nova lista: ${primeiros}`);
    
// console.log(`Usando o .indexOf("Carlos") verifico em qual posição está esse item: ${alunos.indexOf("Carlos")}`);

// console.log(`Usando o .indexOf("Pedro") verifico em qual posição está esse item: ${alunos.indexOf("Pedro")}`);

// const posicao = alunos.indexOf("Pedro");

// if (posicao === -1) {
//     console.log("Aluno não encontrado!");
// } else {
//     console.log(`Aluno na posição: ${posicao}`);
// }

// --- CLASSE DECLARADA ANTES DO USO ---
class Aluno {
    constructor(nome, idade, curso) {
        this.nome = nome;
        this.idade = idade;
        this.curso = curso;
    }
};

const alunos = [
    new Aluno("Ana", 17, "Desv. Web"),
    new Aluno("Carlos", 18, "JavaScript"),
    new Aluno("Mariana", 19, "HTML e CSS"),
];

const inputNome = document.querySelector("#nome");
const inputIdade = document.querySelector("#idade");
const inputCurso = document.querySelector("#curso");
const inputBusca = document.querySelector("#busca");

const listaAlunos = document.querySelector("#listaAlunos");
const total = document.querySelector("#total");
const mensagem = document.querySelector("#mensagem");

const btnAdicionarFinal = document.querySelector("#btnAdicionarFinal");
const btnAdicionarInicio = document.querySelector("#btnAdicionarInicio");
const btnRemoverPrimeiro = document.querySelector("#btnRemoverPrimeiro");
const btnRemoverUltimo = document.querySelector("#btnRemoverUltimo");
const btnBuscar = document.querySelector("#btnBuscar");
const btnRemoverNome = document.querySelector("#btnRemoverNome");
const btnMostrarParte = document.querySelector("#btnMostrarParte");


