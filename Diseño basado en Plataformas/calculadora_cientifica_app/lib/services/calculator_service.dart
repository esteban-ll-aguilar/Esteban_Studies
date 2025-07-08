import 'dart:math';

class CalculatorService {
  String evaluateExpression(String expression) {
    try {
      // Reemplazar π y e con sus valores
      expression = expression.replaceAll('π', pi.toString());
      expression = expression.replaceAll('e', e.toString());
      
      // Implementar funciones trigonométricas, logarítmicas, etc.
      while (expression.contains('sin(') || 
             expression.contains('cos(') || 
             expression.contains('tan(') ||
             expression.contains('log(') ||
             expression.contains('ln(') ||
             expression.contains('√(')) {
        
        // Procesar raíz cuadrada
        RegExp sqrtRegex = RegExp(r'√\(([^()]+)\)');
        if (expression.contains('√(')) {
          var match = sqrtRegex.firstMatch(expression);
          if (match != null) {
            var value = _evaluateSimpleExpression(match.group(1)!);
            var sqrtValue = sqrt(double.parse(value));
            expression = expression.replaceFirst(match.group(0)!, sqrtValue.toString());
            continue;
          }
        }

        // Procesar seno
        RegExp sinRegex = RegExp(r'sin\(([^()]+)\)');
        if (expression.contains('sin(')) {
          var match = sinRegex.firstMatch(expression);
          if (match != null) {
            var value = _evaluateSimpleExpression(match.group(1)!);
            var sinValue = sin(double.parse(value));
            expression = expression.replaceFirst(match.group(0)!, sinValue.toString());
            continue;
          }
        }

        // Procesar coseno
        RegExp cosRegex = RegExp(r'cos\(([^()]+)\)');
        if (expression.contains('cos(')) {
          var match = cosRegex.firstMatch(expression);
          if (match != null) {
            var value = _evaluateSimpleExpression(match.group(1)!);
            var cosValue = cos(double.parse(value));
            expression = expression.replaceFirst(match.group(0)!, cosValue.toString());
            continue;
          }
        }

        // Procesar tangente
        RegExp tanRegex = RegExp(r'tan\(([^()]+)\)');
        if (expression.contains('tan(')) {
          var match = tanRegex.firstMatch(expression);
          if (match != null) {
            var value = _evaluateSimpleExpression(match.group(1)!);
            var tanValue = tan(double.parse(value));
            expression = expression.replaceFirst(match.group(0)!, tanValue.toString());
            continue;
          }
        }

        // Procesar logaritmo base 10
        RegExp logRegex = RegExp(r'log\(([^()]+)\)');
        if (expression.contains('log(')) {
          var match = logRegex.firstMatch(expression);
          if (match != null) {
            var value = _evaluateSimpleExpression(match.group(1)!);
            var logValue = log(double.parse(value)) / ln10;
            expression = expression.replaceFirst(match.group(0)!, logValue.toString());
            continue;
          }
        }

        // Procesar logaritmo natural
        RegExp lnRegex = RegExp(r'ln\(([^()]+)\)');
        if (expression.contains('ln(')) {
          var match = lnRegex.firstMatch(expression);
          if (match != null) {
            var value = _evaluateSimpleExpression(match.group(1)!);
            var lnValue = log(double.parse(value));
            expression = expression.replaceFirst(match.group(0)!, lnValue.toString());
            continue;
          }
        }

        break;
      }

      // Procesar potencias
      while (expression.contains('^')) {
        RegExp powerRegex = RegExp(r'([\d.]+)\^([\d.]+)');
        var match = powerRegex.firstMatch(expression);
        if (match != null) {
          var base = double.parse(match.group(1)!);
          var exponent = double.parse(match.group(2)!);
          var result = pow(base, exponent);
          expression = expression.replaceFirst(match.group(0)!, result.toString());
        } else {
          break;
        }
      }

      // Evaluar expresión básica
      var result = _evaluateSimpleExpression(expression);
      
      // Formatear resultado
      double resultValue = double.parse(result);
      if (resultValue == resultValue.toInt()) {
        return resultValue.toInt().toString();
      }
      return resultValue.toString();
    } catch (e) {
      return "Error";
    }
  }

  String _evaluateSimpleExpression(String expression) {
    // Implementación simplificada para operaciones básicas
    // Nota: En una app real, usarías una biblioteca de expresiones matemáticas
    
    // Reemplazar multiplicación y división
    expression = expression.replaceAll('×', '*');
    expression = expression.replaceAll('÷', '/');
    
    // Evaluar expresiones con operadores básicos
    List<String> tokens = [];
    String currentNumber = '';
    
    // Tokenizar la expresión
    for (int i = 0; i < expression.length; i++) {
      if ('0123456789.'.contains(expression[i])) {
        currentNumber += expression[i];
      } else if ('+-*/()'.contains(expression[i])) {
        if (currentNumber.isNotEmpty) {
          tokens.add(currentNumber);
          currentNumber = '';
        }
        tokens.add(expression[i]);
      }
    }
    if (currentNumber.isNotEmpty) {
      tokens.add(currentNumber);
    }
    
    // Implementación muy simplificada (solo suma y resta para el ejemplo)
    double result = 0;
    String operator = '+';
    
    for (int i = 0; i < tokens.length; i++) {
      if (tokens[i] == '+' || tokens[i] == '-' || tokens[i] == '*' || tokens[i] == '/') {
        operator = tokens[i];
      } else {
        double value = double.parse(tokens[i]);
        if (operator == '+') {
          result += value;
        } else if (operator == '-') {
          result -= value;
        } else if (operator == '*') {
          result *= value;
        } else if (operator == '/') {
          result /= value;
        }
      }
    }
    
    return result.toString();
  }
}
