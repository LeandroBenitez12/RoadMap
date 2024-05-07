/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
// ya se sobre suma, resta, multiplicacion y ,division agrego:
let modulo: number = 10 % 3; // Resultado: 1 (ya que 10 dividido por 3 es 3 con un residuo de 1)
modulo++; //incremento
modulo--; //decremento
modulo += 3; // asignacion de operacion aritmetica

// AND
let result = true && true;

result = result || false;

!result; // negar

// comparacion == y != y para hacer una comparacion estricta === es decir
let isEqual: boolean = true === result;

// Operadorde pertenen
let list = [0, 1, 2, 3, 4, 5];
let isInList: boolean = 3 in list;

let objeto = { a: 1, b: 2, c: 3 };
let resultado: boolean = !("d" in objeto);

let i: number = 0;

//garantiza que el bloque de código se ejecute al menos una vez.
do {
  console.log(i);
  i++;
} while (i < 5);

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

console.log("089098");
for (let j = 10; j <= 55; j++) {
  if (j % 2 == 0 && j !== 16 && j % 3 != 0) console.log(j);
}

// for of para recorrer lista y for in para objetos
