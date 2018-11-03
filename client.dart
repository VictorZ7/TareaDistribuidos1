import 'dart:async';
import 'dart:io';
import 'dart:convert';

String _host = InternetAddress.loopbackIPv4.host;
String path = 'Hola te llego el memo?';

Map jsonData = {
  'name': 'Han Solo',
  'job': 'reluctant hero',
  'BFF': 'Chewbacca',
  'ship': 'Millennium Falcon',
  'weakness': 'smuggling debts'
};

Future main() async {
  HttpClientRequest request = await HttpClient().post(_host, 10000,path) /*1*/
    ..headers.contentType = ContentType.json /*2*/
    ..write(jsonEncode(jsonData)); /*3*/
  print('hola mundo');
  HttpClientResponse response = await request.close(); /*4*/
  await response.transform(utf8.decoder /*5*/).forEach(print);
}
