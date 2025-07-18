import 'dart:async';
import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'mcp_action.dart';
import 'mcp_context.dart';
import 'mcp_ai_engine.dart';
import 'mcp_service.dart';

/// Servicio MCP optimizado con IA avanzada para recomendaciones inteligentes
/// Integra machine learning, análisis predictivo y personalización adaptativa
class MCPOptimizedService {
  // Singleton pattern
  static final MCPOptimizedService _instance = MCPOptimizedService._internal();
  factory MCPOptimizedService() => _instance;
  MCPOptimizedService._internal() {
    _initializeService();
  }

  // Motor de IA avanzado
  final MCPAIEngine _aiEngine = MCPAIEngine();

  // Stream controller para las acciones recomendadas
  final _actionController = StreamController<MCPAction>.broadcast();
  Stream<MCPAction> get actionStream => _actionController.stream;

  // Callback para comunicarse con la calculadora
  MCPCalculatorCallback? _calculatorCallback;

  // Contexto actual del usuario
  MCPContext _context = MCPContext();

  // Sistema de prioridades para recomendaciones
  final List<MCPAction> _priorityQueue = [];

  // Configuración del sistema
  final Map<String, dynamic> _systemConfig = {
    'enablePredictiveMode': true,
    'enableAutoActions': true,
    'confidenceThreshold': 0.7,
    'maxRecommendationsPerSession': 5,
    'learningRate': 0.01,
    'adaptationSpeed': 'medium', // slow, medium, fast
  };

  // Métricas de rendimiento en tiempo real
  final Map<String, dynamic> _performanceMetrics = {
    'averageResponseTime': 0.0,
    'accuracyRate': 0.0,
    'userSatisfactionScore': 0.0,
    'systemLoad': 0.0,
  };

  // Timer para optimización periódica
  Timer? _optimizationTimer;

  /// Inicializa el servicio optimizado
  void _initializeService() {
    // Configurar optimización periódica cada 2 minutos
    _optimizationTimer = Timer.periodic(const Duration(minutes: 2), (timer) {
      _performPeriodicOptimization();
    });

    // Configurar análisis de rendimiento cada 30 segundos
    Timer.periodic(const Duration(seconds: 30), (timer) {
      _updatePerformanceMetrics();
    });
  }

  /// Registra el callback para comunicarse con la calculadora
  void registerCalculatorCallback(MCPCalculatorCallback callback) {
    _calculatorCallback = callback;
  }

  /// Procesa una acción del usuario con análisis de IA avanzado
  void trackUserAction(String action, {Map<String, dynamic>? additionalContext}) {
    final startTime = DateTime.now();

    // Crear contexto enriquecido
    final enrichedContext = {
      'currentScreen': _context.currentScreen,
      'currentInput': _context.currentInput,
      'currentResult': _context.currentResult,
      'scientificModeEnabled': _context.scientificModeEnabled,
      'sessionDuration': _calculateSessionDuration(),
      'actionSequence': _getRecentActionSequence(),
      ...?additionalContext,
    };

    // Procesar con el motor de IA
    _aiEngine.processUserAction(action, enrichedContext);

    // Generar recomendaciones inteligentes
    _generateIntelligentRecommendations(action, enrichedContext);

    // Actualizar métricas de rendimiento
    final processingTime = DateTime.now().difference(startTime).inMilliseconds;
    _updateResponseTime(processingTime);
  }

  /// Actualiza el contexto con análisis inteligente
  void updateContext({
    String? currentScreen,
    String? currentOperation,
    String? currentInput,
    String? currentResult,
    List<String>? operationHistory,
    bool? scientificModeEnabled,
  }) {
    _context = _context.copyWith(
      currentScreen: currentScreen,
      currentOperation: currentOperation,
      currentInput: currentInput,
      currentResult: currentResult,
      operationHistory: operationHistory,
      scientificModeEnabled: scientificModeEnabled,
    );

    // Analizar cambios de contexto para recomendaciones proactivas
    _analyzeContextChanges();
  }

  /// Genera recomendaciones inteligentes basadas en IA
  Future<void> _generateIntelligentRecommendations(
    String action, 
    Map<String, dynamic> context
  ) async {
    try {
      // Obtener recomendaciones del motor de IA
      final aiRecommendations = await _aiEngine.generateRecommendations(
        currentContext: _context.currentScreen ?? 'unknown',
        maxRecommendations: _systemConfig['maxRecommendationsPerSession'],
      );

      // Convertir recomendaciones de IA a acciones MCP
      for (final aiRec in aiRecommendations) {
        if (aiRec.confidence >= _systemConfig['confidenceThreshold']) {
          final mcpAction = _convertAIRecommendationToMCPAction(aiRec);
          _addToPriorityQueue(mcpAction);
        }
      }

      // Procesar cola de prioridades
      _processPriorityQueue();

    } catch (e) {
      debugPrint('Error generando recomendaciones: $e');
    }
  }

  /// Convierte una recomendación de IA a una acción MCP
  MCPAction _convertAIRecommendationToMCPAction(AIRecommendation aiRec) {
    MCPActionType mcpType;
    
    switch (aiRec.type) {
      case AIRecommendationType.prediction:
        mcpType = MCPActionType.prediction;
        break;
      case AIRecommendationType.automation:
        mcpType = MCPActionType.automatic;
        break;
      case AIRecommendationType.interface:
      case AIRecommendationType.productivity:
      case AIRecommendationType.educational:
        mcpType = MCPActionType.suggestion;
        break;
    }

    return MCPAction(
      type: mcpType,
      message: aiRec.description,
      action: () {
        aiRec.action();
        // Registrar feedback positivo automáticamente para acciones ejecutadas
        _aiEngine.evaluateRecommendation(aiRec.id, true, true);
      },
      icon: _getIconForRecommendationType(aiRec.type),
      data: aiRec.metadata,
    );
  }

  /// Obtiene el icono apropiado para el tipo de recomendación
  IconData _getIconForRecommendationType(AIRecommendationType type) {
    switch (type) {
      case AIRecommendationType.prediction:
        return Icons.psychology;
      case AIRecommendationType.interface:
        return Icons.tune;
      case AIRecommendationType.productivity:
        return Icons.speed;
      case AIRecommendationType.educational:
        return Icons.school;
      case AIRecommendationType.automation:
        return Icons.auto_awesome;
    }
  }

  /// Añade una acción a la cola de prioridades
  void _addToPriorityQueue(MCPAction action) {
    _priorityQueue.add(action);
    
    // Ordenar por prioridad (las más recientes y de mayor confianza primero)
    _priorityQueue.sort((a, b) {
      // Priorizar por tipo de acción
      final aPriority = _getActionPriority(a.type);
      final bPriority = _getActionPriority(b.type);
      
      if (aPriority != bPriority) {
        return bPriority.compareTo(aPriority);
      }
      
      // Si tienen la misma prioridad, ordenar por timestamp
      return b.timestamp.compareTo(a.timestamp);
    });

    // Limitar el tamaño de la cola
    if (_priorityQueue.length > 10) {
      _priorityQueue.removeRange(10, _priorityQueue.length);
    }
  }

  /// Obtiene la prioridad numérica de un tipo de acción
  int _getActionPriority(MCPActionType type) {
    switch (type) {
      case MCPActionType.automatic:
        return 4;
      case MCPActionType.prediction:
        return 3;
      case MCPActionType.suggestion:
        return 2;
      case MCPActionType.notification:
        return 1;
    }
  }

  /// Procesa la cola de prioridades
  void _processPriorityQueue() {
    if (_priorityQueue.isEmpty) return;

    // Tomar la acción de mayor prioridad
    final action = _priorityQueue.removeAt(0);
    
    // Enviar al stream
    _actionController.add(action);
  }

  /// Analiza cambios de contexto para recomendaciones proactivas
  void _analyzeContextChanges() {
    // Detectar cambios significativos en el contexto
    if (_context.currentInput != null && _context.currentInput!.length > 10) {
      _suggestOptimizations();
    }

    // Detectar patrones de error
    if (_context.currentResult == "Error") {
      _suggestErrorRecovery();
    }

    // Detectar uso intensivo de funciones científicas
    if (_context.scientificModeEnabled == true) {
      _suggestAdvancedFeatures();
    }
  }

  /// Sugiere optimizaciones basadas en el contexto actual
  void _suggestOptimizations() {
    final action = MCPAction(
      type: MCPActionType.suggestion,
      message: "Expresión larga detectada. ¿Quieres que la simplifique o la divida en pasos?",
      action: () => _simplifyExpression(),
      icon: Icons.auto_fix_high,
    );
    
    _addToPriorityQueue(action);
  }

  /// Sugiere recuperación de errores
  void _suggestErrorRecovery() {
    final action = MCPAction(
      type: MCPActionType.suggestion,
      message: "Error detectado. ¿Quieres que revise la expresión y sugiera correcciones?",
      action: () => _suggestErrorCorrection(),
      icon: Icons.healing,
    );
    
    _addToPriorityQueue(action);
  }

  /// Sugiere características avanzadas
  void _suggestAdvancedFeatures() {
    final action = MCPAction(
      type: MCPActionType.suggestion,
      message: "Modo científico activo. ¿Quieres acceso a funciones avanzadas como matrices o gráficos?",
      action: () => _enableAdvancedFeatures(),
      icon: Icons.science,
    );
    
    _addToPriorityQueue(action);
  }

  /// Ejecuta acciones automáticas inteligentes
  void executeIntelligentAutoActions(BuildContext context) {
    // Análisis de contexto para acciones automáticas
    if (_shouldExecuteAutoSave()) {
      _executeAutoSave();
    }

    if (_shouldExecuteAutoCorrection()) {
      _executeAutoCorrection();
    }

    if (_shouldExecutePerformanceOptimization()) {
      _executePerformanceOptimization();
    }
  }

  /// Determina si debe ejecutar auto-guardado
  bool _shouldExecuteAutoSave() {
    return _context.operationHistory != null && 
           _context.operationHistory!.length > 10 &&
           !_context.operationHistory!.any((op) => op.contains("guardado"));
  }

  /// Determina si debe ejecutar auto-corrección
  bool _shouldExecuteAutoCorrection() {
    return _context.currentInput != null && 
           (_context.currentInput!.contains('++') || 
            _context.currentInput!.contains('--') ||
            _context.currentInput!.contains('××') ||
            _context.currentInput!.contains('÷÷'));
  }

  /// Determina si debe ejecutar optimización de rendimiento
  bool _shouldExecutePerformanceOptimization() {
    return _performanceMetrics['systemLoad'] > 0.8;
  }

  /// Ejecuta auto-guardado inteligente
  void _executeAutoSave() {
    final action = MCPAction(
      type: MCPActionType.automatic,
      message: "Guardado automático realizado. Tu historial está seguro.",
      action: () {
        if (_calculatorCallback != null) {
          _calculatorCallback!('saveHistory');
        }
      },
      icon: Icons.cloud_done,
    );
    
    _actionController.add(action);
  }

  /// Ejecuta auto-corrección inteligente
  void _executeAutoCorrection() {
    if (_context.currentInput == null) return;
    
    String correctedInput = _context.currentInput!
        .replaceAll('++', '+')
        .replaceAll('--', '-')
        .replaceAll('××', '×')
        .replaceAll('÷÷', '÷');

    final action = MCPAction(
      type: MCPActionType.automatic,
      message: "Corrección automática aplicada: operadores duplicados eliminados",
      action: () {
        if (_calculatorCallback != null) {
          _calculatorCallback!('correctInput', data: correctedInput);
        }
      },
      icon: Icons.auto_fix_high,
      data: correctedInput,
    );
    
    _actionController.add(action);
  }

  /// Ejecuta optimización de rendimiento
  void _executePerformanceOptimization() {
    _aiEngine.optimizePerformance();
    
    final action = MCPAction(
      type: MCPActionType.automatic,
      message: "Optimización de rendimiento ejecutada. El sistema funciona más eficientemente.",
      action: () {},
      icon: Icons.speed,
    );
    
    _actionController.add(action);
  }

  /// Realiza optimización periódica del sistema
  void _performPeriodicOptimization() {
    // Optimizar motor de IA
    _aiEngine.optimizePerformance();
    
    // Limpiar cola de prioridades antigua
    _cleanupPriorityQueue();
    
    // Ajustar configuración basada en métricas
    _adjustSystemConfiguration();
    
    debugPrint('Optimización periódica completada');
  }

  /// Limpia la cola de prioridades de elementos antiguos
  void _cleanupPriorityQueue() {
    final now = DateTime.now();
    _priorityQueue.removeWhere((action) => 
        now.difference(action.timestamp).inMinutes > 10);
  }

  /// Ajusta la configuración del sistema basada en métricas
  void _adjustSystemConfiguration() {
    final metrics = _aiEngine.getMetrics();
    
    // Ajustar umbral de confianza basado en la tasa de aceptación
    if (metrics.acceptedRecommendations > 0) {
      final acceptanceRate = metrics.acceptedRecommendations / metrics.recommendationEvaluations;
      
      if (acceptanceRate > 0.8) {
        _systemConfig['confidenceThreshold'] = math.max(0.5, _systemConfig['confidenceThreshold'] - 0.05);
      } else if (acceptanceRate < 0.4) {
        _systemConfig['confidenceThreshold'] = math.min(0.9, _systemConfig['confidenceThreshold'] + 0.05);
      }
    }
    
    // Ajustar número máximo de recomendaciones
    if (_performanceMetrics['userSatisfactionScore'] < 0.6) {
      _systemConfig['maxRecommendationsPerSession'] = math.max(2, _systemConfig['maxRecommendationsPerSession'] - 1);
    } else if (_performanceMetrics['userSatisfactionScore'] > 0.8) {
      _systemConfig['maxRecommendationsPerSession'] = math.min(8, _systemConfig['maxRecommendationsPerSession'] + 1);
    }
  }

  /// Actualiza métricas de rendimiento
  void _updatePerformanceMetrics() {
    final metrics = _aiEngine.getMetrics();
    
    // Calcular tasa de precisión
    if (metrics.recommendationEvaluations > 0) {
      _performanceMetrics['accuracyRate'] = 
          metrics.helpfulRecommendations / metrics.recommendationEvaluations;
    }
    
    // Calcular puntuación de satisfacción del usuario
    if (metrics.acceptedRecommendations > 0) {
      _performanceMetrics['userSatisfactionScore'] = 
          (metrics.helpfulRecommendations / metrics.acceptedRecommendations) * 
          (metrics.acceptedRecommendations / metrics.recommendationEvaluations);
    }
    
    // Simular carga del sistema (en una implementación real, esto vendría del sistema)
    _performanceMetrics['systemLoad'] = math.Random().nextDouble() * 0.5 + 0.2;
  }

  /// Actualiza el tiempo de respuesta promedio
  void _updateResponseTime(int milliseconds) {
    final currentAvg = _performanceMetrics['averageResponseTime'] as double;
    _performanceMetrics['averageResponseTime'] = (currentAvg * 0.9) + (milliseconds * 0.1);
  }

  /// Calcula la duración de la sesión actual
  int _calculateSessionDuration() {
    // Implementación simplificada
    return DateTime.now().millisecondsSinceEpoch % 3600000; // Últimos 60 minutos
  }

  /// Obtiene la secuencia de acciones recientes
  List<String> _getRecentActionSequence() {
    // Implementación simplificada - en una implementación real, 
    // esto vendría del historial de acciones
    return ['recent_action_1', 'recent_action_2', 'recent_action_3'];
  }

  // Métodos de acción para las recomendaciones

  void _simplifyExpression() {
    if (_calculatorCallback != null) {
      _calculatorCallback!('simplifyExpression');
    }
  }

  void _suggestErrorCorrection() {
    if (_calculatorCallback != null) {
      _calculatorCallback!('suggestCorrection');
    }
  }

  void _enableAdvancedFeatures() {
    if (_calculatorCallback != null) {
      _calculatorCallback!('enableAdvancedFeatures');
    }
  }

  /// Obtiene métricas del sistema
  Map<String, dynamic> getSystemMetrics() {
    return {
      'aiMetrics': _aiEngine.getMetrics(),
      'performanceMetrics': Map.from(_performanceMetrics),
      'systemConfig': Map.from(_systemConfig),
      'queueSize': _priorityQueue.length,
    };
  }

  /// Configura el sistema
  void updateSystemConfiguration(Map<String, dynamic> newConfig) {
    _systemConfig.addAll(newConfig);
  }

  /// Proporciona feedback sobre una recomendación
  void provideFeedback(String recommendationId, bool wasHelpful) {
    _aiEngine.evaluateRecommendation(recommendationId, true, wasHelpful);
    
    // Actualizar puntuación de satisfacción
    final currentScore = _performanceMetrics['userSatisfactionScore'] as double;
    final newScore = wasHelpful ? 1.0 : 0.0;
    _performanceMetrics['userSatisfactionScore'] = (currentScore * 0.9) + (newScore * 0.1);
  }

  /// Limpia recursos cuando el servicio ya no se necesita
  void dispose() {
    _actionController.close();
    _optimizationTimer?.cancel();
  }
}
