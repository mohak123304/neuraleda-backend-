const express = require("express");
const app = express();
const PORT = process.env.PORT || 8080;

app.get("/", (req, res) => {
  res.send("NeuralEDA backend running!");
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
