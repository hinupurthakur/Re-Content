import 'package:flutter/material.dart';

class Help extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Material(
      color: Colors.lightBlueAccent,
      child:Center(
          child:Text("Welcome to Re-Content",
            textDirection: TextDirection.ltr,
            style: TextStyle(color: Colors.white,fontSize: 25.0),)
      ),
    );
  }

}