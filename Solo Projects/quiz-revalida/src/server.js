const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

// Servir arquivos estáticos (HTML, CSS, JS)
app.use(express.static(path.join(__dirname, '../public')));

// Rota para o quiz
app.get('/quiz', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

// Rota para servir as perguntas
const questions = require('./data/questions.json');
app.get('/api/questions', (req, res) => {
  res.json(questions);
});

// Iniciar o servidor
app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});