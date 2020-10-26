// NPM modules required

const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.set("view engine", "ejs");
app.use(express.static("public"));

// Connection to mongoDB database via mongoose

mongoose.connect("mongodb://0.0.0.0:27017/todolistDB", { // 172.17.0.1 host.docker.internal
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const itemsSchema = {
  name: String,
};

const Item = mongoose.model("Item", itemsSchema);

const item1 = new Item({
  name: "Welcome to your todolist",
});

const item2 = new Item({
  name: "Hit the + button to add the new item",
});

const item3 = new Item({
  name: "<-- Hit this to delete an item",
});

const defaultItems = [item1, item2, item3];

app.get("/", (req, res) => {
  Item.find({}, (err, foundItems) => {
    if (foundItems.length === 0) {
      Item.insertMany(defaultItems, (err) => {
        if (err) {
          console.log(err);
        } else {
          console.log("Successfully saved default items to database");
        }
      });
      res.redirect("/");
    } else {
      res.render("list", { listTitle: "Today", newListItems: foundItems });
    }
  });
});

app.post("/", (req, res) => {
  const itemName = req.body.newItem;

  const item = new Item({
    name: itemName,
  });

  item.save();
  res.redirect("/");
});

app.post("/delete", (req, res) => {
  const checkedItemId = req.body.checkbox;
  Item.findByIdAndRemove(checkedItemId, (err) => {
    if (err) {
      console.log(err);
    } else {
      console.log("Item deleted succesfully");
    }
  });
  res.redirect("/");
});

app.get("/work", (req, res) => {
  res.render("list", { listTitle: "Work List", newListItems: workItems });
});

app.post("/work", (req, res) => {
  let item = req.body.newItem;
  workItems.push(item);
  res.redirect("/work");
});

// Connection on Port 3000

app.listen(3000,'0.0.0.0', () => { //127.0.0.1
  console.log("Server has Started");
});
