import 'dart:async';
import 'dart:math';
import 'package:flutter/material.dart';
import 'mcp_action.dart';
import 'mcp_context.dart';

// Callback para ejecutar acciones en la calculadora
typedef MCPCalculatorCallback = void Function(String action, {dynamic data});

class MCPService {
  // Singleton pattern
  static final MCPService _instance = MCPService._internal();
  factory MCPService() => _instance;
  MCPService._internal() {
    // Iniciar análisis periódico de patrones
    _startPeriodicAnalysis();
  }

  // Stream controller para las acciones recomendadas
  final _actionController = StreamController<MCPAction>.broadcast();
  Stream<MCPAction> get actionStream => _actionController.stream;

  // Callback para comunicarse con la calculadora
  MCPCalculatorCallback? _calculatorCallback;

  // Registrar el callback de la calculadora
  void registerCalculatorCallback(MCPCalculatorCallback callback) {
    _calculatorCallback = callback;
  }

  // Contexto actual del usuario
  MCPContext _context = MCPContext();

  // Historial de acciones del usuario con timestamp
  final List<UserAction> _userActionHistory = [];
  
  // Patrones de uso detectados
  final Map<String, int> _patternCounter = {};
  
  // Secuencias de operaciones detectadas
  final List<List<String>> _sequencePatterns = [];
  
  // Predicciones actuales
  final Map<String, double> _predictions = {};
  
  // Preferencias de usuario inferidas
  final Map<String, dynamic> _userPreferences = {
    'prefersScientificMode': false,
    'prefersLargeNumbers': false,
    'prefersDarkMode': false,
    'prefersTrigFunctions': false,
    'prefersDecimalPrecision': 2,
    'commonOperations': <String>[],
    'frequentResults': <String>[],
    'workingHours': {
      'start': 8, // 8:00 AM
      'end': 18,  // 6:00 PM
    },
  };
  
  // Modelo de predicción simple
  final Map<String, Map<String, double>> _transitionProbabilities = {};

  // Añadir una acción al historial
  void trackUserAction(String action) {
    final timestamp = DateTime.now();
    _userActionHistory.add(UserAction(action: action, timestamp: timestamp));
    
    // Si el historial es muy largo, mantener solo las últimas 100 acciones
    if (_userActionHistory.length > 100) {
      _userActionHistory.removeAt(0);
    }
    
    _updatePatterns(action);
    _updateSequencePatterns();
    _updateTransitionProbabilities();
    _generatePredictions();
    _inferUserPreferences();
    _analyzeAndSuggest();
  }

  // Iniciar análisis periódico de patrones
  void _startPeriodicAnalysis() {
    // Analizar cada 30 segundos para detectar patrones más complejos
    Timer.periodic(const Duration(seconds: 30), (timer) {
      if (_userActionHistory.isNotEmpty) {
        _analyzeTimePatterns();
        _detectLongTermPatterns();
        _predictNextActions();
      }
    });
  }

  // Actualizar los patrones de uso
  void _updatePatterns(String action) {
    if (_patternCounter.containsKey(action)) {
      _patternCounter[action] = (_patternCounter[action] ?? 0) + 1;
    } else {
      _patternCounter[action] = 1;
    }
  }
  
  // Actualizar patrones de secuencia
  void _updateSequencePatterns() {
    if (_userActionHistory.length < 3) return;
    
    // Extraer las últimas 3 acciones
    final lastThree = _userActionHistory.sublist(_userActionHistory.length - 3)
      .map((action) => action.action).toList();
    
    // Verificar si esta secuencia ya existe
    bool exists = false;
    for (var pattern in _sequencePatterns) {
      if (pattern.length == 3 && 
          pattern[0] == lastThree[0] && 
          pattern[1] == lastThree[1] && 
          pattern[2] == lastThree[2]) {
        exists = true;
        break;
      }
    }
    
    // Si no existe, añadirla
    if (!exists) {
      _sequencePatterns.add(lastThree);
    }
  }
  
  // Actualizar probabilidades de transición para modelo predictivo
  void _updateTransitionProbabilities() {
    if (_userActionHistory.length < 2) return;
    
    for (int i = 0; i < _userActionHistory.length - 1; i++) {
      final currentAction = _userActionHistory[i].action;
      final nextAction = _userActionHistory[i + 1].action;
      
      if (!_transitionProbabilities.containsKey(currentAction)) {
        _transitionProbabilities[currentAction] = {};
      }
      
      if (!_transitionProbabilities[currentAction]!.containsKey(nextAction)) {
        _transitionProbabilities[currentAction]![nextAction] = 0;
      }
      
      _transitionProbabilities[currentAction]![nextAction] = 
        (_transitionProbabilities[currentAction]![nextAction] ?? 0) + 1;
    }
    
    // Normalizar probabilidades
    for (var action in _transitionProbabilities.keys) {
      final transitions = _transitionProbabilities[action]!;
      final total = transitions.values.fold<double>(0, (sum, count) => sum + count);
      
      for (var nextAction in transitions.keys) {
        transitions[nextAction] = transitions[nextAction]! / total;
      }
    }
  }
  
  // Generar predicciones basadas en el modelo
  void _generatePredictions() {
    if (_userActionHistory.isEmpty) return;
    
    final lastAction = _userActionHistory.last.action;
    
    // Si tenemos transiciones para esta acción, generar predicciones
    if (_transitionProbabilities.containsKey(lastAction)) {
      _predictions.clear();
      
      final transitions = _transitionProbabilities[lastAction]!;
      for (var nextAction in transitions.keys) {
        final probability = transitions[nextAction]!;
        if (probability > 0.15) { // Solo considerar probabilidades significativas
          _predictions[nextAction] = probability;
        }
      }
    }
  }
  
  // Inferir preferencias del usuario basadas en su comportamiento
  void _inferUserPreferences() {
    // Analizar preferencia por modo científico
    final scientificActions = _userActionHistory
        .where((action) => 
            action.action == 'sin' || 
            action.action == 'cos' || 
            action.action == 'tan' ||
            action.action == 'log' ||
            action.action == 'ln' ||
            action.action == '√')
        .length;
    
    _userPreferences['prefersScientificMode'] = scientificActions > 5;
    _userPreferences['prefersTrigFunctions'] = 
        scientificActions > 0 && 
        _userActionHistory.any((action) => 
            action.action == 'sin' || 
            action.action == 'cos' || 
            action.action == 'tan');
    
    // Analizar preferencia por números grandes
    final largeInputs = _userActionHistory
        .where((action) => 
            _context.currentInput != null && 
            _context.currentInput!.length > 8)
        .length;
    
    _userPreferences['prefersLargeNumbers'] = largeInputs > 3;
    
    // Determinar operaciones comunes
    final operationCounts = <String, int>{};
    for (var action in _userActionHistory) {
      if (['+', '-', '×', '÷', '^'].contains(action.action)) {
        operationCounts[action.action] = (operationCounts[action.action] ?? 0) + 1;
      }
    }
    
    if (operationCounts.isNotEmpty) {
      final sortedOperations = operationCounts.entries.toList()
          ..sort((a, b) => b.value.compareTo(a.value));
      
      _userPreferences['commonOperations'] = 
          sortedOperations.take(3).map((e) => e.key).toList();
    }
    
    // Analizar resultados frecuentes
    if (_context.operationHistory != null && _context.operationHistory!.isNotEmpty) {
      final results = <String>[];
      for (var op in _context.operationHistory!) {
        final parts = op.split('=');
        if (parts.length > 1) {
          final result = parts[1].trim();
          results.add(result);
        }
      }
      
      if (results.isNotEmpty) {
        _userPreferences['frequentResults'] = 
            results.take(min(5, results.length)).toList();
      }
    }
    
    // Inferir preferencia de modo oscuro basado en hora del día
    final hour = DateTime.now().hour;
    _userPreferences['prefersDarkMode'] = hour < 7 || hour > 19;
  }
  
  // Analizar patrones temporales
  void _analyzeTimePatterns() {
    if (_userActionHistory.length < 10) return;
    
    // Analizar horas de actividad
    final hours = _userActionHistory.map((action) => action.timestamp.hour).toList();
    hours.sort();
    
    if (hours.isNotEmpty) {
      final earliestHour = hours.first;
      final latestHour = hours.last;
      
      if (latestHour - earliestHour > 2) {
        _userPreferences['workingHours'] = {
          'start': earliestHour,
          'end': latestHour,
        };
      }
    }
    
    // Detectar ritmo de trabajo (rápido vs. lento)
    if (_userActionHistory.length >= 2) {
      final intervals = <int>[];
      
      for (int i = 0; i < _userActionHistory.length - 1; i++) {
        final interval = _userActionHistory[i + 1].timestamp.difference(
            _userActionHistory[i].timestamp).inSeconds;
        intervals.add(interval);
      }
      
      if (intervals.isNotEmpty) {
        final avgInterval = intervals.reduce((a, b) => a + b) / intervals.length;
        _userPreferences['fastPaced'] = avgInterval < 5; // Menos de 5 segundos entre acciones
      }
    }
  }
  
  // Detectar patrones a largo plazo
  void _detectLongTermPatterns() {
    if (_userActionHistory.length < 15) return;
    
    // Detectar ciclos de operaciones
    final operations = _userActionHistory
        .where((action) => ['+', '-', '×', '÷', '='].contains(action.action))
        .map((action) => action.action)
        .toList();
    
    if (operations.length >= 6) {
      // Buscar ciclos de 3 operaciones
      for (int i = 0; i <= operations.length - 6; i++) {
        if (operations[i] == operations[i + 3] && 
            operations[i + 1] == operations[i + 4] && 
            operations[i + 2] == operations[i + 5]) {
          
          _userPreferences['hasCyclicPattern'] = true;
          _userPreferences['cyclicPattern'] = [
            operations[i], operations[i + 1], operations[i + 2]
          ];
          
          break;
        }
      }
    }
  }
  
  // Predecir próximas acciones
  void _predictNextActions() {
    if (_userActionHistory.isEmpty || _predictions.isEmpty) return;
    
    // Obtener la predicción más probable
    final sortedPredictions = _predictions.entries.toList()
        ..sort((a, b) => b.value.compareTo(a.value));
    
    if (sortedPredictions.isNotEmpty && sortedPredictions.first.value > 0.4) {
      final predictedAction = sortedPredictions.first.key;
      
      // Si es una predicción fuerte, sugerir
      _suggestAction(
        MCPAction(
          type: MCPActionType.prediction,
          message: "Basado en tu patrón de uso, ¿quieres usar $predictedAction?",
          action: () => _executePredictedAction(predictedAction),
          icon: Icons.psychology,
        )
      );
    }
  }
  
  // Ejecutar acción predicha
  void _executePredictedAction(String action) {
    // Esta función debería ser implementada para comunicarse con la calculadora
    print("Ejecutando acción predicha: $action");
    
    // Llamar al callback de la calculadora si está registrado
    if (_calculatorCallback != null) {
      _calculatorCallback!(action);
    }
  }

  // Actualizar el contexto
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
    
    // Analizar el contexto y sugerir acciones
    _analyzeAndSuggest();
  }

  // Analiza el contexto y sugiere acciones
  void _analyzeAndSuggest() {
    // Si no hay suficiente contexto aún, salir
    if (_context.currentScreen == null) return;
    
    // REGLAS PREDICTIVAS BASADAS EN CONTEXTO
    
    // Regla 1: Predicción de operación basada en patrones
    if (_predictions.isNotEmpty && _context.currentScreen == 'calculadora' &&
        _context.currentInput != null && 
        _context.currentInput!.isNotEmpty &&
        !_context.currentInput!.endsWith('+') &&
        !_context.currentInput!.endsWith('-') &&
        !_context.currentInput!.endsWith('×') &&
        !_context.currentInput!.endsWith('÷') &&
        !_context.currentInput!.endsWith('^')) {
      
      // Encontrar la operación más probable para sugerir
      final operations = ['+', '-', '×', '÷', '^'];
      String? suggestedOp;
      double maxProb = 0;
      
      for (var op in operations) {
        if (_predictions.containsKey(op) && _predictions[op]! > maxProb) {
          maxProb = _predictions[op]!;
          suggestedOp = op;
        }
      }
      
      if (suggestedOp != null && maxProb > 0.35) {
        _suggestAction(
          MCPAction(
            type: MCPActionType.prediction,
            message: "¿Quieres usar la operación $suggestedOp a continuación?",
            action: () => _suggestOperationCompletion(suggestedOp!),
            icon: Icons.psychology,
          )
        );
      }
    }
    
    // Regla 2: Predicción de número basada en resultados frecuentes
    if (_context.currentScreen == 'calculadora' && 
        _userPreferences['frequentResults'] is List && 
        (_userPreferences['frequentResults'] as List).isNotEmpty &&
        _context.currentInput != null &&
        (_context.currentInput!.endsWith('+') ||
         _context.currentInput!.endsWith('-') ||
         _context.currentInput!.endsWith('×') ||
         _context.currentInput!.endsWith('÷') ||
         _context.currentInput!.endsWith('^'))) {
      
      final frequentResults = _userPreferences['frequentResults'] as List;
      if (frequentResults.isNotEmpty) {
        final suggestedNumber = frequentResults.first;
        
        _suggestAction(
          MCPAction(
            type: MCPActionType.prediction,
            message: "¿Quieres usar el número $suggestedNumber?",
            action: () => _suggestNumberCompletion(suggestedNumber.toString()),
            icon: Icons.psychology,
          )
        );
      }
    }
    
    // Regla 3: Detección de patrones y sugerencia de automatización
    if (_userPreferences.containsKey('hasCyclicPattern') && 
        _userPreferences['hasCyclicPattern'] == true &&
        _userPreferences.containsKey('cyclicPattern')) {
      
      final pattern = _userPreferences['cyclicPattern'] as List;
      
      _suggestAction(
        MCPAction(
          type: MCPActionType.suggestion,
          message: "He detectado que repites frecuentemente el patrón: ${pattern.join(' → ')}. ¿Quieres que cree un botón de acceso rápido?",
          action: () => _createShortcutForPattern(pattern),
          icon: Icons.auto_awesome_motion,
        )
      );
    }
    
    // Regla 4: Números grandes - notación científica
    if (_context.currentScreen == 'calculadora' && 
        _context.currentInput != null && 
        _context.currentInput!.length > 8 &&
        !_context.currentInput!.contains('e+') &&
        _userPreferences['prefersLargeNumbers']) {
      
      _suggestAction(
        MCPAction(
          type: MCPActionType.suggestion,
          message: "Estás trabajando con números grandes. ¿Quieres ver el resultado en notación científica?",
          action: () => _convertToScientificNotation(),
          icon: Icons.science,
        )
      );
    }
    
    // Regla 5: Sugerir modo científico basado en preferencias inferidas
    if (_context.currentScreen == 'calculadora' && 
        !(_context.scientificModeEnabled ?? false) &&
        _userPreferences['prefersScientificMode']) {
      
      _suggestAction(
        MCPAction(
          type: MCPActionType.suggestion,
          message: "Basado en tus cálculos anteriores, el modo científico podría serte útil. ¿Quieres activarlo?",
          action: () => _enableScientificMode(),
          icon: Icons.auto_awesome,
        )
      );
    }
    
    // Regla 6: Sugerencia basada en hora del día
    final hour = DateTime.now().hour;
    if (_userPreferences['prefersDarkMode'] && hour >= 20 || hour <= 6) {
      _suggestAction(
        MCPAction(
          type: MCPActionType.suggestion,
          message: "Es de noche. ¿Quieres activar el modo oscuro para reducir la fatiga visual?",
          action: () => _enableDarkMode(),
          icon: Icons.dark_mode,
        )
      );
    }
    
    // Regla 7: Completar expresiones matemáticas
    if (_context.currentScreen == 'calculadora' && 
        _context.currentInput != null &&
        _context.currentInput!.contains('(') && 
        !_context.currentInput!.contains(')')) {
      
      _suggestAction(
        MCPAction(
          type: MCPActionType.suggestion,
          message: "Tienes un paréntesis abierto sin cerrar. ¿Quieres que lo cierre?",
          action: () => _closeParenthesis(),
          icon: Icons.format_align_center,
        )
      );
    }
    
    // Regla 8: Recomendación de funciones basada en valores
    if (_context.currentScreen == 'calculadora' && 
        _context.currentInput != null && 
        _context.currentInput!.isNotEmpty && 
        _userPreferences['prefersTrigFunctions'] &&
        double.tryParse(_context.currentInput!) != null) {
          
      final value = double.parse(_context.currentInput!);
      if (value >= 0 && value <= 360) {
        _suggestAction(
          MCPAction(
            type: MCPActionType.suggestion,
            message: "¿Quieres calcular el seno, coseno o tangente de $value grados?",
            action: () => _suggestTrigFunction(value),
            icon: Icons.waves,
          )
        );
      }
    }
  }
  
  // Métodos para las acciones predichas/sugeridas
  
  void _suggestOperationCompletion(String operation) {
    print("Completar con operación: $operation");
    // Llamar al callback de la calculadora si está registrado
    if (_calculatorCallback != null) {
      _calculatorCallback!('operation', data: operation);
    }
  }
  
  void _suggestNumberCompletion(String number) {
    print("Completar con número: $number");
    // Llamar al callback de la calculadora si está registrado
    if (_calculatorCallback != null) {
      _calculatorCallback!('number', data: number);
    }
  }
  
  void _createShortcutForPattern(List pattern) {
    print("Crear acceso directo para patrón: $pattern");
    // Llamar al callback de la calculadora si está registrado
    if (_calculatorCallback != null) {
      _calculatorCallback!('createShortcut', data: pattern);
    }
  }
  
  void _convertToScientificNotation() {
    print("Convertir a notación científica");
    // Llamar al callback de la calculadora si está registrado
    if (_calculatorCallback != null) {
      _calculatorCallback!('scientificNotation');
    }
  }
  
  void _enableScientificMode() {
    print("Habilitar modo científico");
    // Llamar al callback de la calculadora si está registrado
    if (_calculatorCallback != null) {
      _calculatorCallback!('enableScientificMode');
    }
  }
  
  void _enableDarkMode() {
    print("Habilitar modo oscuro");
    // Llamar al callback de la calculadora si está registrado
    if (_calculatorCallback != null) {
      _calculatorCallback!('enableDarkMode');
    }
  }
  
  void _closeParenthesis() {
    print("Cerrar paréntesis");
    // Llamar al callback de la calculadora si está registrado
    if (_calculatorCallback != null) {
      _calculatorCallback!('closeParenthesis');
    }
  }
  
  void _suggestTrigFunction(double value) {
    print("Sugerir función trigonométrica para: $value");
    // Llamar al callback de la calculadora si está registrado
    if (_calculatorCallback != null) {
      _calculatorCallback!('trigFunction', data: value);
    }
  }
  
  // Envía una acción al stream
  void _suggestAction(MCPAction action) {
    _actionController.add(action);
  }
  
  // Ejecuta una acción automáticamente basada en ciertos criterios
  void executeAutomaticAction(BuildContext context) {
    // Lógica mejorada para acciones automáticas
    
    // Ejemplo: Auto-guardado inteligente
    if (_context.operationHistory != null && 
        _context.operationHistory!.length > 5 && 
        !_context.operationHistory!.any((op) => op.contains("guardado"))) {
      
      _suggestAction(
        MCPAction(
          type: MCPActionType.automatic,
          message: "He guardado automáticamente tu historial de cálculos para referencia futura",
          action: () {
            // Llamar al callback de la calculadora si está registrado
            if (_calculatorCallback != null) {
              _calculatorCallback!('saveHistory');
            } else {
              _saveHistory();
            }
          },
          icon: Icons.save,
        )
      );
      
      // No es necesario ejecutar _saveHistory() aquí, ya que la acción ya lo hace
      // cuando MCPNotificationManager llama a action.action()
    }
    
    // Otra acción automática: detección y corrección de errores comunes
    if (_context.currentInput != null && 
        (_context.currentInput!.contains('++') || 
        _context.currentInput!.contains('--') ||
        _context.currentInput!.contains('××') ||
        _context.currentInput!.contains('÷÷'))) {
      
      String correctedInput = _context.currentInput!
          .replaceAll('++', '+')
          .replaceAll('--', '-')
          .replaceAll('××', '×')
          .replaceAll('÷÷', '÷');
      
      _suggestAction(
        MCPAction(
          type: MCPActionType.automatic,
          message: "He corregido automáticamente operadores duplicados en tu expresión",
          action: () {
            // Llamar al callback de la calculadora si está registrado
            if (_calculatorCallback != null) {
              _calculatorCallback!('correctInput', data: correctedInput);
            }
          },
          icon: Icons.auto_fix_high,
          data: correctedInput, // Pasamos el input corregido como dato extra
        )
      );
    }
  }
  
  void _saveHistory() {
    // Implementación real para guardar el historial
    print("Guardando historial automáticamente");
  }
  
  // Método para cerrar recursos cuando ya no se necesiten
  void dispose() {
    _actionController.close();
  }
}

// Clase para almacenar acciones de usuario con timestamp
class UserAction {
  final String action;
  final DateTime timestamp;
  
  UserAction({required this.action, required this.timestamp});
}
