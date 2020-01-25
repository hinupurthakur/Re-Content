import 'package:flutter/material.dart';

import 'app_screens/Home.dart';


void main() {
  runApp(new MyFlutterApp() );
}
class MyFlutterApp extends StatelessWidget
{
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return MaterialApp(
      title: "Re-Content",
      home: Scaffold(
        appBar: AppBar(title: Text("Home" ),),
        body: Home()
      ),
    );
  }

}