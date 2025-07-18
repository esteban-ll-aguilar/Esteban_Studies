import 'package:flutter/material.dart';
import 'mcp_action.dart';
import 'mcp_suggestion_widget.dart';

class MCPNotificationManager {
  // Singleton pattern
  static final MCPNotificationManager _instance = MCPNotificationManager._internal();
  factory MCPNotificationManager() => _instance;
  MCPNotificationManager._internal();

  // Cola de notificaciones pendientes
  final List<MCPAction> _pendingActions = [];
  
  // Mostrar una acción como notificación/sugerencia
  void showAction(BuildContext context, MCPAction action) {
    // Si es una acción automática, ejecutarla inmediatamente
    if (action.type == MCPActionType.automatic) {
      // Ejecutar la acción
      action.action();
    }
    
    // Añadir a la cola y mostrar
    _pendingActions.add(action);
    _showNextAction(context);
  }
  
  // Mostrar la siguiente acción en la cola
  void _showNextAction(BuildContext context) {
    if (_pendingActions.isEmpty) return;
    
    final action = _pendingActions.first;
    
    // Usar OverlayEntry para mostrar la notificación
    final overlayState = Overlay.of(context);
    late final OverlayEntry overlayEntry;
    
    overlayEntry = OverlayEntry(
      builder: (context) => Positioned(
        bottom: 20,
        left: 20,
        right: 20,
        child: MCPSuggestionWidget(
          action: action,
          onAccept: () {
            // Remover de la cola y cerrar
            _pendingActions.remove(action);
            overlayEntry.remove();
            
            // Mostrar siguiente si hay
            if (_pendingActions.isNotEmpty) {
              _showNextAction(context);
            }
          },
          onDismiss: () {
            // Remover de la cola y cerrar
            _pendingActions.remove(action);
            overlayEntry.remove();
            
            // Mostrar siguiente si hay
            if (_pendingActions.isNotEmpty) {
              _showNextAction(context);
            }
          },
        ),
      ),
    );
    
    // Insertar en el overlay
    overlayState.insert(overlayEntry);
    
    // Auto-cerrar después de un tiempo para notificaciones
    if (action.type == MCPActionType.notification) {
      Future.delayed(const Duration(seconds: 5), () {
        if (_pendingActions.contains(action)) {
          _pendingActions.remove(action);
          overlayEntry.remove();
          
          // Mostrar siguiente si hay
          if (_pendingActions.isNotEmpty) {
            _showNextAction(context);
          }
        }
      });
    }
  }
}
