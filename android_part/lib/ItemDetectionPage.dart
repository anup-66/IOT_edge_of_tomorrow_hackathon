// ignore_for_file: file_names, must_be_immutable

import 'package:flutter/material.dart';

class ItemDetectionPage extends StatefulWidget {
  String path;
  String txt;
  ItemDetectionPage({super.key, required this.path, required this.txt});

  @override
  State<ItemDetectionPage> createState() => _ItemDetectionPageState();
}

class _ItemDetectionPageState extends State<ItemDetectionPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[50],
      appBar: AppBar(
        title: const Text(
          "Item Detection",
          style: TextStyle(color: Colors.white),
        ),
        centerTitle: true,
        backgroundColor: Colors.indigo[900],
        elevation: 10.0,
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          const SizedBox(
            height: 10.0,
          ),

          Center(
              child: SizedBox(
            height: 300,
            width: 300,
            child: ClipRRect(
              borderRadius: BorderRadius.circular(10.0),
              child: Image.asset(widget.path),
              
            ),
          )),
          Divider(
            height: 60.0,
            color: Colors.grey[800],
          ),

          Center(
            child: Text(
              widget.txt,
              style: TextStyle(
                fontSize: 28.0,
                letterSpacing: 2.0,
                fontWeight: FontWeight.bold,
                color: Colors.indigo[900],
              ),
              ),
          ),

          const SizedBox(
            height: 20.0,
            ),

          Center(
            child: ElevatedButton(
              onPressed: null, 
              child: Text(
                "Check Out",
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 20.0
                  ),
                ),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.indigo[900],minimumSize: const Size(150.0, 50.0)),
              ),)
        ],
      ),
    );
  }
}
