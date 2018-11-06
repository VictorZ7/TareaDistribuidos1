const grpc = require('grpc'); // Importar grpc
const proto = grpc.load('proto/trafico_aereo.proto'); // Cargar archivo proto 
const server = new grpc.Server(); // Crear Servidor grpc

var pistas_a = new Array(); // Pistas de Aterrizaje
var pistas_d = new Array(); // Pistas de Despegue
var busy_queue = new Array(); // Cola de Aviones
var ips_air = {}; // IPs de aviones
var i=0;
var name=0;

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
  /**
  Check if an employee is eligible for leave.
  True If the requested leave days are greater than 0 and within the number
  of accrued days.
  */
  Despegue(call, callback) {
        ip_cliente = call.request.ip_cliente;
        ip_server;
        callback(null, { ip_server});
      
    console.log(ip_cliente);
    
  },

  /**
  Grant an employee leave days
  */
  Aterrizaje(call, callback) {
        var i= 0;
        let pos;
        while (i<pistas_a.length){
          if (pistas_a[i] == 0){
            pistas_a.splice(i,1,1);  
            pos = parseInt(i);
            console.log(pistas_a);
            break;
          }
          i++;

        }
        callback(null, {pos});
        console.log(pos);
        }
});

/**var prop = rl.createInterface(process.stdin, process.stdout);

prop.question('Cuantas Pistas son?', function(answer){

  process.exit();
  rl.close();
});
console.log(pistas);**/


//Specify the IP and and port to start the grpc Server, no SSL in test environment
server.bind('0.0.0.0:50050', grpc.ServerCredentials.createInsecure());

//Start the server
server.start();
console.log('grpc server running on port:', '0.0.0.0:50050');
