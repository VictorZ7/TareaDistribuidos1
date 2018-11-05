const grpc = require('grpc');

const proto = grpc.load('proto/trafico_aereo.proto');
const server = new grpc.Server();





//define the callable methods that correspond to the methods defined in the protofile
server.addProtoService(proto.trafico_aereo.EmployeeLeaveDaysService.service, {
  /**
  Check if an employee is eligible for leave.
  True If the requested leave days are greater than 0 and within the number
  of accrued days.
  */
  eligibleForLeave(call, callback) {
    if (call.request.requested_leave_days > 0) {
      if (call.request.accrued_leave_days > call.request.requested_leave_days) {
        callback(null, { eligible: true });
      } else {
        callback(null, { eligible: false });
      }
    } else {
      callback(new Error('Invalid requested days'));
    }
  },

  /**
  Grant an employee leave days
  */
  grantLeave(call, callback) {
    let granted_leave_days = call.request.requested_leave_days;
    let accrued_leave_days = call.request.accrued_leave_days - granted_leave_days;

    callback(null, {
      granted: true,
      granted_leave_days,
      accrued_leave_days
    });
  }
});

var pistas_a = new Array();
var pistas_d = new Array();
var busy_queue = new Array();
var ips_air = {};
var i=0;
var  name=0;

var readline = require('readline-sync');

var name = readline.question("Cantidad Pistas Aterrizaje?");

while (i<parseInt(name)){
  pistas_a.push(0);
  i++;

}
i=0
console.log(pistas_a);

var readline = require('readline-sync');

var name = readline.question("Cantidad Pistas Despegue?");

while (i<parseInt(name)){
  pistas_d.push(0);
  i++;

}
console.log(pistas_d);
name3=1;
while(1===parseInt(name3)){

  var readline = require('readline-sync');

  var name = readline.question("Destino?");
  var name2 = readline.question("IP Destino?");
  var name3 = readline.question("Desea agregar otro destino? SI=1/No=0");
  ips_air[name2]=name;

}

console.log(ips_air[name2]);



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
