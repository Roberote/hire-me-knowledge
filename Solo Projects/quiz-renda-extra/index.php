<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz - Descubra sua Melhor Renda Extra</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
<body>
    <div class="quiz-container">
        <h1>Descubra a Melhor Renda Extra para Você!</h1>
        <form id="quiz-form">
            <div class="question active">
                <p>1. Quanto tempo por dia você tem disponível?</p>
                <label class="option"><input type="radio" name="tempo" value="1"> Menos de 1h</label>
                <label class="option"><input type="radio" name="tempo" value="2"> 1h a 3h</label>
                <label class="option"><input type="radio" name="tempo" value="3"> Mais de 3h</label>
            </div>
            
            <div class="question">
                <p>2. Você prefere renda extra online ou presencial?</p>
                <label class="option"><input type="radio" name="tipo" value="online"> Online</label>
                <label class="option"><input type="radio" name="tipo" value="presencial"> Presencial</label>
            </div>
            
            <div class="question">
                <p>3. Você tem experiência com vendas?</p>
                <label class="option"><input type="radio" name="vendas" value="sim"> Sim</label>
                <label class="option"><input type="radio" name="vendas" value="nao"> Não</label>
            </div>
            
            <div class="navigation">
                <button type="button" id="prev" class="hidden">Voltar</button>
                <button type="button" id="next">Próxima</button>
                <button type="submit" id="submit" class="hidden">Ver Resultado</button>
            </div>
        </form>
    </div>
    
    <script src="script.js"></script>
</body>
</html>
