# 📚 Documentação do Projeto Quiz Revalida

Bem-vindo à documentação do projeto Quiz Revalida! Aqui você encontrará tudo o que precisa para **gerenciar o quiz** e **integrá-lo ao seu site**. Vamos lá? 🚀

---

## 🛠️ Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- **`admin.html`** 🖥️  
  Painel de administração para adicionar/remover categorias e perguntas.

- **`index.html`** 📄  
  Página principal do quiz, onde os usuários respondem às perguntas.

- **`script.js`** 🧠  
  Contém a lógica do quiz, incluindo correção de respostas e análise de desempenho.

- **`styles.css`** 🎨  
  Estilos para o quiz e o painel de administração.

- **`server.js`** 🌐  
  Servidor Node.js para servir os arquivos estáticos.

---

## 📋 Guia para o Cliente

Aqui está um passo a passo para **gerenciar categorias e perguntas** no painel de administração.

### 1. **Adicionar Categorias** 📂

1. Acesse o painel de administração (`admin.html`).
2. No formulário **"Adicionar Categoria"**, digite o nome da categoria.
3. Clique em **"Adicionar"**.

   > 💡 **Dica:** Crie categorias como "Cardiologia", "Pediatria", etc., para organizar as perguntas.

---

### 2. **Adicionar Perguntas** ❓

1. No formulário **"Adicionar Pergunta"**, preencha os seguintes campos:
   - **Texto da pergunta**: Digite a pergunta.
   - **Categoria**: Selecione uma categoria existente.
   - **Opções de resposta**: Insira 4 opções de resposta.
   - **Resposta correta**: Digite a resposta correta (deve ser igual a uma das opções).
2. Clique em **"Adicionar Pergunta"**.

   > 💡 **Exemplo:**  
   > **Pergunta:** Qual é o tratamento inicial para angina instável?  
   > **Opções:** AAS 300mg, Heparina, Nitroglicerina, Todos acima  
   > **Resposta Correta:** Todos acima

---

### 3. **Excluir Categorias/Perguntas** 🗑️

1. Na lista de **Categorias Existentes** ou **Perguntas Existentes**, localize o item que deseja remover.
2. Clique no botão **🗑️ Excluir** ao lado do item.

   > ⚠️ **Atenção:** A exclusão é permanente e não pode ser desfeita.

---

## 🚀 Como Integrar o Quiz ao Seu Site

Se você deseja integrar o quiz ao seu site existente, siga estas etapas:

### 1. **Hospedagem dos Arquivos**
   - Coloque os arquivos do projeto (`index.html`, `styles.css`, `script.js`, etc.) em uma pasta no seu servidor.
   - Certifique-se de que o servidor está configurado para servir arquivos estáticos.

### 2. **Incluir o Quiz em uma Página Existente**
   - Se você já tem um site, pode incorporar o quiz em uma página HTML existente. Use um `<iframe>` para isso:
     ```html
     <iframe src="caminho/para/index.html" width="100%" height="600px"></iframe>
     ```
   - Substitua `caminho/para/index.html` pelo caminho correto para o arquivo `index.html` do quiz.

### 3. **Personalização**
   - Para personalizar o design do quiz, edite o arquivo `styles.css`.
   - Para alterar a lógica do quiz, edite o arquivo `script.js`.

### 4. **Testar e Publicar**
   - Teste o quiz no seu site para garantir que tudo está funcionando corretamente.
   - Publique as alterações no servidor.

---

## 📄 Exemplo de Perguntas de Exemplo

Aqui estão algumas perguntas de exemplo que você pode adicionar ao quiz:

### Categoria: **Cardiologia** ❤️
- **Pergunta:** Qual é o tratamento inicial para angina instável?  
  **Opções:** AAS 300mg, Heparina, Nitroglicerina, Todos acima  
  **Resposta Correta:** Todos acima

- **Pergunta:** Qual é a principal causa de insuficiência cardíaca?  
  **Opções:** Hipertensão, Diabetes, Infarto do miocárdio, Todas acima  
  **Resposta Correta:** Todas acima

### Categoria: **Pediatria** 👶
- **Pergunta:** Qual vacina previne a tuberculose?  
  **Opções:** BCG, Tríplice viral, Hepatite B, Poliomielite  
  **Resposta Correta:** BCG

- **Pergunta:** Qual é a dose inicial de paracetamol para crianças?  
  **Opções:** 10 mg/kg, 15 mg/kg, 20 mg/kg, 25 mg/kg  
  **Resposta Correta:** 15 mg/kg

### Categoria: **Clínica Geral** 🩺
- **Pergunta:** Qual é o sintoma mais comum da diabetes tipo 2?  
  **Opções:** Sede excessiva, Fadiga, Visão turva, Todos acima  
  **Resposta Correta:** Todos acima

---

## 🎉 Pronto!

Agora você está pronto para gerenciar o quiz e integrá-lo ao seu site. Se precisar de mais ajuda, é só pedir! 😊