document.addEventListener("DOMContentLoaded", function () {
    const questions = document.querySelectorAll(".question");
    const options = document.querySelectorAll(".option");
    const prevButton = document.getElementById("prev");
    const nextButton = document.getElementById("next");
    const submitButton = document.getElementById("submit");
    let currentQuestionIndex = 0;

    function showQuestion(index) {
        questions.forEach((q, i) => {
            q.classList.remove("active");
            q.style.opacity = 0;
            if (i === index) {
                q.classList.add("active");
                setTimeout(() => { q.style.opacity = 1; }, 100);
            }
        });

        prevButton.classList.toggle("hidden", index === 0);
        nextButton.classList.toggle("hidden", index === questions.length - 1);
        submitButton.classList.toggle("hidden", index !== questions.length - 1);
    }

    options.forEach(option => {
        option.addEventListener("click", function () {
            const parent = this.closest(".question");
            const optionsInGroup = parent.querySelectorAll(".option");

            optionsInGroup.forEach(opt => opt.classList.remove("selected"));
            this.classList.add("selected");

            parent.querySelector("input").checked = true;
        });
    });

    nextButton.addEventListener("click", () => {
        if (currentQuestionIndex < questions.length - 1) {
            currentQuestionIndex++;
            showQuestion(currentQuestionIndex);
        }
    });

    prevButton.addEventListener("click", () => {
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            showQuestion(currentQuestionIndex);
        }
    });

    showQuestion(currentQuestionIndex);

    // Criando partículas animadas no fundo
    const particleContainer = document.createElement("div");
    particleContainer.classList.add("particles");
    document.body.appendChild(particleContainer);

    function createParticle() {
        const particle = document.createElement("div");
        particle.classList.add("particle");
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.top = `${Math.random() * 100}%`;
        particle.style.animationDuration = `${2 + Math.random() * 3}s`;
        particleContainer.appendChild(particle);

        setTimeout(() => {
            particle.remove();
        }, 5000);
    }

    setInterval(createParticle, 300);
});
