const grpc = require('grpc'); // Importar grpc
const proto = grpc.load('proto/trafico_aereo.proto'); // Cargar archivo proto
const server = new grpc.Server(); // Crear Servidor grpc

var asignaciones_a ={};
var asignaciones_d= {};
var id_fly;
var pistas_a = new Array(); // Pistas de Aterrizaje
var pistas_d = new Array(); // Pistas de Despegue
var queue_A = new Array(); // Prima de Aviones aterrizaje
var queue_D = new Array(); //Cola de Despegues
var ips_air = {}; // IPs de aviones
var i=0;
var name=0;

var readline = require('readline-sync'); // readline-sync se utiliza para pedir datos desde la consola, similar a un raw-input
var ips = readline.question("IP de la torre?");


var readline = require('readline-sync'); // readline-sync se utiliza para pedir datos desde la consola, similar a un raw-input
var name = readline.question("Cantidad Pistas Aterrizaje?");

while (i<parseInt(name)){ // se agregan pistas de aterrizaje al arreglo
  pistas_a.push(0);
  i++;
}
i=0

console.log(pistas_a);

var readline = require('readline-sync'); // readline-sync se utiliza para pedir datos desde la consola, similar a un raw-input
var name = readline.question("Cantidad Pistas Despegue?");

while (i<parseInt(name)){ // se agregan pistas de despegue al arreglo
  pistas_d.push(0);
  i++;
}

console.log(pistas_d);

name3=1;

while(1===parseInt(name3)){

  var readline = require('readline-sync'); // readline-sync se utiliza para pedir datos desde la consola, similar a un raw-input

  var name = readline.question("Destino?");
  var ip_server = readline.question("IP Destino?");
  var name3 = readline.question("Desea agregar otro destino? SI=1/No=0");
  ips_air[ip_server]=name;

}

const keys= Object.keys(ips_air);

ip_server=keys[0];
//define the callable methods that correspond to the methods defined in the protofile
server.addProtoService(proto.trafico_aereo.ServicioAereo.service, {

  IP(call, callback) {
        ip_cliente = call.request.ip_cliente;
        ip_server;
        callback(null, { ip_server});
    id_fly=ip_cliente;
    console.log(ip_cliente);

  },



  /**
  Grant an employee leave days
  */
  Aterrizaje(call, callback) {
        var i= 0;
        let pos=-1;
        while (i<pistas_a.length){
          if (pistas_a[i] == 0){
            pistas_a.splice(i,1,1);
            pos = parseInt(i);
            console.log(pistas_a);
            asignaciones_a[id_fly]=pos;
            break;
          }
          i++;

        }
        if(pos=== -1){
          if(!queue_A.includes(id_fly)){
          queue_A.push(id_fly);
        }
        }

        console.log(asignaciones_a);

        callback(null, {pos});
        console.log(pos);
        },

  Despegue(call, callback) {
        var i= 0;
        let pos_d=-1;
        ip_cliente = call.request.ip_cliente;
        while (i<pistas_d.length){
          if (pistas_d[i] == 0){
            pistas_d.splice(i,1,1);
            pos_d = parseInt(i);
            console.log(pistas_d);
            asignaciones_d[ip_cliente]=pos_d;
            pistas_a.splice(asignaciones_a[ip_cliente],1,0);
            break;
          }
          i++;

        }

        if (pos_d===-1){
          if(!queue_D.includes(ip_cliente)){
          queue_D.push(ip_cliente);
        }
        }

        callback(null, {pos_d});
        console.log(pos_d);
      },

    Dejar_air(call, callback) {
          estado = call.request;
          if ((estado.psj>=300 || estado.psj<=524) && (estado.fuel<245 || estado.fuel>190)){
            console.log("Avion saliendo de la pista de aterrizaje");
            console.log(estado.ip_a);
            pistas_d.splice(asignaciones_d[estado.ip_a],1,0);

          }
          else{
            console.log("Debe cargar combustible o esperar más pasajeros");
            while(estado.psj<300){
              estado.psj++;
              console.log("Subiendo pasajeros...");
            }
            while(estado.fuel<245){
              estado.fuel++;
              console.log("Cargando combustible...");
            }

          }
          estado=call.request;
          callback(null,50502);

          console.log(pistas_d);
        },

});




//Specify the IP and and port to start the grpc Server, no SSL in test environment

server.bind('0.0.0.0:'+ips, grpc.ServerCredentials.createInsecure());

//Start the server
server.start();
console.log('grpc server running on port:', '0.0.0.0:'+ips);
