<?php
// Pegando respostas do quiz
$tempo = $_GET['tempo'] ?? '';
$tipo = $_GET['tipo'] ?? '';

// Lógica para definir a oferta
if ($tempo == "1" && $tipo == "online") {
    $mensagem = "Você tem pouco tempo, então indicamos algo prático, como afiliado digital!";
} elseif ($tempo == "2" && $tipo == "online") {
    $mensagem = "Você pode se dedicar algumas horas! Que tal abrir sua loja online?";
} elseif ($tempo == "3" && $tipo == "online") {
    $mensagem = "Você tem tempo e quer algo sólido! Criar um curso pode ser ideal!";
} elseif ($tempo == "1" && $tipo == "presencial") {
    $mensagem = "Com pouco tempo, faça renda extra como motorista de app!";
} else {
    $mensagem = "Descubra a melhor opção para você no nosso curso!";
}

// URL do checkout (substitua pelo seu link real)
$checkout_url = "https://seulinkdecheckout.com";

?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seu Resultado</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="quiz-container">
        <h1>Seu Resultado:</h1>
        <p><?php echo $mensagem; ?></p>
        <a href="<?php echo $checkout_url; ?>" class="botao-comprar">Quero Aprender Agora!</a>
    </div>
</body>
</html>
