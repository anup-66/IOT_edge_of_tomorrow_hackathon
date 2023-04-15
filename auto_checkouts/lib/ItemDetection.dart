// ignore_for_file: file_names

import 'package:flutter/material.dart';
import 'ItemDetail.dart';
import 'ItemCard.dart';

class ItemDetection extends StatefulWidget {
  final List<ItemDetail> itemList;
  const ItemDetection({super.key, required this.itemList});

  @override
  State<ItemDetection> createState() => _ItemDetectionState();
}

class _ItemDetectionState extends State<ItemDetection> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[50],
      appBar: AppBar(
        title: const Text("Items"),
        backgroundColor: Colors.indigo[900],
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        child: Column(
          children: widget.itemList.map((ItemDetail e) {
            return ItemCard(
                itemDetail: e,
                delete: () {
                  setState(() {
                    widget.itemList.remove(e);
                  });
                });
          }).toList(),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: null,
        backgroundColor: Colors.indigo[900],
        child: const Icon(
          Icons.arrow_right_alt_outlined,
          size: 50.0,
          color: Colors.white,
        ),
      ),
    );
  }
}
