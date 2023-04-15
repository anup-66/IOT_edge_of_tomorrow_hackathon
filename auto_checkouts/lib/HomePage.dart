// ignore_for_file: file_names

import 'package:flutter/material.dart';
import 'ItemDetectionPage.dart';
import 'ItemDetail.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  // use this controller to get what the user typed
  final _textController = TextEditingController();

  List<ItemDetail> _listItemDetail = [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[50],
      appBar: AppBar(
        title: const Text("Auto CheckOuts"),
        centerTitle: true,
        backgroundColor: Colors.indigo[900],
        elevation: 10.0,
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            TextField(
              // enabled: false,
              controller: _textController,
              cursorColor: Colors.indigo[900],
              cursorWidth: 2.0,
              decoration: InputDecoration(
                // enabledBorder: OutlineInputBorder(
                //   borderSide: const BorderSide(width: 3.0, color: Colors.indigo),
                //   borderRadius: BorderRadius.circular(50.0),
                // ),
                hintText: "Item",
                focusedBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(11),
                    borderSide: const BorderSide(
                      color: Colors.indigo,
                      width: 2,
                    )),
                // enabledBorder: OutlineInputBorder(
                //   borderSide:
                //       const BorderSide(color: Colors.indigo, width: 2.0),
                //   borderRadius: BorderRadius.circular(15.0),
                // ),
                suffixIcon: IconButton(
                  onPressed: () {
                    // clearing what is there in the TextField
                    setState(() {
                      _textController.clear();
                    });
                  },
                  icon: const Icon(Icons.clear),
                  color: Colors.indigo[900],
                ),
              ),
            ),
            const SizedBox(
              height: 10.0,
            ),
            ElevatedButton(
              onPressed: () {
                // setState(() {
                //   print(_textController);
                // });
                String path = "assets/error.jpg";
                String txt = "Error! No item Found";
                String string = _textController.text.toLowerCase();
                // List<String> list = [];
                // String s = "";
                // for (int i = 0; i < string.length; i++) {
                //         if (string[i] != ',') {
                //                 s = s + string[i];
                //             } else {
                //                 list.add(s);
                //                 s = "";
                //             }
                //       }
                // list.add(s);
                if (string == "pepsi") {
                  path = "assets/pepsi.jpg";
                  txt = "PEPSI";
                } else if (string == "jimjam") {
                  path = "assets/jimjam.jpg";
                  txt = "JIM-JAM";
                } else if (string == "fashwash") {
                  path = "assets/fashwash.jpg";
                  txt = "FASHWASH";
                }
                Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) => ItemDetectionPage(
                              path: path,
                              txt: txt,
                            )));
              },
              style: const ButtonStyle(
                backgroundColor: MaterialStatePropertyAll(Colors.indigo),
              ),
              child: const Text(
                "submit",
                style: TextStyle(
                  color: Color.fromARGB(255, 196, 219, 238),
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
