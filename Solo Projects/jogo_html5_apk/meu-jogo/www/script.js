document.addEventListener('deviceready', function() {
    const switchKey = document.getElementById('switch-key');
    const gameContainer = document.getElementById('game-container');
    let inAppBrowserRef = null;
    let isLandingPageOpen = false;

    switchKey.addEventListener('click', function() {
        if (gameContainer.style.display !== 'none') {
            // Esconde o jogo e abre a WebView imersiva
            gameContainer.style.display = 'none';
            inAppBrowserRef = cordova.InAppBrowser.open(
                'landing-page.html', // URL da landing page
                '_blank',           // Abre em uma nova janela
                'location=no,toolbar=no,fullscreen=yes' // Configurações da WebView
            );
            isLandingPageOpen = true;
        } else {
            // Mostra o jogo novamente
            gameContainer.style.display = 'block';
            if (inAppBrowserRef) {
                inAppBrowserRef.close(); // Fecha a WebView
            }
            isLandingPageOpen = false;
        }
    });

    // Bloqueia o botão "Voltar" apenas quando a landing page estiver aberta
    document.addEventListener('backbutton', function(e) {
        if (isLandingPageOpen) {
            e.preventDefault(); // Impede o comportamento padrão do botão "Voltar"
        }
    }, false);
}, false);