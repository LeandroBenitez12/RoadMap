/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */

/*
En TS estan las mismas estructuras de datos que en JS 
Array: como en python son listas que pueden tener cualquier elemente y estan ordenadas
tupla: son arrays especiales , pero se les definde el tipo de datos y orden que poseera dentro los datos
objects: los maps no tienen un orden , son claves-valor 
maps: son objects la diferencia es que estas mantienen un orden al insertar

operaciones:
array y tuplas:
insercion:
.push() //se agrega al final
.unshift //al principio
.splice // posicion especifica (posicion, elementos a eliminar, cosa a insertar)

eliminar:
pop() //ultimo elemento del array 
shift() //al principio
splice(posicion, 1) //para elimianr el 1

actualizar :
asignando nuevo valor

orden:
sort() de forma ascendente

*/

let array = [1, 2, 3];
array.push(4); // [1, 2, 3, 4]

array.unshift(0); // [0,1, 2, 3, 4]

array[1] = 10; // [0, 10, 2, 3, 4]

array.splice(1, 1); // [0, 2, 3, 4]

// manipular arrays con otras funciones

let numbers = [0, 1, 2, 3, 4, 5];

numbers = numbers.map((n) => n - 1); // [-1,0,1,2,3,4]

let numberPair = numbers.filter((n) => n % 2 == 0); //[2,4]

//busqueda
let findZero = numbers.find((n) => n == 0); //0

//saber posicion
let positionOfNumberFour = numbers.indexOf(4); //5

// contrato
interface Person {
  nombre: string;
  edad?: number;
  ciudad?: string;
}
let persona: Person = { nombre: "Juan", edad: 30 };
persona.ciudad = "Lisboa";

delete persona.edad;

// actualizacion
persona.nombre = "PEDRO";

//busqueda
let namePerson = persona.nombre;

// Maps

let mapa = new Map();
mapa.set("nombre", "Juan");
mapa.set("edad", 30);

mapa.delete("edad");

mapa.set("edad", 30);
mapa.set("edad", 31);

let nameMap = mapa.get("nombre");

/*
DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */

function menu(): void {
  const options = ["Menu", "Search", "Insert", "Update", "Delete", "Exit"];

  
}

function bookContacts() {
  let exit = false;
  while (!exit) {}
}
