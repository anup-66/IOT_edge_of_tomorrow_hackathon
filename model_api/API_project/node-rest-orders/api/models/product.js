// this file will tell how our product should look like in our application
const mongoose = require("mongoose");
const productSchema = mongoose.Schema({
  _id: mongoose.Schema.Types.ObjectId, //type of data, types, serial id used by mongoose internally
  name: String,
  price: Number,
});

module.exports = mongoose.model("Product", productSchema); //model takes two parameters: 1. name of model 2. schema we want to use
