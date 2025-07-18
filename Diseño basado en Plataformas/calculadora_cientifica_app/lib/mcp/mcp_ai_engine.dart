import 'dart:math' as math;
import 'dart:convert';
import 'package:flutter/foundation.dart';

/// Motor de IA avanzado para el sistema MCP
/// Implementa algoritmos de machine learning para recomendaciones optimizadas
class MCPAIEngine {
  // Singleton pattern
  static final MCPAIEngine _instance = MCPAIEngine._internal();
  factory MCPAIEngine() => _instance;
  MCPAIEngine._internal() {
    _initializeNeuralNetwork();
  }

  // Red neuronal simple para predicciones
  late NeuralNetwork _neuralNetwork;
  
  // Matriz de características del usuario
  final Map<String, double> _userFeatures = {
    'operationFrequency': 0.0,
    'scientificUsage': 0.0,
    'complexityPreference': 0.0,
    'speedOfUse': 0.0,
    'errorRate': 0.0,
    'sessionLength': 0.0,
    'timeOfDayPattern': 0.0,
    'sequentialPattern': 0.0,
  };
  
  // Historial de acciones para análisis temporal
  final List<ActionVector> _actionHistory = [];
  
  // Modelo de clustering para segmentación de usuarios
  final List<UserCluster> _userClusters = [];
  
  // Cache de recomendaciones para optimización
  final Map<String, List<AIRecommendation>> _recommendationCache = {};
  
  // Métricas de rendimiento del modelo
  final AIMetrics _metrics = AIMetrics();

  /// Inicializa la red neuronal con arquitectura optimizada
  void _initializeNeuralNetwork() {
    _neuralNetwork = NeuralNetwork(
      inputSize: 8, // Número de características de entrada
      hiddenLayers: [16, 12, 8], // Capas ocultas
      outputSize: 5, // Tipos de recomendaciones
      learningRate: 0.01,
    );
    
    // Inicializar clusters de usuarios
    _initializeUserClusters();
  }
  
  /// Inicializa clusters de usuarios basados en patrones comunes
  void _initializeUserClusters() {
    _userClusters.addAll([
      UserCluster(
        id: 'basic_user',
        name: 'Usuario Básico',
        characteristics: {
          'operationFrequency': 0.3,
          'scientificUsage': 0.1,
          'complexityPreference': 0.2,
        },
      ),
      UserCluster(
        id: 'scientific_user',
        name: 'Usuario Científico',
        characteristics: {
          'operationFrequency': 0.7,
          'scientificUsage': 0.9,
          'complexityPreference': 0.8,
        },
      ),
      UserCluster(
        id: 'professional_user',
        name: 'Usuario Profesional',
        characteristics: {
          'operationFrequency': 0.9,
          'scientificUsage': 0.6,
          'complexityPreference': 0.7,
          'speedOfUse': 0.8,
        },
      ),
      UserCluster(
        id: 'student_user',
        name: 'Estudiante',
        characteristics: {
          'operationFrequency': 0.5,
          'scientificUsage': 0.4,
          'complexityPreference': 0.3,
          'sessionLength': 0.6,
        },
      ),
    ]);
  }

  /// Procesa una nueva acción del usuario y actualiza el modelo
  void processUserAction(String action, Map<String, dynamic> context) {
    final actionVector = ActionVector(
      action: action,
      timestamp: DateTime.now(),
      context: context,
    );
    
    _actionHistory.add(actionVector);
    
    // Mantener solo las últimas 1000 acciones para optimización
    if (_actionHistory.length > 1000) {
      _actionHistory.removeAt(0);
    }
    
    // Actualizar características del usuario
    _updateUserFeatures(actionVector);
    
    // Entrenar la red neuronal con nuevos datos
    _trainNeuralNetwork();
    
    // Actualizar métricas
    _metrics.totalActions++;
    _metrics.lastActionTime = DateTime.now();
  }

  /// Actualiza las características del usuario basadas en la nueva acción
  void _updateUserFeatures(ActionVector action) {
    // Frecuencia de operaciones
    if (_isOperation(action.action)) {
      _userFeatures['operationFrequency'] = 
          (_userFeatures['operationFrequency']! * 0.9) + 0.1;
    }
    
    // Uso de funciones científicas
    if (_isScientificFunction(action.action)) {
      _userFeatures['scientificUsage'] = 
          (_userFeatures['scientificUsage']! * 0.9) + 0.1;
    }
    
    // Preferencia de complejidad
    final complexity = _calculateActionComplexity(action.action);
    _userFeatures['complexityPreference'] = 
        (_userFeatures['complexityPreference']! * 0.95) + (complexity * 0.05);
    
    // Velocidad de uso
    if (_actionHistory.length > 1) {
      final timeDiff = action.timestamp.difference(
          _actionHistory[_actionHistory.length - 2].timestamp).inSeconds;
      final speed = math.max(0, 1 - (timeDiff / 10)); // Normalizado
      _userFeatures['speedOfUse'] = 
          (_userFeatures['speedOfUse']! * 0.9) + (speed * 0.1);
    }
    
    // Patrón temporal (hora del día)
    final hour = action.timestamp.hour;
    final timePattern = _calculateTimePattern(hour);
    _userFeatures['timeOfDayPattern'] = 
        (_userFeatures['timeOfDayPattern']! * 0.95) + (timePattern * 0.05);
    
    // Patrón secuencial
    final sequentialScore = _calculateSequentialPattern();
    _userFeatures['sequentialPattern'] = sequentialScore;
  }

  /// Entrena la red neuronal con los datos actuales
  void _trainNeuralNetwork() {
    if (_actionHistory.length < 10) return; // Necesitamos datos suficientes
    
    // Preparar datos de entrenamiento
    final trainingData = _prepareTrainingData();
    
    // Entrenar la red neuronal
    for (final sample in trainingData) {
      _neuralNetwork.train(sample.input, sample.expectedOutput);
    }
    
    _metrics.trainingIterations++;
  }

  /// Prepara los datos de entrenamiento para la red neuronal
  List<TrainingSample> _prepareTrainingData() {
    final samples = <TrainingSample>[];
    
    // Crear muestras de entrenamiento basadas en secuencias de acciones
    for (int i = 5; i < _actionHistory.length; i++) {
      final input = List<double>.from(_userFeatures.values);
      
      // Agregar contexto de las últimas 5 acciones
      for (int j = i - 5; j < i; j++) {
        input.add(_encodeAction(_actionHistory[j].action));
      }
      
      // La salida esperada es el tipo de recomendación más apropiada
      final expectedOutput = _calculateExpectedRecommendation(_actionHistory[i]);
      
      samples.add(TrainingSample(input: input, expectedOutput: expectedOutput));
    }
    
    return samples.take(50).toList(); // Limitar para rendimiento
  }

  /// Genera recomendaciones de IA optimizadas
  Future<List<AIRecommendation>> generateRecommendations({
    required String currentContext,
    int maxRecommendations = 3,
  }) async {
    // Verificar cache primero
    final cacheKey = _generateCacheKey(currentContext);
    if (_recommendationCache.containsKey(cacheKey)) {
      final cached = _recommendationCache[cacheKey]!;
      if (cached.isNotEmpty && 
          DateTime.now().difference(cached.first.timestamp).inMinutes < 5) {
        return cached;
      }
    }
    
    final recommendations = <AIRecommendation>[];
    
    // 1. Recomendaciones basadas en red neuronal
    final neuralRecommendations = await _generateNeuralRecommendations();
    recommendations.addAll(neuralRecommendations);
    
    // 2. Recomendaciones basadas en clustering
    final clusterRecommendations = _generateClusterRecommendations();
    recommendations.addAll(clusterRecommendations);
    
    // 3. Recomendaciones basadas en patrones temporales
    final temporalRecommendations = _generateTemporalRecommendations();
    recommendations.addAll(temporalRecommendations);
    
    // 4. Recomendaciones basadas en análisis de secuencias
    final sequenceRecommendations = _generateSequenceRecommendations();
    recommendations.addAll(sequenceRecommendations);
    
    // Ordenar por confianza y tomar las mejores
    recommendations.sort((a, b) => b.confidence.compareTo(a.confidence));
    final topRecommendations = recommendations.take(maxRecommendations).toList();
    
    // Guardar en cache
    _recommendationCache[cacheKey] = topRecommendations;
    
    // Actualizar métricas
    _metrics.recommendationsGenerated += topRecommendations.length;
    
    return topRecommendations;
  }

  /// Genera recomendaciones usando la red neuronal
  Future<List<AIRecommendation>> _generateNeuralRecommendations() async {
    final input = List<double>.from(_userFeatures.values);
    
    // Agregar contexto de las últimas acciones
    final recentActions = _actionHistory.take(5).toList();
    for (final action in recentActions) {
      input.add(_encodeAction(action.action));
    }
    
    // Obtener predicción de la red neuronal
    final prediction = _neuralNetwork.predict(input);
    
    final recommendations = <AIRecommendation>[];
    
    // Interpretar la salida de la red neuronal
    for (int i = 0; i < prediction.length; i++) {
      if (prediction[i] > 0.6) { // Umbral de confianza
        final recommendation = _createRecommendationFromPrediction(i, prediction[i]);
        if (recommendation != null) {
          recommendations.add(recommendation);
        }
      }
    }
    
    return recommendations;
  }

  /// Genera recomendaciones basadas en clustering de usuarios
  List<AIRecommendation> _generateClusterRecommendations() {
    final userCluster = _findUserCluster();
    final recommendations = <AIRecommendation>[];
    
    if (userCluster != null) {
      // Generar recomendaciones específicas para el cluster
      switch (userCluster.id) {
        case 'scientific_user':
          recommendations.add(AIRecommendation(
            id: 'scientific_mode',
            title: 'Activar Modo Científico Avanzado',
            description: 'Basado en tu perfil científico, te recomiendo activar funciones avanzadas',
            type: AIRecommendationType.interface,
            confidence: 0.85,
            action: () => _activateScientificMode(),
            priority: AIRecommendationPriority.high,
          ));
          break;
          
        case 'professional_user':
          recommendations.add(AIRecommendation(
            id: 'shortcuts',
            title: 'Crear Atajos Personalizados',
            description: 'Como usuario profesional, los atajos pueden acelerar tu trabajo',
            type: AIRecommendationType.productivity,
            confidence: 0.80,
            action: () => _createCustomShortcuts(),
            priority: AIRecommendationPriority.medium,
          ));
          break;
          
        case 'student_user':
          recommendations.add(AIRecommendation(
            id: 'learning_mode',
            title: 'Activar Modo Aprendizaje',
            description: 'Te ayudo a entender mejor los cálculos con explicaciones paso a paso',
            type: AIRecommendationType.educational,
            confidence: 0.75,
            action: () => _activateLearningMode(),
            priority: AIRecommendationPriority.medium,
          ));
          break;
      }
    }
    
    return recommendations;
  }

  /// Genera recomendaciones basadas en patrones temporales
  List<AIRecommendation> _generateTemporalRecommendations() {
    final recommendations = <AIRecommendation>[];
    final hour = DateTime.now().hour;
    
    // Recomendaciones basadas en la hora del día
    if (hour >= 22 || hour <= 6) {
      recommendations.add(AIRecommendation(
        id: 'dark_mode',
        title: 'Activar Modo Nocturno',
        description: 'Es tarde, el modo oscuro puede reducir la fatiga visual',
        type: AIRecommendationType.interface,
        confidence: 0.70,
        action: () => _activateDarkMode(),
        priority: AIRecommendationPriority.low,
      ));
    }
    
    // Recomendaciones basadas en patrones de uso por hora
    final hourlyPattern = _analyzeHourlyPattern();
    if (hourlyPattern.isNotEmpty) {
      recommendations.add(AIRecommendation(
        id: 'optimize_layout',
        title: 'Optimizar Diseño',
        description: 'He notado que usas más la calculadora a esta hora, ¿optimizo el diseño?',
        type: AIRecommendationType.interface,
        confidence: 0.65,
        action: () => _optimizeLayout(),
        priority: AIRecommendationPriority.low,
      ));
    }
    
    return recommendations;
  }

  /// Genera recomendaciones basadas en análisis de secuencias
  List<AIRecommendation> _generateSequenceRecommendations() {
    final recommendations = <AIRecommendation>[];
    
    // Analizar secuencias frecuentes
    final frequentSequences = _findFrequentSequences();
    
    for (final sequence in frequentSequences) {
      if (sequence.frequency > 3 && sequence.actions.length >= 3) {
        recommendations.add(AIRecommendation(
          id: 'sequence_${sequence.id}',
          title: 'Automatizar Secuencia Frecuente',
          description: 'He detectado que repites la secuencia: ${sequence.actions.join(" → ")}',
          type: AIRecommendationType.automation,
          confidence: 0.75 + (sequence.frequency * 0.05),
          action: () => _createSequenceShortcut(sequence),
          priority: AIRecommendationPriority.medium,
          metadata: {'sequence': sequence.actions},
        ));
      }
    }
    
    return recommendations;
  }

  /// Evalúa la efectividad de una recomendación
  void evaluateRecommendation(String recommendationId, bool wasAccepted, bool wasHelpful) {
    _metrics.recommendationEvaluations++;
    
    if (wasAccepted) {
      _metrics.acceptedRecommendations++;
    }
    
    if (wasHelpful) {
      _metrics.helpfulRecommendations++;
    }
    
    // Ajustar el modelo basado en el feedback
    _adjustModelBasedOnFeedback(recommendationId, wasAccepted, wasHelpful);
  }

  /// Obtiene métricas de rendimiento del sistema de IA
  AIMetrics getMetrics() => _metrics;

  /// Optimiza el rendimiento del motor de IA
  void optimizePerformance() {
    // Limpiar cache antiguo
    _cleanupCache();
    
    // Optimizar red neuronal
    _optimizeNeuralNetwork();
    
    // Actualizar clusters de usuarios
    _updateUserClusters();
    
    _metrics.optimizationRuns++;
  }

  // Métodos auxiliares privados

  bool _isOperation(String action) {
    return ['+', '-', '×', '÷', '^', '='].contains(action);
  }

  bool _isScientificFunction(String action) {
    return ['sin', 'cos', 'tan', 'log', 'ln', '√', 'π', 'e'].contains(action);
  }

  double _calculateActionComplexity(String action) {
    if (_isScientificFunction(action)) return 0.8;
    if (_isOperation(action)) return 0.4;
    if (RegExp(r'\d').hasMatch(action)) return 0.2;
    return 0.1;
  }

  double _calculateTimePattern(int hour) {
    // Normalizar la hora a un patrón circular
    return (math.sin(2 * math.pi * hour / 24) + 1) / 2;
  }

  double _calculateSequentialPattern() {
    if (_actionHistory.length < 3) return 0.0;
    
    final recent = _actionHistory.skip(_actionHistory.length - 3).take(3).map((a) => a.action).toList();
    int patternCount = 0;
    
    // Buscar este patrón en el historial
    for (int i = 0; i <= _actionHistory.length - 3; i++) {
      final sequence = _actionHistory.skip(i).take(3).map((a) => a.action).toList();
      if (listEquals(sequence, recent)) {
        patternCount++;
      }
    }
    
    return math.min(1.0, patternCount / 10.0);
  }

  double _encodeAction(String action) {
    // Codificación simple de acciones a números
    final actionMap = {
      '+': 0.1, '-': 0.2, '×': 0.3, '÷': 0.4, '=': 0.5,
      'sin': 0.6, 'cos': 0.7, 'tan': 0.8, 'log': 0.9, 'ln': 1.0,
    };
    
    return actionMap[action] ?? 0.05;
  }

  List<double> _calculateExpectedRecommendation(ActionVector action) {
    // Crear vector de salida esperado basado en la acción
    final output = List<double>.filled(5, 0.0);
    
    if (_isScientificFunction(action.action)) {
      output[0] = 1.0; // Recomendación científica
    } else if (_isOperation(action.action)) {
      output[1] = 1.0; // Recomendación de operación
    } else {
      output[2] = 1.0; // Recomendación general
    }
    
    return output;
  }

  String _generateCacheKey(String context) {
    final features = _userFeatures.values.map((v) => v.toStringAsFixed(2)).join(',');
    return '$context:$features';
  }

  UserCluster? _findUserCluster() {
    double bestMatch = 0.0;
    UserCluster? bestCluster;
    
    for (final cluster in _userClusters) {
      final similarity = _calculateClusterSimilarity(cluster);
      if (similarity > bestMatch) {
        bestMatch = similarity;
        bestCluster = cluster;
      }
    }
    
    return bestMatch > 0.6 ? bestCluster : null;
  }

  double _calculateClusterSimilarity(UserCluster cluster) {
    double similarity = 0.0;
    int commonFeatures = 0;
    
    for (final entry in cluster.characteristics.entries) {
      if (_userFeatures.containsKey(entry.key)) {
        final userValue = _userFeatures[entry.key]!;
        final clusterValue = entry.value;
        similarity += 1.0 - (userValue - clusterValue).abs();
        commonFeatures++;
      }
    }
    
    return commonFeatures > 0 ? similarity / commonFeatures : 0.0;
  }

  AIRecommendation? _createRecommendationFromPrediction(int index, double confidence) {
    switch (index) {
      case 0:
        return AIRecommendation(
          id: 'neural_scientific',
          title: 'Función Científica Recomendada',
          description: 'La IA predice que podrías necesitar una función científica',
          type: AIRecommendationType.prediction,
          confidence: confidence,
          action: () => _suggestScientificFunction(),
          priority: AIRecommendationPriority.medium,
        );
      case 1:
        return AIRecommendation(
          id: 'neural_operation',
          title: 'Operación Sugerida',
          description: 'Basado en tu patrón, esta operación podría ser útil',
          type: AIRecommendationType.prediction,
          confidence: confidence,
          action: () => _suggestOperation(),
          priority: AIRecommendationPriority.medium,
        );
      default:
        return null;
    }
  }

  Map<String, dynamic> _analyzeHourlyPattern() {
    final hourCounts = <int, int>{};
    
    for (final action in _actionHistory) {
      final hour = action.timestamp.hour;
      hourCounts[hour] = (hourCounts[hour] ?? 0) + 1;
    }
    
    return hourCounts.isNotEmpty ? {'pattern': hourCounts} : {};
  }

  List<ActionSequence> _findFrequentSequences() {
    final sequences = <String, ActionSequence>{};
    
    // Buscar secuencias de 3 acciones
    for (int i = 0; i <= _actionHistory.length - 3; i++) {
      final sequence = _actionHistory.skip(i).take(3).map((a) => a.action).toList();
      final key = sequence.join('|');
      
      if (sequences.containsKey(key)) {
        sequences[key]!.frequency++;
      } else {
        sequences[key] = ActionSequence(
          id: key,
          actions: sequence,
          frequency: 1,
        );
      }
    }
    
    return sequences.values.where((s) => s.frequency > 1).toList();
  }

  void _adjustModelBasedOnFeedback(String recommendationId, bool wasAccepted, bool wasHelpful) {
    // Ajustar pesos de la red neuronal basado en el feedback
    if (wasAccepted && wasHelpful) {
      _neuralNetwork.reinforceLastPrediction(0.1);
    } else if (!wasAccepted || !wasHelpful) {
      _neuralNetwork.reinforceLastPrediction(-0.05);
    }
  }

  void _cleanupCache() {
    final now = DateTime.now();
    _recommendationCache.removeWhere((key, recommendations) {
      return recommendations.isEmpty || 
             now.difference(recommendations.first.timestamp).inHours > 1;
    });
  }

  void _optimizeNeuralNetwork() {
    // Implementar optimización de la red neuronal
    _neuralNetwork.optimize();
  }

  void _updateUserClusters() {
    // Actualizar clusters basado en nuevos datos
    // Implementación simplificada
  }

  // Métodos de acción para recomendaciones
  void _activateScientificMode() => debugPrint('Activando modo científico avanzado');
  void _createCustomShortcuts() => debugPrint('Creando atajos personalizados');
  void _activateLearningMode() => debugPrint('Activando modo aprendizaje');
  void _activateDarkMode() => debugPrint('Activando modo oscuro');
  void _optimizeLayout() => debugPrint('Optimizando diseño');
  void _createSequenceShortcut(ActionSequence sequence) => debugPrint('Creando atajo para: ${sequence.actions}');
  void _suggestScientificFunction() => debugPrint('Sugiriendo función científica');
  void _suggestOperation() => debugPrint('Sugiriendo operación');
}

// Clases de soporte

class NeuralNetwork {
  final int inputSize;
  final List<int> hiddenLayers;
  final int outputSize;
  final double learningRate;
  
  late List<List<List<double>>> _weights;
  late List<List<double>> _biases;
  List<List<double>>? _lastActivations;

  NeuralNetwork({
    required this.inputSize,
    required this.hiddenLayers,
    required this.outputSize,
    required this.learningRate,
  }) {
    _initializeWeights();
  }

  void _initializeWeights() {
    _weights = [];
    _biases = [];
    
    final layers = [inputSize, ...hiddenLayers, outputSize];
    
    for (int i = 0; i < layers.length - 1; i++) {
      final layerWeights = <List<double>>[];
      final layerBiases = <double>[];
      
      for (int j = 0; j < layers[i + 1]; j++) {
        final neuronWeights = <double>[];
        for (int k = 0; k < layers[i]; k++) {
          neuronWeights.add((math.Random().nextDouble() - 0.5) * 2);
        }
        layerWeights.add(neuronWeights);
        layerBiases.add((math.Random().nextDouble() - 0.5) * 2);
      }
      
      _weights.add(layerWeights);
      _biases.add(layerBiases);
    }
  }

  List<double> predict(List<double> input) {
    List<double> activation = List.from(input);
    _lastActivations = [activation];
    
    for (int layer = 0; layer < _weights.length; layer++) {
      final newActivation = <double>[];
      
      for (int neuron = 0; neuron < _weights[layer].length; neuron++) {
        double sum = _biases[layer][neuron];
        
        for (int i = 0; i < activation.length; i++) {
          sum += activation[i] * _weights[layer][neuron][i];
        }
        
        newActivation.add(_sigmoid(sum));
      }
      
      activation = newActivation;
      _lastActivations!.add(activation);
    }
    
    return activation;
  }

  void train(List<double> input, List<double> expectedOutput) {
    final output = predict(input);
    
    // Backpropagation simplificado
    final errors = <double>[];
    for (int i = 0; i < output.length; i++) {
      errors.add(expectedOutput[i] - output[i]);
    }
    
    // Actualizar pesos (implementación simplificada)
    for (int layer = _weights.length - 1; layer >= 0; layer--) {
      for (int neuron = 0; neuron < _weights[layer].length; neuron++) {
        for (int weight = 0; weight < _weights[layer][neuron].length; weight++) {
          final delta = learningRate * errors[neuron] * 
                       _lastActivations![layer][weight];
          _weights[layer][neuron][weight] += delta;
        }
        _biases[layer][neuron] += learningRate * errors[neuron];
      }
    }
  }

  void reinforceLastPrediction(double reinforcement) {
    // Reforzar o debilitar la última predicción
    for (int layer = 0; layer < _weights.length; layer++) {
      for (int neuron = 0; neuron < _weights[layer].length; neuron++) {
        for (int weight = 0; weight < _weights[layer][neuron].length; weight++) {
          _weights[layer][neuron][weight] *= (1 + reinforcement);
        }
      }
    }
  }

  void optimize() {
    // Implementar optimización de la red
    // Por ejemplo, regularización L2, dropout, etc.
  }

  double _sigmoid(double x) {
    return 1 / (1 + math.exp(-x));
  }
}

class ActionVector {
  final String action;
  final DateTime timestamp;
  final Map<String, dynamic> context;

  ActionVector({
    required this.action,
    required this.timestamp,
    required this.context,
  });
}

class UserCluster {
  final String id;
  final String name;
  final Map<String, double> characteristics;

  UserCluster({
    required this.id,
    required this.name,
    required this.characteristics,
  });
}

class TrainingSample {
  final List<double> input;
  final List<double> expectedOutput;

  TrainingSample({
    required this.input,
    required this.expectedOutput,
  });
}

enum AIRecommendationType {
  prediction,
  interface,
  productivity,
  educational,
  automation,
}

enum AIRecommendationPriority {
  low,
  medium,
  high,
  critical,
}

class AIRecommendation {
  final String id;
  final String title;
  final String description;
  final AIRecommendationType type;
  final double confidence;
  final Function() action;
  final AIRecommendationPriority priority;
  final DateTime timestamp;
  final Map<String, dynamic>? metadata;

  AIRecommendation({
    required this.id,
    required this.title,
    required this.description,
    required this.type,
    required this.confidence,
    required this.action,
    required this.priority,
    DateTime? timestamp,
    this.metadata,
  }) : timestamp = timestamp ?? DateTime.now();
}

class ActionSequence {
  final String id;
  final List<String> actions;
  int frequency;

  ActionSequence({
    required this.id,
    required this.actions,
    required this.frequency,
  });
}

class AIMetrics {
  int totalActions = 0;
  int trainingIterations = 0;
  int recommendationsGenerated = 0;
  int recommendationEvaluations = 0;
  int acceptedRecommendations = 0;
  int helpfulRecommendations = 0;
  int optimizationRuns = 0;
  DateTime? lastActionTime;
}
