// Exercício: Soma dos Números Pares

// Escreva um programa que some todos os números pares de 1 a 50 e exiba o resultado no console.

// Requisitos:
// Use um loop for.
//Verifique se o número é par antes de somá-lo.
// Exiba o resultado final no console.

let total = 0

for(let index = 0; index <= 50; index++){
    if(index%2==0){
        total+=index
    }
}

console.log(total)
