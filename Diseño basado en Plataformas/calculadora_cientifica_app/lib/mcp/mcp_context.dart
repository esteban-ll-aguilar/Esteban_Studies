// Clase para almacenar el contexto del usuario
class MCPContext {
  final String? currentScreen;
  final String? currentOperation;
  final String? currentInput;
  final String? currentResult;
  final List<String>? operationHistory;
  final bool? scientificModeEnabled;
  
  MCPContext({
    this.currentScreen,
    this.currentOperation,
    this.currentInput,
    this.currentResult,
    this.operationHistory,
    this.scientificModeEnabled,
  });
  
  // Para crear una copia del contexto con algunos cambios
  MCPContext copyWith({
    String? currentScreen,
    String? currentOperation,
    String? currentInput,
    String? currentResult,
    List<String>? operationHistory,
    bool? scientificModeEnabled,
  }) {
    return MCPContext(
      currentScreen: currentScreen ?? this.currentScreen,
      currentOperation: currentOperation ?? this.currentOperation,
      currentInput: currentInput ?? this.currentInput,
      currentResult: currentResult ?? this.currentResult,
      operationHistory: operationHistory ?? this.operationHistory,
      scientificModeEnabled: scientificModeEnabled ?? this.scientificModeEnabled,
    );
  }
}
