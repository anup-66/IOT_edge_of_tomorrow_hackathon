// ignore_for_file: file_names

import 'package:flutter/material.dart';
import 'ItemDetail.dart';

class BillGeneration extends StatefulWidget {
  final double billList;
  const BillGeneration({super.key, required this.billList});

  @override
  State<BillGeneration> createState() => _BillGenerationState();
}

class _BillGenerationState extends State<BillGeneration> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[50],
      appBar: AppBar(
        backgroundColor: Colors.blue[900],
        title: const Text("Bill"),
        centerTitle: true,
        elevation: 10.0,
      ),

      body: Text("Total PRice ---> ${widget.billList}"),

      // body: SingleChildScrollView(
      //   child: Center(
      //     child: Column(
      //       children: widget.billList.map((ItemDetail e) {
      //         return Row(
      //           children: <Widget>[
      //             const SizedBox(height: 10.0,),
      //             Text(
      //               e.imageName.toUpperCase(),
      //               style: const TextStyle(fontWeight: FontWeight.bold,color: Colors.indigo,letterSpacing: 2.0),
      //             ),
        
      //             const SizedBox(height: 10.0,),
        
      //             Text(
      //               "${e.price}",
      //               style: const TextStyle(fontWeight: FontWeight.bold,color: Colors.indigo,letterSpacing: 2.0),
      //             ),
        
      //             const SizedBox(height: 10.0,),
      //           ],
      //         );
      //       }).toList(),
      //     ),
      //   ),
      // ),
    );
  }
}
