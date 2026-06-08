const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("NeuralEDA backend running!");
});

app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
