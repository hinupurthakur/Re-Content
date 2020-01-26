import 'package:flutter/material.dart';

import 'boomMenu.dart';
import 'boom_Menu.dart';

class Home extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Center
      (

        child: Container(

        alignment: Alignment.topCenter ,
            margin:EdgeInsets.only(left: 35.0),


          width: 400,
          height: 150,

            //color:Colors.lightBlue,

          child:Column(

            children: <Widget>[
              FlightImageAsset(),
              Row
                (
                children: <Widget>[
                  Expanded(

                      child:Text("WELCOME TO RE-CONTENT",textDirection: TextDirection.ltr,

                    style: TextStyle(color: Colors.blueGrey ,fontSize: 25.0),

                  )),

                ],
              ),
              BoomMenu()

            ]
          )

        )


        );







  }

}
class FlightImageAsset extends StatelessWidget
{
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    AssetImage assetImage=AssetImage('../images/logo.png');
    Image image=Image(image: assetImage,width: 100,height: 100,alignment: Alignment.center);
    //child:Image
     // (
      width:700;
      height: 700;
    //);

    return Container(child: image,);
  }

}
class HomeScreen extends StatelessWidget
{
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      appBar: AppBar(

      ),
      drawer: Drawer(
        child: ListView(
          children: <Widget>[
            DrawerHeader(child:Text("MENU")),
            ListTile(
              title: Text(""),
            ),
            ListTile
              (title:Text(""),),
            ListTile
              (title:Text(""),),

          ],
        ),
      ),
    );
  }

}