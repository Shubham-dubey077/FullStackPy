const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

app.post("/login", (req, res) => {
  const { username, password } = req.body;

  if (username === "admin" && password === "123") {
    return res.json({ message: "Login successful ✅" });
  } else {
    return res.status(401).json({ message: "Invalid username or password ❌" });
  }
});

app.get("/", (req, res) => {
  res.send("Backend is running ✅");
});


app.listen(5000, () => {
  console.log("Backend running on http://localhost:5000");
});
