<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f9;
        }
        .calculator {
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        .calculator-display {
            width: 100%;
            height: 50px;
            font-size: 1.5rem;
            text-align: right;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background: #f9f9f9;
        }
        .calculator-buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
        }
        .button {
            padding: 15px;
            font-size: 1.2rem;
            border: none;
            border-radius: 5px;
            background-color: #007BFF;
            color: white;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .button:hover {
            background-color: #0056b3;
        }
        .button.clear {
            background-color: #dc3545;
        }
        .button.clear:hover {
            background-color: #a71d2a;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <input type="text" id="display" class="calculator-display" disabled />
        <div class="calculator-buttons">
            <button class="button" onclick="appendNumber('7')">7</button>
            <button class="button" onclick="appendNumber('8')">8</button>
            <button class="button" onclick="appendNumber('9')">9</button>
            <button class="button" onclick="setOperation('/')">/</button>

            <button class="button" onclick="appendNumber('4')">4</button>
            <button class="button" onclick="appendNumber('5')">5</button>
            <button class="button" onclick="appendNumber('6')">6</button>
            <button class="button" onclick="setOperation('*')">*</button>

            <button class="button" onclick="appendNumber('1')">1</button>
            <button class="button" onclick="appendNumber('2')">2</button>
            <button class="button" onclick="appendNumber('3')">3</button>
            <button class="button" onclick="setOperation('-')">-</button>

            <button class="button" onclick="appendNumber('0')">0</button>
            <button class="button" onclick="appendNumber('.')">.</button>
            <button class="button" onclick="calculate()">=</button>
            <button class="button" onclick="setOperation('+')">+</button>

            <button class="button clear" onclick="clearDisplay()">C</button>
        </div>
    </div>

    <script>
        let currentInput = '';
        let currentOperation = null;
        let previousInput = '';

        function appendNumber(number) {
            currentInput += number;
            updateDisplay();
        }

        function setOperation(operation) {
            if (currentInput === '') return;
            if (previousInput !== '') {
                calculate();
            }
            currentOperation = operation;
            previousInput = currentInput;
            currentInput = '';
        }

        function calculate() {
            if (currentOperation === null || currentInput === '' || previousInput === '') return;
            const a = parseFloat(previousInput);
            const b = parseFloat(currentInput);
            let result;

            switch (currentOperation) {
                case '+':
                    result = a + b;
                    break;
                case '-':
                    result = a - b;
                    break;
                case '*':
                    result = a * b;
                    break;
                case '/':
                    result = b === 0 ? 'Error' : a / b;
                    break;
                default:
                    return;
            }

            currentInput = result.toString();
            currentOperation = null;
            previousInput = '';
            updateDisplay();
        }

        function clearDisplay() {
            currentInput = '';
            currentOperation = null;
            previousInput = '';
            updateDisplay();
        }

        function updateDisplay() {
            const display = document.getElementById('display');
            display.value = currentInput;
        }
    </script>
</body>
</html>
