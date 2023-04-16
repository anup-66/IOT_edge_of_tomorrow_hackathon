// ignore_for_file: file_names

import 'package:flutter/material.dart';
import 'ItemDetail.dart';
import 'ItemCard.dart';
import 'BillGeneration.dart';

class ItemDetection extends StatefulWidget {
  final List<ItemDetail> itemList;
  const ItemDetection({super.key, required this.itemList});

  @override
  State<ItemDetection> createState() => _ItemDetectionState();
}

class _ItemDetectionState extends State<ItemDetection> {
  double billList(List<ItemDetail> L) {
    // Map<String, double> map = {};
    // List<ItemDetail> arr = [];
    // map[L[0].productID] = L[0].price;
    // arr.add(L[0]);
    // for (int i = 1; i < L.length; i++) {
    //   for (int j = 0; j < arr.length; j++) {
    //     if (arr[j].productID == L[i].productID) {
    //       arr[j].price = arr[j].price + widget.itemList[i].price;
    //       break;
    //     }
    //   }
    //   for (int i = 1; i < L.length; i++) {
    //     if (map.keys.contains(L[i].productID)) {
    //       map[L[i].productID] = map[L[i].productID] + L[i].price;
    //     }
    //   }
    //   arr.add(widget.itemList[i]);
    // }

    double total = 0.0;
    for (int i = 0; i < L.length; i++) {
      total += L[i].price;
    }
    return total;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[50],
      appBar: AppBar(
        title: const Text("Items"),
        backgroundColor: Colors.indigo[900],
        centerTitle: true,
        elevation: 10.0,
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
        onPressed: () {
          Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) =>
                      BillGeneration(billList: billList(widget.itemList))));
        },
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
