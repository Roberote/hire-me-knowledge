require('dotenv').config();
const express = require('express');
const cors = require('cors');

const app = express();

// Middlewares
app.use(cors());
app.use(express.json());

// Rotas básicas
app.get('/', (req, res) => {
    res.send('API de Usuários Rodando 🚀');
});

// Configuração do servidor
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));
const userRoutes = require('./routes/userRoutes');

app.use('/api', userRoutes);
