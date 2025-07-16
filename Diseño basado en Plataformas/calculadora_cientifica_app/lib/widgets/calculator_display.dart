import 'package:flutter/material.dart';

class CalculatorDisplay extends StatelessWidget {
  final String input;
  final String output;

  const CalculatorDisplay({
    super.key,
    required this.input,
    required this.output,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16.0),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.surface,
        borderRadius: BorderRadius.circular(16.0),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.1),
            blurRadius: 8.0,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.end,
        children: [
          // Entrada del usuario
          Container(
            alignment: Alignment.centerRight,
            padding: const EdgeInsets.symmetric(vertical: 8.0, horizontal: 12.0),
            child: Text(
              input,
              style: const TextStyle(fontSize: 32),
              textAlign: TextAlign.right,
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
            ),
          ),
          
          // Resultado
          if (output.isNotEmpty)
            Container(
              alignment: Alignment.centerRight,
              padding: const EdgeInsets.symmetric(vertical: 8.0, horizontal: 12.0),
              child: AnimatedDefaultTextStyle(
                style: TextStyle(
                  fontSize: 24,
                  color: Theme.of(context).colorScheme.primary,
                  fontFamily: 'Roboto',
                ),
                duration: const Duration(milliseconds: 200),
                child: Text(output),
              ),
            ),
        ],
      ),
    );
  }
}