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
var myVariable = 10;
var pi = 3.14;
// data types
var myNumber = 30.029;
var myString = "hello world";
var isRight = false;
// arrays
var numberslist = [1, 2, 3, 4, 5];
var arrayList = ["2", "2"];
// enum
var State;
(function (State) {
    State[State["On"] = 0] = "On";
    State[State["Off"] = 1] = "Off";
    State[State["Suspend"] = 2] = "Suspend";
})(State || (State = {}));
var myState = State.On;
// ANY PARA INDICAR QUE PUEDE SER CUALQUIERA , PERO LA DIFERENCIA CON OTROS ES QUE ANULA LO QUE ES TODO TYPESCRIPT
var miDato = 17;
miDato = "hola"; // no salta error xD
function printInDisplay() {
    // medio que no nos interesa lo que retorna asi que es void porque no retornamos nada
    console.log("Hola");
    // return "OK";
}
var myNoSe;
function error() {
    // nunca llegaria a ejecutarse un return implicito tecnicamente
    if (true) {
        throw new Error("Error");
    }
}
var myLanguage = "TypeScript";
console.log("\u00A1Hola, ".concat(myLanguage));
