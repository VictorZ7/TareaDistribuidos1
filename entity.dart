// At package:client_server/entity.dart

/// Interface Foo implements Timestamps, and having one concrete implementation.
abstract class Foo implements Timestamps {
  /// Datastore id (Type: String).
  String get id;
  bool get isSomething;
  List<String> get aList;
  // A domain specific name alias to id.
  String get text => id;
  
  // some validation method here sounds nice.
}

/// Timestamps interface.
/// CreatedTime and UpdatedTime interfaces are separated. Because there can be an entity which don't need updatedTime interface.
abstract class Timestamps = CreatedTime with UpdatedTime;

/// For an Entity which don't need updatedTime interface.  
abstract class CreatedTime {
  DateTime get createdTime;
}

abstract class UpdatedTime {
  DateTime get updatedTime;
}