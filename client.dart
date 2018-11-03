import 'dart:async';
import 'dart:io';
import 'dart:convert';

String _host = InternetAddress.loopbackIPv4.host;
String path = 'file.txt';

Map jsonData = {
  'name': 'Han Solo',
  'job': 'reluctant hero',
  'BFF': 'Chewbacca',
  'ship': 'Millennium Falcon',
  'weakness': 'smuggling debts'
};

Future main() async {
  HttpClientRequest request = await HttpClient().post(_host, 4049, path) /*1*/
    ..headers.contentType = ContentType.json /*2*/
    ..write(jsonEncode(jsonData)); /*3*/
  HttpClientResponse response = await request.close(); /*4*/
  await response.transform(utf8.decoder /*5*/).forEach(print);
}
