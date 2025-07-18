import 'package:flutter/material.dart';
import 'mcp_action.dart';

class MCPSuggestionWidget extends StatelessWidget {
  final MCPAction action;
  final VoidCallback onAccept;
  final VoidCallback onDismiss;

  const MCPSuggestionWidget({
    super.key,
    required this.action,
    required this.onAccept,
    required this.onDismiss,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 4,
      margin: const EdgeInsets.all(8),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
      ),
      color: _getCardColor(context, action.type),
      child: Padding(
        padding: const EdgeInsets.all(12),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Row(
              children: [
                Icon(
                  action.icon,
                  color: _getIconColor(context, action.type),
                  size: 24,
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Text(
                    action.message,
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.w500,
                      color: _getTextColor(context, action.type),
                    ),
                  ),
                ),
              ],
            ),
            if (action.data != null) ...[
              const SizedBox(height: 8),
              Container(
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: Theme.of(context).colorScheme.surface.withOpacity(0.7),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Text(
                  action.data.toString(),
                  style: TextStyle(
                    fontStyle: FontStyle.italic,
                    color: Theme.of(context).colorScheme.onSurface,
                  ),
                ),
              ),
            ],
            const SizedBox(height: 12),
            Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                if (action.type == MCPActionType.suggestion || 
                   action.type == MCPActionType.prediction) ...[
                  TextButton(
                    onPressed: onDismiss,
                    child: const Text('No, gracias'),
                  ),
                  const SizedBox(width: 8),
                  ElevatedButton(
                    onPressed: () {
                      action.action();
                      onAccept();
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: _getActionButtonColor(context, action.type),
                    ),
                    child: const Text('Aceptar'),
                  ),
                ] else if (action.type == MCPActionType.automatic) ...[
                  TextButton(
                    onPressed: onDismiss,
                    child: const Text('Entendido'),
                  ),
                ] else ...[
                  TextButton(
                    onPressed: onDismiss,
                    child: const Text('Cerrar'),
                  ),
                ],
              ],
            ),
          ],
        ),
      ),
    );
  }

  Color _getIconColor(BuildContext context, MCPActionType type) {
    switch (type) {
      case MCPActionType.suggestion:
        return Theme.of(context).colorScheme.primary;
      case MCPActionType.automatic:
        return Theme.of(context).colorScheme.tertiary;
      case MCPActionType.notification:
        return Theme.of(context).colorScheme.secondary;
      case MCPActionType.prediction:
        return Colors.purple;
    }
  }
  
  Color _getCardColor(BuildContext context, MCPActionType type) {
    switch (type) {
      case MCPActionType.suggestion:
        return Theme.of(context).colorScheme.surface;
      case MCPActionType.automatic:
        return Theme.of(context).colorScheme.tertiaryContainer.withOpacity(0.3);
      case MCPActionType.notification:
        return Theme.of(context).colorScheme.surface;
      case MCPActionType.prediction:
        return Colors.purple.withOpacity(0.1);
    }
  }
  
  Color _getTextColor(BuildContext context, MCPActionType type) {
    switch (type) {
      case MCPActionType.suggestion:
      case MCPActionType.notification:
      case MCPActionType.automatic:
        return Theme.of(context).colorScheme.onSurface;
      case MCPActionType.prediction:
        return Colors.purple.shade900;
    }
  }
  
  Color _getActionButtonColor(BuildContext context, MCPActionType type) {
    switch (type) {
      case MCPActionType.suggestion:
        return Theme.of(context).colorScheme.primary;
      case MCPActionType.automatic:
        return Theme.of(context).colorScheme.tertiary;
      case MCPActionType.notification:
        return Theme.of(context).colorScheme.secondary;
      case MCPActionType.prediction:
        return Colors.purple;
    }
  }
}
