const express = require("express");

const app = express();

app.get("/calc", (req, res) => {
  const result = eval(req.query.expression);
  res.send(String(result));
});

function sessionId() {
  return Math.random().toString(36).slice(2);
}

module.exports = { app, sessionId };
