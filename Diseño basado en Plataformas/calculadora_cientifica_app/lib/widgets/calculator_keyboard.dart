import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class CalculatorKeyboard extends StatelessWidget {
  final Function(String) onButtonPressed;
  final bool showScientificButtons;

  const CalculatorKeyboard({
    super.key,
    required this.onButtonPressed,
    required this.showScientificButtons,
  });

  @override
  Widget build(BuildContext context) {
    // Cambiado de Column a Expanded para evitar el error de altura ilimitada
    return Expanded(
      flex: 5,
      child: Column(
        children: [
          // Scientific buttons (conditional)
          if (showScientificButtons)
            _buildScientificButtons(context),
          
          // Basic calculator buttons
          _buildBasicButtons(context),
        ],
      ),
    );
  }

  Widget _buildScientificButtons(BuildContext context) {
    return AnimatedContainer(
      duration: const Duration(milliseconds: 300),
      curve: Curves.easeInOut,
      padding: const EdgeInsets.fromLTRB(8.0, 4.0, 8.0, 12.0),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.secondaryContainer.withOpacity(0.3),
        borderRadius: const BorderRadius.vertical(bottom: Radius.circular(16)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildButton(context, "sin", isFunction: true, tooltip: "Seno"),
              _buildButton(context, "cos", isFunction: true, tooltip: "Coseno"),
              _buildButton(context, "tan", isFunction: true, tooltip: "Tangente"),
              _buildButton(context, "π", isSpecial: true, tooltip: "Pi (3.1415...)"),
            ],
          ),
          const SizedBox(height: 8),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildButton(context, "x²", isFunction: true, tooltip: "Cuadrado"),
              _buildButton(context, "x³", isFunction: true, tooltip: "Cubo"),
              _buildButton(context, "xʸ", isFunction: true, tooltip: "Potencia"),
              _buildButton(context, "e", isSpecial: true, tooltip: "Número e (2.7182...)"),
            ],
          ),
          const SizedBox(height: 8),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildButton(context, "log", isFunction: true, tooltip: "Logaritmo base 10"),
              _buildButton(context, "ln", isFunction: true, tooltip: "Logaritmo natural"),
              _buildButton(context, "√", isFunction: true, tooltip: "Raíz cuadrada"),
              _buildButton(context, "(", isOperator: true, tooltip: "Paréntesis izquierdo"),
              _buildButton(context, ")", isOperator: true, tooltip: "Paréntesis derecho"),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildBasicButtons(BuildContext context) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          children: [
            Expanded(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  _buildButton(context, "C", isClear: true),
                  _buildButton(context, "⌫", isOperator: true),
                  _buildButton(context, "%", isOperator: true),
                  _buildButton(context, "÷", isOperator: true),
                ],
              ),
            ),
            Expanded(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  _buildButton(context, "7"),
                  _buildButton(context, "8"),
                  _buildButton(context, "9"),
                  _buildButton(context, "×", isOperator: true),
                ],
              ),
            ),
            Expanded(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  _buildButton(context, "4"),
                  _buildButton(context, "5"),
                  _buildButton(context, "6"),
                  _buildButton(context, "-", isOperator: true),
                ],
              ),
            ),
            Expanded(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  _buildButton(context, "1"),
                  _buildButton(context, "2"),
                  _buildButton(context, "3"),
                  _buildButton(context, "+", isOperator: true),
                ],
              ),
            ),
            Expanded(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  _buildButton(context, "0", flex: 2),
                  _buildButton(context, "."),
                  _buildButton(context, "=", isEquals: true),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildButton(BuildContext context, String text, {
    bool isOperator = false, 
    bool isClear = false, 
    bool isEquals = false,
    bool isFunction = false,
    bool isSpecial = false,
    String? tooltip,
    int flex = 1
  }) {
    Color backgroundColor;
    Color textColor;
    Color splashColor;
    IconData? iconData;
    
    if (isEquals) {
      backgroundColor = Theme.of(context).colorScheme.primary;
      textColor = Theme.of(context).colorScheme.onPrimary;
      splashColor = Theme.of(context).colorScheme.onPrimary.withOpacity(0.3);
    } else if (isOperator) {
      backgroundColor = Theme.of(context).colorScheme.primaryContainer;
      textColor = Theme.of(context).colorScheme.onPrimaryContainer;
      splashColor = Theme.of(context).colorScheme.onPrimaryContainer.withOpacity(0.3);
    } else if (isClear) {
      backgroundColor = Theme.of(context).colorScheme.errorContainer;
      textColor = Theme.of(context).colorScheme.onErrorContainer;
      splashColor = Theme.of(context).colorScheme.onErrorContainer.withOpacity(0.3);
    } else if (isFunction || isSpecial) {
      backgroundColor = Theme.of(context).colorScheme.secondaryContainer;
      textColor = Theme.of(context).colorScheme.onSecondaryContainer;
      splashColor = Theme.of(context).colorScheme.onSecondaryContainer.withOpacity(0.3);
    } else {
      backgroundColor = Theme.of(context).colorScheme.surfaceVariant;
      textColor = Theme.of(context).colorScheme.onSurfaceVariant;
      splashColor = Theme.of(context).colorScheme.onSurfaceVariant.withOpacity(0.3);
    }
    
    // Asignar iconos en lugar de texto para algunos botones
    if (text == "⌫") {
      iconData = Icons.backspace_outlined;
    } else if (text == "C") {
      iconData = Icons.clear;
    } else if (text == "=") {
      iconData = Icons.done;
    }
    
    return Expanded(
      flex: flex,
      child: Padding(
        padding: const EdgeInsets.all(4.0),
        child: Tooltip(
          message: tooltip ?? text,
          child: Material(
            color: backgroundColor,
            borderRadius: BorderRadius.circular(16),
            elevation: 2,
            shadowColor: Colors.black26,
            child: InkWell(
              borderRadius: BorderRadius.circular(16),
              splashColor: splashColor,
              highlightColor: splashColor.withOpacity(0.5),
              onTap: () {
                HapticFeedback.lightImpact(); // Retroalimentación táctil
                onButtonPressed(text);
              },
              child: Container(
                alignment: Alignment.center,
                padding: const EdgeInsets.all(8),
                child: iconData != null
                    ? Icon(iconData, color: textColor, size: 24)
                    : Text(
                        text,
                        style: TextStyle(
                          fontSize: 22,
                          fontWeight: isFunction || isOperator || isSpecial || isEquals
                              ? FontWeight.bold
                              : FontWeight.normal,
                          color: textColor,
                        ),
                      ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
