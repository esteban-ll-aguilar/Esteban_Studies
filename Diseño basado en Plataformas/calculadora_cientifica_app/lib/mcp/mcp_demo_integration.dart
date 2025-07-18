import 'package:flutter/material.dart';
import 'mcp_optimized_service.dart';
import 'mcp_ai_recommendation_widget.dart';
import 'mcp_notification_manager.dart';
import 'mcp_action.dart';

/// Demostración de integración del sistema MCP optimizado con IA
/// Muestra cómo implementar el sistema completo en una aplicación
class MCPDemoIntegration extends StatefulWidget {
  const MCPDemoIntegration({super.key});

  @override
  State<MCPDemoIntegration> createState() => _MCPDemoIntegrationState();
}

class _MCPDemoIntegrationState extends State<MCPDemoIntegration> {
  final MCPOptimizedService _mcpService = MCPOptimizedService();
  final List<String> _actionLog = [];
  bool _isAIEnabled = true;
  
  @override
  void initState() {
    super.initState();
    _initializeMCPSystem();
  }

  /// Inicializa el sistema MCP optimizado
  void _initializeMCPSystem() {
    // Registrar callback para acciones de la calculadora
    _mcpService.registerCalculatorCallback(_handleCalculatorAction);
    
    // Configurar listener para recomendaciones de IA
    _mcpService.actionStream.listen((action) {
      if (mounted) {
        _showAIRecommendation(action);
      }
    });
    
    // Configuración inicial del sistema
    _mcpService.updateSystemConfiguration({
      'enablePredictiveMode': _isAIEnabled,
      'confidenceThreshold': 0.6,
      'maxRecommendationsPerSession': 3,
    });
    
    // Simular algunas acciones iniciales para entrenar el sistema
    _simulateInitialTraining();
  }

  /// Simula acciones iniciales para entrenar el sistema de IA
  void _simulateInitialTraining() {
    final trainingActions = [
      '2', '+', '3', '=',
      '5', '×', '4', '=',
      'sin', '(', '30', ')', '=',
      '√', '16', '=',
      '10', '÷', '2', '=',
    ];

    // Ejecutar acciones de entrenamiento con delay
    for (int i = 0; i < trainingActions.length; i++) {
      Future.delayed(Duration(milliseconds: i * 100), () {
        if (mounted) {
          _trackAction(trainingActions[i]);
        }
      });
    }
  }

  /// Maneja acciones de la calculadora
  void _handleCalculatorAction(String action, {dynamic data}) {
    setState(() {
      _actionLog.add('Acción ejecutada: $action${data != null ? ' (datos: $data)' : ''}');
    });

    // Mostrar feedback al usuario
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('MCP ejecutó: $action'),
        duration: const Duration(seconds: 2),
        backgroundColor: Colors.green,
      ),
    );
  }

  /// Rastrea una acción del usuario
  void _trackAction(String action) {
    _mcpService.trackUserAction(action, additionalContext: {
      'timestamp': DateTime.now().toIso8601String(),
      'userInterface': 'demo',
    });

    // Actualizar contexto
    _mcpService.updateContext(
      currentScreen: 'demo',
      currentInput: action,
      scientificModeEnabled: ['sin', 'cos', 'tan', 'log', '√'].contains(action),
    );

    setState(() {
      _actionLog.add('Acción rastreada: $action');
    });
  }

  /// Muestra una recomendación de IA
  void _showAIRecommendation(MCPAction action) {
    final overlayState = Overlay.of(context);
    late final OverlayEntry overlayEntry;

    overlayEntry = OverlayEntry(
      builder: (context) => Positioned(
        top: 100,
        left: 20,
        right: 20,
        child: MCPAIRecommendationWidget(
          action: action,
          onAccept: () {
            overlayEntry.remove();
            setState(() {
              _actionLog.add('Recomendación aceptada: ${action.message}');
            });
          },
          onDismiss: () {
            overlayEntry.remove();
            setState(() {
              _actionLog.add('Recomendación rechazada: ${action.message}');
            });
          },
          onFeedback: (isHelpful) {
            _mcpService.provideFeedback('demo_recommendation', isHelpful);
            setState(() {
              _actionLog.add('Feedback enviado: ${isHelpful ? 'Útil' : 'No útil'}');
            });
          },
        ),
      ),
    );

    overlayState.insert(overlayEntry);

    // Auto-remover después de 10 segundos si no hay interacción
    Future.delayed(const Duration(seconds: 10), () {
      if (overlayEntry.mounted) {
        overlayEntry.remove();
      }
    });
  }

  /// Ejecuta acciones automáticas inteligentes
  void _executeAutoActions() {
    _mcpService.executeIntelligentAutoActions(context);
    setState(() {
      _actionLog.add('Acciones automáticas ejecutadas');
    });
  }

  /// Obtiene y muestra métricas del sistema
  void _showSystemMetrics() {
    final metrics = _mcpService.getSystemMetrics();
    
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Métricas del Sistema MCP'),
        content: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              _buildMetricSection('Métricas de IA', metrics['aiMetrics']),
              const SizedBox(height: 16),
              _buildMetricSection('Rendimiento', metrics['performanceMetrics']),
              const SizedBox(height: 16),
              _buildMetricSection('Configuración', metrics['systemConfig']),
            ],
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: const Text('Cerrar'),
          ),
        ],
      ),
    );
  }

  Widget _buildMetricSection(String title, dynamic data) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          title,
          style: const TextStyle(
            fontSize: 16,
            fontWeight: FontWeight.bold,
          ),
        ),
        const SizedBox(height: 8),
        Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: Colors.grey[100],
            borderRadius: BorderRadius.circular(8),
          ),
          child: Text(
            data.toString(),
            style: const TextStyle(
              fontFamily: 'monospace',
              fontSize: 12,
            ),
          ),
        ),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Demo MCP con IA Avanzada'),
        backgroundColor: Colors.purple,
        foregroundColor: Colors.white,
        actions: [
          Switch(
            value: _isAIEnabled,
            onChanged: (value) {
              setState(() {
                _isAIEnabled = value;
              });
              _mcpService.updateSystemConfiguration({
                'enablePredictiveMode': value,
              });
            },
            activeColor: Colors.white,
          ),
          IconButton(
            icon: const Icon(Icons.analytics),
            onPressed: _showSystemMetrics,
            tooltip: 'Ver métricas',
          ),
        ],
      ),
      body: Column(
        children: [
          // Panel de control
          Container(
            padding: const EdgeInsets.all(16),
            color: Colors.grey[100],
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Sistema MCP ${_isAIEnabled ? 'ACTIVO' : 'INACTIVO'}',
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                    color: _isAIEnabled ? Colors.green : Colors.red,
                  ),
                ),
                const SizedBox(height: 12),
                
                // Botones de demostración
                Wrap(
                  spacing: 8,
                  runSpacing: 8,
                  children: [
                    ElevatedButton.icon(
                      onPressed: () => _trackAction('2'),
                      icon: const Icon(Icons.looks_two),
                      label: const Text('Número'),
                    ),
                    ElevatedButton.icon(
                      onPressed: () => _trackAction('+'),
                      icon: const Icon(Icons.add),
                      label: const Text('Suma'),
                    ),
                    ElevatedButton.icon(
                      onPressed: () => _trackAction('sin'),
                      icon: const Icon(Icons.waves),
                      label: const Text('Seno'),
                    ),
                    ElevatedButton.icon(
                      onPressed: () => _trackAction('='),
                      icon: const Icon(Icons.drag_handle),
                      label: const Text('Igual'),
                    ),
                    ElevatedButton.icon(
                      onPressed: _executeAutoActions,
                      icon: const Icon(Icons.auto_awesome),
                      label: const Text('Auto'),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.orange,
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
          
          // Log de acciones
          Expanded(
            child: Container(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      const Text(
                        'Log de Actividad',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      TextButton(
                        onPressed: () {
                          setState(() {
                            _actionLog.clear();
                          });
                        },
                        child: const Text('Limpiar'),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),
                  
                  Expanded(
                    child: Container(
                      decoration: BoxDecoration(
                        border: Border.all(color: Colors.grey[300]!),
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: _actionLog.isEmpty
                          ? const Center(
                              child: Text(
                                'No hay actividad registrada',
                                style: TextStyle(
                                  color: Colors.grey,
                                  fontStyle: FontStyle.italic,
                                ),
                              ),
                            )
                          : ListView.builder(
                              itemCount: _actionLog.length,
                              itemBuilder: (context, index) {
                                final log = _actionLog[_actionLog.length - 1 - index];
                                return ListTile(
                                  dense: true,
                                  leading: CircleAvatar(
                                    radius: 12,
                                    backgroundColor: _getLogColor(log),
                                    child: Text(
                                      '${_actionLog.length - index}',
                                      style: const TextStyle(
                                        fontSize: 10,
                                        color: Colors.white,
                                      ),
                                    ),
                                  ),
                                  title: Text(
                                    log,
                                    style: const TextStyle(fontSize: 14),
                                  ),
                                  subtitle: Text(
                                    DateTime.now().toString().substring(11, 19),
                                    style: TextStyle(
                                      fontSize: 12,
                                      color: Colors.grey[600],
                                    ),
                                  ),
                                );
                              },
                            ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          // Simular una secuencia compleja para activar recomendaciones
          final complexSequence = ['2', '+', '3', '×', '4', '÷', '2', 'sin', '30'];
          for (int i = 0; i < complexSequence.length; i++) {
            Future.delayed(Duration(milliseconds: i * 200), () {
              if (mounted) {
                _trackAction(complexSequence[i]);
              }
            });
          }
        },
        icon: const Icon(Icons.psychology),
        label: const Text('Activar IA'),
        backgroundColor: Colors.purple,
      ),
    );
  }

  Color _getLogColor(String log) {
    if (log.contains('Recomendación')) {
      return Colors.purple;
    } else if (log.contains('ejecutada')) {
      return Colors.green;
    } else if (log.contains('rastreada')) {
      return Colors.blue;
    } else if (log.contains('Feedback')) {
      return Colors.orange;
    }
    return Colors.grey;
  }

  @override
  void dispose() {
    _mcpService.dispose();
    super.dispose();
  }
}
