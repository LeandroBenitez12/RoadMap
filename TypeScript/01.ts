/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

// https://www.typescriptlang.org
/*
several 
lines */

let myVariable = 10;
const pi = 3.14;

// data types

let myNumber: number = 30.029;
let myString: string = "hello world";
let isRight: boolean = false;
// arrays
let numberslist: number[] = [1, 2, 3, 4, 5];
let arrayList: Array<string> = ["2", "2"];

// enum

enum State {
  On,
  Off,
  Suspend,
}

let myState: State = State.On;

// ANY PARA INDICAR QUE PUEDE SER CUALQUIERA , PERO LA DIFERENCIA CON OTROS ES QUE ANULA LO QUE ES TODO TYPESCRIPT
let miDato: any = 17;
miDato = "hola"; // no salta error xD

function printInDisplay(): void {
  // medio que no nos interesa lo que retorna asi que es void porque no retornamos nada
  console.log("Hola");
  // return "OK";
}

let myNoSe: undefined;

function error(): never {
  // nunca llegaria a ejecutarse un return implicito tecnicamente
  if (true) {
    throw new Error("Error");
  }
}

let myLanguage = "TypeScript";
console.log(`¡Hola, ${myLanguage}!`);
