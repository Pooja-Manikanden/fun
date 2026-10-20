const express=require("express");
const mongoose=require("mongoose");
const cors=require("cors");

const app=express();

app.use(cors());
app.use(express.json());

mongoose.connect("mongodb://127.0.0.1:27017/demoweb")
.then(() => console.log("MongoDb connected successfully"))
.catch((err) => console.log(err));

const Bookschema=new mongoose.Schema({
    bookname:String,
    quantity:Number
});

const Book=mongoose.model("Book",Bookschema);

app.get("/books", async(req ,res) =>{
    try{
        const books=await Book.find();
        res.json(books);
    }
    catch(error){
        console.log(error);
    }
});


app.post("/books", async (req, res) => {
    try {
        console.log("Received book:", req.body);

        const book = new Book({
            bookname: req.body.bookname,
            quantity: req.body.quantity
        });

        await book.save();

        res.json({ message: "Book added successfully", book: book });
    } catch (error) {
        console.log("POST Error:", error);
        res.status(500).json({ message: "Something went wrong" });
    }
});


app.delete("/books/:id", async(req,res) =>{
    try{
        const book=books.findByIdandDelete(req.params.id);
        books.splice(book ,1);
    }
    catch{
        res.Status(404).json({message: "No book found"});
    }
});

app.listen(3000,() =>
console.log("Server is listening at http://localhost:3000"));
