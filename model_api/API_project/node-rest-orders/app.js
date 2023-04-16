const express = require("express");
const app = express();
const morgan = require("morgan");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");

const productRoutes = require("./api/routes/products");
const orderRoutes = require("./api/routes/orders");

mongoose.connect(
  "mongodb+srv://Anup_66:Anup65@cluster0.xramm.mongodb.net/?retryWrites=true&w=majority",
  {
    useNewUrlParser: true, //it will use mongodb client
  }
);
app.use(morgan("dev"));
app.use(bodyParser.urlencoded({ extended: false })); //the type of body we want to parse is url encoded and true allows us to parse extended bodies with rich data but false will only support simple bodies for url encoded data
app.use(bodyParser.json()); //extracts json data and makes it readable for us
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "*");
  if (req.method === "OPTIONS") {
    res.header("Access-Control-Allow-Methods", "PUT, POST, PATCH, DELETE, GET");
    return res.status(200).json({});
  }
  next();
});
// Routes which should handle requests
app.use("/products", productRoutes);
app.use("/orders", orderRoutes);

app.use((req, res, next) => {
  const error = new Error("Not Found");
  error.status = 404;
  next(error); // forward the error request
});
app.use((error, req, res, next) => {
  //handles error detected in the previous step
  res.status(error.status || 500);
  res.json({
    error: {
      message: error.message,
    },
  });
});
//
module.exports = app;
