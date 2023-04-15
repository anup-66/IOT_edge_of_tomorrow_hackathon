// ignore_for_file: prefer_const_constructors_in_immutables, file_names

import 'package:flutter/material.dart';
import 'ItemDetail.dart';

class ItemCard extends StatelessWidget {
  final ItemDetail itemDetail;
  final Function delete;
  ItemCard({super.key, required this.itemDetail, required this.delete});

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.fromLTRB(20.0, 20.0, 20.0, 0.0),
      child: Padding(
        padding: const EdgeInsets.all(12.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            Text(
              itemDetail.imageName.toUpperCase(),
              style: TextStyle(
                fontSize: 18.0,
                color: Colors.indigo[900],
              ),
            ),
            const SizedBox(
              height: 6.0,
            ),
            Text(
              "${itemDetail.price}",
              style: const TextStyle(
                fontSize: 15.0,
                fontWeight: FontWeight.bold,
              ),
            ),

            Container(
              height: 50.0,
              width: 50.0,
              decoration: BoxDecoration(
                image: DecorationImage(
                  image: NetworkImage(itemDetail.imagePath),
                  ),
              ),
            ),

            TextButton.icon(
              onPressed: () {
                delete();
              },
              label: const Text("remove"),
              icon: const Icon(Icons.delete),
            ),
          ],
        ),
      ),
    );
  }
}
