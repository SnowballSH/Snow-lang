/// DART output.dart

import 'dart:io';
import 'package:path/path.dart' as p;

void main(file) {
  String pt = p.absolute("..", "compiler/compiler.py");
  Process.run("python", [pt, file]);
  print("file ran successfully");
}
