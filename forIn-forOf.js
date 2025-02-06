const meuArray = [ 10,20,30,40,50 ]

for(let indice=0; indice < meuArray.length; indice++) {
    console.log("indice: " + indice)
    console.log("Elemento: " + meuArray[indice])
}

for (const indice in meuArray) {
    console.log("indice in: " + indice)
}

for (const elemento of meuArray) {
    console.log("Elemento of: " + elemento)  
}
