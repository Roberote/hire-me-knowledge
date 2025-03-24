let currentQuestionIndex = 0;
let score = 0;
let questions = JSON.parse(localStorage.getItem('questions')) || [];
let performanceData = {};

// Inicializar Dados de Desempenho
function initializePerformanceData() {
  const categories = JSON.parse(localStorage.getItem('categories')) || [];
  categories.forEach(category => {
    performanceData[category] = { total: 0, correct: 0 };
  });
}

// Funções do Quiz
function initializeQuiz() {
  initializePerformanceData();
  showScreen('quiz-screen');
  loadQuestion();
}

function showScreen(screenId) {
  document.querySelectorAll('.screen').forEach(screen => screen.classList.remove('active'));
  document.getElementById(screenId).classList.add('active');
}

function loadQuestion() {
  const question = questions[currentQuestionIndex];
  const questionContainer = document.getElementById('question-container');
  
  questionContainer.innerHTML = `
    <div class="question">
      <h3>${question.question}</h3>
      ${question.options.map(option => `
        <button class="option-btn" onclick="selectAnswer('${option}', '${question.category}')">${option}</button>
      `).join('')}
    </div>
  `;

  updateProgress();
}

function updateProgress() {
  const progress = (currentQuestionIndex / questions.length) * 100;
  document.getElementById('progress').style.width = `${progress}%`;
  document.getElementById('question-count').textContent = `Questão ${currentQuestionIndex + 1} de ${questions.length}`;
}

// Função de Resposta
function selectAnswer(selectedAnswer, category) {
  const question = questions[currentQuestionIndex];
  const options = document.querySelectorAll('.option-btn');

  // Verifica se a resposta está correta
  const isCorrect = selectedAnswer === question.answer;
  if (isCorrect) {
    score++;
    performanceData[category].correct++;
  }
  performanceData[category].total++;

  // Feedback visual
  options.forEach(option => {
    if (option.textContent === question.answer) {
      option.classList.add('correct');
    } else if (option.textContent === selectedAnswer) {
      option.classList.add('incorrect');
    }
    option.disabled = true;
  });

  // Avança para a próxima pergunta
  setTimeout(() => {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
      loadQuestion();
    } else {
      showResults();
    }
  }, 1000);
}

// Mostrar Resultados com Gráfico
function showResults() {
  showScreen('result-screen');
  
  const ctx = document.getElementById('performanceChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: Object.keys(performanceData),
      datasets: [{
        label: 'Taxa de Acertos (%)',
        data: Object.values(performanceData).map(data => 
          Math.round((data.correct / data.total) * 100)
        ),
        backgroundColor: '#1e3c72'
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          max: 100
        }
      }
    }
  });
}

// Event Listeners
document.getElementById('start-btn').addEventListener('click', initializeQuiz);
document.getElementById('restart-btn').addEventListener('click', () => {
  currentQuestionIndex = 0;
  score = 0;
  initializePerformanceData();
  initializeQuiz();
});