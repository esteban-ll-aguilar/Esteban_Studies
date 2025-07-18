import 'package:flutter/material.dart';

// Enumeración para los tipos de acciones
enum MCPActionType {
  suggestion,  // Recomendación que requiere aprobación del usuario
  automatic,   // Acción ejecutada automáticamente
  notification, // Solo notificación informativa
  prediction   // Predicción basada en patrones de uso
}

// Clase para representar una acción del MCP
class MCPAction {
  final MCPActionType type;
  final String message;
  final Function() action;
  final IconData icon;
  final DateTime timestamp;
  final dynamic data; // Campo adicional para datos específicos de la acción
  
  MCPAction({
    required this.type,
    required this.message,
    required this.action,
    required this.icon,
    DateTime? timestamp,
    this.data,
  }) : timestamp = timestamp ?? DateTime.now();
  
  // Para crear una copia de la acción con algunos cambios
  MCPAction copyWith({
    MCPActionType? type,
    String? message,
    Function()? action,
    IconData? icon,
    DateTime? timestamp,
    dynamic data,
  }) {
    return MCPAction(
      type: type ?? this.type,
      message: message ?? this.message,
      action: action ?? this.action,
      icon: icon ?? this.icon,
      timestamp: timestamp ?? this.timestamp,
      data: data ?? this.data,
    );
  }
}
