/// Client side.

import 'package:client_server/entity.dart' as entity;

class Foo extends entity.Foo {
  @override
  final String id;
  @override
  bool isSomething;
  @override
  List<String> aList;
  @override
  final DateTime createdTime;
  @override
  final DateTime updatedTime;
  
  Foo(this.id, this.isSomething, this.aList, this.createdTime,
      this.updatedTime);
  
  // Some other client side specific constructors below...
    
  // Some client side specific methods below...  
}