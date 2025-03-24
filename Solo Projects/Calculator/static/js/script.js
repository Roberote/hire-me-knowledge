function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function deleteLast() {
    let display = document.getElementById('display');
    display.value = display.value.slice(0, -1);
}

function calculate() {
    let display = document.getElementById('display');
    try {
        display.value = eval(display.value);
    } catch (e) {
        display.value = 'Erro';
    }
}

async function calculateComplex() {
    let expression = document.getElementById('display').value;
    try {
        let response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ expression: expression })
        });
        let data = await response.json();
        if (data.error) {
            document.getElementById('display').value = 'Erro';
        } else {
            document.getElementById('display').value = data.result;
        }
    } catch (e) {
        document.getElementById('display').value = 'Erro';
    }
}