import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../widgets/calculator_keyboard.dart';
import '../widgets/calculator_display.dart';
import 'dart:math' as math;

class CalculadoraCientifica extends StatefulWidget {
  const CalculadoraCientifica({super.key});

  @override
  State<CalculadoraCientifica> createState() => _CalculadoraCientificaState();
}

class _CalculadoraCientificaState extends State<CalculadoraCientifica> {
  String _input = "0";
  String _output = "";
  bool _showScientificButtons = false;
  final List<String> _history = [];
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();
  
  void _onButtonPressed(String buttonText) {
    setState(() {
      // Procesa la entrada según el botón presionado
      if (buttonText == "C") {
        _clearAll();
      } else if (buttonText == "⌫") {
        _backspace();
      } else if (buttonText == "=") {
        _calculate();
      } else if (buttonText == "sin" || buttonText == "cos" || buttonText == "tan" ||
                buttonText == "log" || buttonText == "ln" || buttonText == "√") {
        _addFunction(buttonText);
      } else if (buttonText == "π") {
        _addConstant(math.pi.toString());
      } else if (buttonText == "e") {
        _addConstant(math.e.toString());
      } else if (buttonText == "x²") {
        _addPower(2);
      } else if (buttonText == "x³") {
        _addPower(3);
      } else if (buttonText == "xʸ") {
        _addOperator("^");
      } else {
        _addToInput(buttonText);
      }
    });
  }

  void _clearAll() {
    _input = "0";
    _output = "";
  }

  void _backspace() {
    if (_input.length > 1) {
      _input = _input.substring(0, _input.length - 1);
    } else {
      _input = "0";
    }
  }

  void _addToInput(String value) {
    if (_input == "0" && value != ".") {
      _input = value;
    } else {
      _input += value;
    }
  }

  void _addFunction(String func) {
    _input += "$func(";
  }

  void _addConstant(String value) {
    if (_input == "0") {
      _input = value;
    } else {
      _input += value;
    }
  }

  void _addPower(int power) {
    _input += "^$power";
  }

  void _addOperator(String operator) {
    _input += operator;
  }

  void _calculate() {
    try {
      // Simulación simple de cálculo para demostración
      // En una implementación real, se necesitaría un evaluador de expresiones matemáticas
      _output = _evaluateExpression(_input);
      _history.add("$_input = $_output");
      _input = _output;
    } catch (e) {
      _output = "Error";
    }
  }

  // Evaluador simple de expresiones (solo para demostración)
  String _evaluateExpression(String expression) {
    // Esta es una implementación muy básica para demostración
    // En una calculadora real, necesitarías un analizador más complejo
    try {
      // Simulemos algunos cálculos básicos
      if (expression.contains('+')) {
        List<String> parts = expression.split('+');
        double result = double.parse(parts[0]) + double.parse(parts[1]);
        return result.toString();
      } else if (expression.contains('-')) {
        List<String> parts = expression.split('-');
        double result = double.parse(parts[0]) - double.parse(parts[1]);
        return result.toString();
      } else if (expression.contains('×')) {
        List<String> parts = expression.split('×');
        double result = double.parse(parts[0]) * double.parse(parts[1]);
        return result.toString();
      } else if (expression.contains('÷')) {
        List<String> parts = expression.split('÷');
        double result = double.parse(parts[0]) / double.parse(parts[1]);
        return result.toString();
      }
      return expression; // Si no hay operación, devuelve la expresión original
    } catch (e) {
      return "Error"; // En caso de cualquier error
    }
  }

  void _toggleScientificMode(bool value) {
    setState(() {
      _showScientificButtons = value;
      HapticFeedback.lightImpact(); // Retroalimentación táctil al cambiar modo
    });
  }

  void _showHistoryDialog() {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text('Historial de cálculos'),
          content: SizedBox(
            width: double.maxFinite,
            child: _history.isEmpty
                ? const Center(child: Text('No hay historial disponible'))
                : ListView.builder(
                    itemCount: _history.length,
                    itemBuilder: (context, index) {
                      return ListTile(
                        title: Text(_history[_history.length - 1 - index]),
                        onTap: () {
                          setState(() {
                            _input = _history[_history.length - 1 - index].split(' = ')[0];
                          });
                          Navigator.pop(context);
                        },
                      );
                    },
                  ),
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: const Text('Cerrar'),
            ),
            TextButton(
              onPressed: () {
                setState(() {
                  _history.clear();
                });
                Navigator.of(context).pop();
              },
              child: const Text('Limpiar historial'),
            ),
          ],
        );
      },
    );
  }

  void _showSettingsDialog() {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text('Configuración'),
          content: const SingleChildScrollView(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Próximamente: opciones de configuración'),
              ],
            ),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('Cerrar'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: _scaffoldKey,
      appBar: AppBar(
        title: const Text('Calculadora Científica'),
        centerTitle: true,
        elevation: 2,
        actions: [
          Tooltip(
            message: _showScientificButtons ? 'Modo básico' : 'Modo científico',
            child: Switch(
              value: _showScientificButtons,
              onChanged: _toggleScientificMode,
              activeColor: Theme.of(context).colorScheme.primary,
            ),
          ),
          IconButton(
            icon: const Icon(Icons.history),
            tooltip: 'Historial',
            onPressed: _showHistoryDialog,
          ),
          const SizedBox(width: 8),
        ],
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            DrawerHeader(
              decoration: BoxDecoration(
                color: Theme.of(context).colorScheme.primary,
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  const Icon(
                    Icons.calculate_rounded,
                    color: Colors.white,
                    size: 40,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    'Calculadora Científica',
                    style: TextStyle(
                      color: Theme.of(context).colorScheme.onPrimary,
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    'Versión 1.0.0',
                    style: TextStyle(
                      color: Theme.of(context).colorScheme.onPrimary.withOpacity(0.8),
                      fontSize: 14,
                    ),
                  ),
                ],
              ),
            ),
            ListTile(
              leading: const Icon(Icons.history),
              title: const Text('Historial'),
              onTap: () {
                Navigator.pop(context);
                _showHistoryDialog();
              },
            ),
            const Divider(),
            ListTile(
              leading: const Icon(Icons.settings),
              title: const Text('Configuración'),
              onTap: () {
                Navigator.pop(context);
                _showSettingsDialog();
              },
            ),
            ListTile(
              leading: const Icon(Icons.dark_mode),
              title: const Text('Tema oscuro'),
              trailing: Switch(
                value: Theme.of(context).brightness == Brightness.dark,
                onChanged: (value) {
                  // Aquí iría la lógica para cambiar el tema
                  Navigator.pop(context);
                },
              ),
            ),
            const Divider(),
            ListTile(
              leading: const Icon(Icons.info_outline),
              title: const Text('Acerca de'),
              onTap: () {
                Navigator.pop(context);
                showAboutDialog(
                  context: context,
                  applicationName: 'Calculadora Científica',
                  applicationVersion: '1.0.0',
                  applicationIcon: const Icon(Icons.calculate_rounded),
                  children: const [
                    Text('Una calculadora científica avanzada con múltiples funcionalidades.'),
                    SizedBox(height: 12),
                    Text('Desarrollada con Flutter.'),
                  ],
                );
              },
            ),
          ],
        ),
      ),
      body: SafeArea(
        child: Column(
          children: [
            // Display
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: CalculatorDisplay(
                input: _input,
                output: _output,
              ),
            ),
            
            // Keyboard
            CalculatorKeyboard(
              onButtonPressed: _onButtonPressed,
              showScientificButtons: _showScientificButtons,
            ),
          ],
        ),
      ),
    );
  }
}

    