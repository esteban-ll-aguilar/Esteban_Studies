import 'package:flutter/material.dart';
import '../mcp/mcp.dart'; // Importamos el MCP

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
          // Botón de MCP
          Row(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              StreamBuilder<MCPAction>(
                stream: MCPService().actionStream,
                builder: (context, snapshot) {
                  // Determinar el color del indicador basado en la actividad reciente
                  Color indicatorColor = Colors.grey;
                  IconData iconData = Icons.assistant_outlined;
                  
                  if (snapshot.hasData) {
                    // Cambiar color basado en el tipo de acción
                    switch (snapshot.data!.type) {
                      case MCPActionType.prediction:
                        indicatorColor = Colors.purple;
                        iconData = Icons.psychology;
                        break;
                      case MCPActionType.suggestion:
                        indicatorColor = Colors.blue;
                        iconData = Icons.lightbulb_outline;
                        break;
                      case MCPActionType.automatic:
                        indicatorColor = Colors.orange;
                        iconData = Icons.auto_fix_high;
                        break;
                      case MCPActionType.notification:
                        indicatorColor = Colors.teal;
                        iconData = Icons.notifications_active;
                        break;
                    }
                  }
                  
                  return Row(
                    children: [
                      // Pequeño indicador de actividad
                      Container(
                        width: 10,
                        height: 10,
                        decoration: BoxDecoration(
                          color: indicatorColor,
                          shape: BoxShape.circle,
                        ),
                      ),
                      const SizedBox(width: 6),
                      Icon(
                        iconData,
                        color: indicatorColor,
                        size: 20,
                      ),
                      const SizedBox(width: 6),
                      IconButton(
                        icon: const Icon(Icons.assistant),
                        tooltip: 'Asistente MCP Predictivo',
                        onPressed: () {
                          // Mostrar una acción de ejemplo del MCP
                          final action = MCPAction(
                            type: MCPActionType.prediction,
                            message: "¿Puedo ayudarte a predecir tus próximos cálculos?",
                            action: () {
                              // Aquí iría la lógica real
                              ScaffoldMessenger.of(context).showSnackBar(
                                const SnackBar(
                                  content: Text('¡MCP Predictivo activado! Analizando patrones matemáticos...'),
                                  duration: Duration(seconds: 2),
                                ),
                              );
                            },
                            icon: Icons.psychology,
                          );
                          
                          MCPNotificationManager().showAction(context, action);
                        },
                      ),
                    ],
                  );
                },
              ),
            ],
          ),
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