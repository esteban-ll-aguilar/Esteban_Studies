import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../widgets/calculator_display.dart';
import '../widgets/calculator_keyboard.dart';
import '../services/calculator_service.dart';

class CalculadoraCientifica extends StatefulWidget {
  const CalculadoraCientifica({super.key});

  @override
  State<CalculadoraCientifica> createState() => _CalculadoraCientificaState();
}

class _CalculadoraCientificaState extends State<CalculadoraCientifica> with SingleTickerProviderStateMixin {
  final CalculatorService _calculatorService = CalculatorService();
  String _input = "";
  String _output = "0";
  bool _showScientificButtons = false;
  late AnimationController _animationController;
  late Animation<double> _animation;
  
  @override
  void initState() {
    super.initState();
    _animationController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 300),
    );
    _animation = CurvedAnimation(
      parent: _animationController,
      curve: Curves.easeInOut,
    );
  }

  @override
  void dispose() {
    _animationController.dispose();
    super.dispose();
  }

  void _onButtonPressed(String buttonText) {
    HapticFeedback.selectionClick();
    setState(() {
      if (buttonText == "C") {
        _input = "";
        _output = "0";
      } else if (buttonText == "⌫") {
        if (_input.isNotEmpty) {
          _input = _input.substring(0, _input.length - 1);
        }
      } else if (buttonText == "=") {
        try {
          _output = _calculatorService.evaluateExpression(_input);
          if (_output != "Error") {
            _input = _output;
          }
        } catch (e) {
          _output = "Error";
        }
      } else if (buttonText == "sin" || buttonText == "cos" || buttonText == "tan" ||
                 buttonText == "log" || buttonText == "ln" || buttonText == "√") {
        _input += "$buttonText(";
      } else if (buttonText == "π") {
        _input += "π";
      } else if (buttonText == "e") {
        _input += "e";
      } else if (buttonText == "x²") {
        _input += "^2";
      } else if (buttonText == "x³") {
        _input += "^3";
      } else if (buttonText == "xʸ") {
        _input += "^";
      } else {
        _input += buttonText;
      }
    });
  }

  void _toggleScientificButtons() {
    setState(() {
      _showScientificButtons = !_showScientificButtons;
      if (_showScientificButtons) {
        _animationController.forward();
      } else {
        _animationController.reverse();
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Calculadora Científica', 
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        backgroundColor: Theme.of(context).colorScheme.primary,
        foregroundColor: Theme.of(context).colorScheme.onPrimary,
        elevation: 0,
        actions: [
          Tooltip(
            message: _showScientificButtons 
                ? "Ocultar funciones científicas" 
                : "Mostrar funciones científicas",
            child: IconButton(
              icon: AnimatedIcon(
                icon: AnimatedIcons.menu_close,
                progress: _animation,
              ),
              onPressed: _toggleScientificButtons,
            ),
          ),
        ],
      ),
      body: SafeArea(
        child: Column(
          children: [
            // Display
            CalculatorDisplay(input: _input, output: _output),
            
            // Calculator Keyboard
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
