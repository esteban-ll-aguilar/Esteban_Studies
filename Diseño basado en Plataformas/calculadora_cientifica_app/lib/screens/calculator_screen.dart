import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../widgets/calculator_keyboard.dart';
import '../widgets/calculator_display.dart';
import '../mcp/mcp.dart'; // Importamos el MCP
import 'dart:math' as math;

class CalculadoraCientifica extends StatefulWidget {
  const CalculadoraCientifica({super.key});

  @override
  State<CalculadoraCientifica> createState() => _CalculadoraCientificaState();
}

class _CalculadoraCientificaState extends State<CalculadoraCientifica> {
  String _input = "0";
  String _output = "";
  bool _showScientificButtons = false;
  final List<String> _history = [];
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();
  
  @override
  void initState() {
    super.initState();
    // Inicializar el contexto del MCP
    _updateMCPContext();
    
    // Registrar el callback para las acciones del MCP
    MCPService().registerCalculatorCallback(_handleMCPAction);
  }
  
  void _onButtonPressed(String buttonText) {
    setState(() {
      // Procesa la entrada según el botón presionado
      if (buttonText == "C") {
        _clearAll();
      } else if (buttonText == "⌫") {
        _backspace();
      } else if (buttonText == "=") {
        _calculate();
      } else if (buttonText == "sin" || buttonText == "cos" || buttonText == "tan" ||
                buttonText == "log" || buttonText == "ln" || buttonText == "√") {
        _addFunction(buttonText);
      } else if (buttonText == "π") {
        _addConstant(math.pi.toString());
      } else if (buttonText == "e") {
        _addConstant(math.e.toString());
      } else if (buttonText == "x²") {
        _addPower(2);
      } else if (buttonText == "x³") {
        _addPower(3);
      } else if (buttonText == "xʸ") {
        _addOperator("^");
      } else {
        _addToInput(buttonText);
      }
      
      // Registrar acción en el MCP
      MCPService().trackUserAction(buttonText);
      // Actualizar contexto MCP
      _updateMCPContext();
    });
  }
  
  void _updateMCPContext() {
    MCPService().updateContext(
      currentScreen: 'calculadora',
      currentInput: _input,
      currentResult: _output,
      operationHistory: _history,
      scientificModeEnabled: _showScientificButtons,
    );
  }

  void _clearAll() {
    _input = "0";
    _output = "";
  }

  void _backspace() {
    if (_input.length > 1) {
      _input = _input.substring(0, _input.length - 1);
    } else {
      _input = "0";
    }
  }

  void _addToInput(String value) {
    if (_input == "0" && value != ".") {
      _input = value;
    } else {
      _input += value;
    }
  }

  void _addFunction(String func) {
    _input += "$func(";
  }

  void _addConstant(String value) {
    if (_input == "0") {
      _input = value;
    } else {
      _input += value;
    }
  }

  void _addPower(int power) {
    _input += "^$power";
  }

  void _addOperator(String operator) {
    setState(() {
      _input += operator;
    });
  }

  // Manejador para las acciones del MCP
  void _handleMCPAction(String action, {dynamic data}) {
    setState(() {
      switch (action) {
        case 'operation':
          if (data is String) {
            _addOperator(data);
          }
          break;
        case 'number':
          if (data is String) {
            _addToInput(data);
          }
          break;
        case 'createShortcut':
          // Lógica para crear atajos
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Atajo creado para operación frecuente')),
          );
          break;
        case 'scientificNotation':
          // Convertir a notación científica
          if (_output.isNotEmpty) {
            double? value = double.tryParse(_output);
            if (value != null) {
              _output = value.toStringAsExponential(2);
              _input = _output;
            }
          }
          break;
        case 'enableScientificMode':
          _toggleScientificMode(true);
          break;
        case 'enableDarkMode':
          // Esta funcionalidad requiere un ThemeProvider en la app
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Modo oscuro activado')),
          );
          break;
        case 'closeParenthesis':
          _addToInput(')');
          break;
        case 'trigFunction':
          if (data is double) {
            // Mostrar un diálogo para elegir la función trigonométrica
            _showTrigFunctionDialog(data);
          }
          break;
        case 'saveHistory':
          // Guardar historial (simulado)
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Historial guardado')),
          );
          break;
        case 'correctInput':
          // Corregir entrada con operadores duplicados
          if (data is String) {
            _input = data;
            ScaffoldMessenger.of(context).showSnackBar(
              const SnackBar(content: Text('Se corrigieron operadores duplicados')),
            );
          }
          break;
      }
      
      // Actualizar el contexto del MCP después de la acción
      _updateMCPContext();
    });
  }
  
  // Diálogo para elegir función trigonométrica
  void _showTrigFunctionDialog(double value) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Calcular para $value'),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            ListTile(
              title: const Text('Seno'),
              onTap: () {
                Navigator.of(context).pop();
                setState(() {
                  // Convertir a radianes y calcular
                  double radians = value * (math.pi / 180);
                  _input = 'sin($value)';
                  _output = math.sin(radians).toString();
                  _history.add("$_input = $_output");
                });
              },
            ),
            ListTile(
              title: const Text('Coseno'),
              onTap: () {
                Navigator.of(context).pop();
                setState(() {
                  // Convertir a radianes y calcular
                  double radians = value * (math.pi / 180);
                  _input = 'cos($value)';
                  _output = math.cos(radians).toString();
                  _history.add("$_input = $_output");
                });
              },
            ),
            ListTile(
              title: const Text('Tangente'),
              onTap: () {
                Navigator.of(context).pop();
                setState(() {
                  // Convertir a radianes y calcular
                  double radians = value * (math.pi / 180);
                  _input = 'tan($value)';
                  _output = math.tan(radians).toString();
                  _history.add("$_input = $_output");
                });
              },
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: const Text('Cancelar'),
          ),
        ],
      ),
    );
  }

  void _calculate() {
    try {
      // Simulación simple de cálculo para demostración
      // En una implementación real, se necesitaría un evaluador de expresiones matemáticas
      _output = _evaluateExpression(_input);
      _history.add("$_input = $_output");
      _input = _output;
      
      // Ejecutar MCP automática después del cálculo
      _executeMCPAutoAction();
      
      // Actualizar contexto MCP
      _updateMCPContext();
    } catch (e) {
      _output = "Error";
      _updateMCPContext();
    }
  }
  
  void _executeMCPAutoAction() {
    // Esta función ejecuta automáticamente acciones MCP basadas en patrones específicos
    
    // Por ejemplo, si el resultado es un número muy grande, sugerir notación científica
    if (_output.length > 10) {
      MCPService().executeAutomaticAction(context);
    }
    
    // Si la operación es una raíz cuadrada con resultado no entero, podemos sugerir redondear
    if (_input.contains('√') && _output.contains('.') && _output.length > 6) {
      final action = MCPAction(
        type: MCPActionType.suggestion,
        message: "¿Quieres redondear el resultado a 2 decimales?",
        action: () {
          setState(() {
            double value = double.parse(_output);
            _output = value.toStringAsFixed(2);
            _input = _output;
            _updateMCPContext();
          });
        },
        icon: Icons.rounded_corner,
      );
      
      MCPNotificationManager().showAction(context, action);
    }
  }

  // Evaluador simple de expresiones (solo para demostración)
  String _evaluateExpression(String expression) {
    // Esta es una implementación muy básica para demostración
    // En una calculadora real, necesitarías un analizador más complejo
    try {
      // Simulemos algunos cálculos básicos
      if (expression.contains('+')) {
        List<String> parts = expression.split('+');
        double result = double.parse(parts[0]) + double.parse(parts[1]);
        return result.toString();
      } else if (expression.contains('-')) {
        List<String> parts = expression.split('-');
        double result = double.parse(parts[0]) - double.parse(parts[1]);
        return result.toString();
      } else if (expression.contains('×')) {
        List<String> parts = expression.split('×');
        double result = double.parse(parts[0]) * double.parse(parts[1]);
        return result.toString();
      } else if (expression.contains('÷')) {
        List<String> parts = expression.split('÷');
        double result = double.parse(parts[0]) / double.parse(parts[1]);
        return result.toString();
      }
      return expression; // Si no hay operación, devuelve la expresión original
    } catch (e) {
      return "Error"; // En caso de cualquier error
    }
  }

  void _toggleScientificMode(bool value) {
    setState(() {
      _showScientificButtons = value;
      HapticFeedback.lightImpact(); // Retroalimentación táctil al cambiar modo
      
      // Actualizar contexto MCP
      _updateMCPContext();
      
      // Si es la primera vez que se activa el modo científico, mostrar un mensaje guía
      if (value && !_history.any((item) => item.contains('sin') || item.contains('cos'))) {
        final action = MCPAction(
          type: MCPActionType.notification,
          message: "Ahora puedes usar funciones científicas como seno, coseno y logaritmos.",
          action: () {},
          icon: Icons.info_outline,
        );
        
        MCPNotificationManager().showAction(context, action);
      }
    });
  }

  void _showHistoryDialog() {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text('Historial de cálculos'),
          content: SizedBox(
            width: double.maxFinite,
            child: _history.isEmpty
                ? const Center(child: Text('No hay historial disponible'))
                : ListView.builder(
                    itemCount: _history.length,
                    itemBuilder: (context, index) {
                      return ListTile(
                        title: Text(_history[_history.length - 1 - index]),
                        onTap: () {
                          setState(() {
                            _input = _history[_history.length - 1 - index].split(' = ')[0];
                          });
                          Navigator.pop(context);
                        },
                      );
                    },
                  ),
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: const Text('Cerrar'),
            ),
            TextButton(
              onPressed: () {
                setState(() {
                  _history.clear();
                });
                Navigator.of(context).pop();
              },
              child: const Text('Limpiar historial'),
            ),
          ],
        );
      },
    );
  }

  void _showMCPDialog() {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Row(
            children: [
              const Icon(Icons.psychology, color: Colors.purple),
              const SizedBox(width: 10),
              const Text('Asistente MCP Predictivo'),
            ],
          ),
          content: SingleChildScrollView(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  'El Modelo de Contexto de Plataforma (MCP) es una IA predictiva que analiza tu comportamiento, aprende de tus patrones y ofrece sugerencias personalizadas.',
                  style: TextStyle(fontSize: 16),
                ),
                const SizedBox(height: 16),
                const Text(
                  'Capacidades de IA:',
                  style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
                ),
                const SizedBox(height: 8),
                ListTile(
                  leading: const Icon(Icons.psychology, color: Colors.purple),
                  title: const Text('Predicción inteligente'),
                  subtitle: const Text('Anticipa tus próximas acciones'),
                  onTap: () {
                    Navigator.pop(context);
                    // Simulamos una acción de MCP predictiva
                    final action = MCPAction(
                      type: MCPActionType.prediction,
                      message: "Basado en tu historial, predigo que quieres calcular un promedio",
                      action: () {
                        // Lógica para sugerir operación de promedio
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(content: Text('Calculando promedio...')),
                        );
                      },
                      icon: Icons.psychology,
                    );
                    
                    MCPNotificationManager().showAction(context, action);
                  },
                ),
                ListTile(
                  leading: const Icon(Icons.pattern, color: Colors.blue),
                  title: const Text('Análisis de patrones'),
                  subtitle: const Text('Detecta secuencias repetitivas'),
                  onTap: () {
                    Navigator.pop(context);
                    // Simulamos una acción de detección de patrones
                    final action = MCPAction(
                      type: MCPActionType.suggestion,
                      message: "He detectado un patrón repetitivo en tus cálculos. ¿Quieres que cree un atajo?",
                      action: () {
                        // Lógica para crear atajos
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(content: Text('Atajo creado para operación frecuente')),
                        );
                      },
                      icon: Icons.auto_awesome_motion,
                      data: "Patrón: × → + → =",
                    );
                    
                    MCPNotificationManager().showAction(context, action);
                  },
                ),
                ListTile(
                  leading: const Icon(Icons.auto_fix_high, color: Colors.orange),
                  title: const Text('Corrección automática'),
                  subtitle: const Text('Detecta y corrige errores'),
                  onTap: () {
                    Navigator.pop(context);
                    // Simulamos una acción de corrección automática
                    final action = MCPAction(
                      type: MCPActionType.automatic,
                      message: "He corregido automáticamente la expresión",
                      action: () {},
                      icon: Icons.auto_fix_high,
                      data: "2+++3 → 2+3",
                    );
                    
                    MCPNotificationManager().showAction(context, action);
                  },
                ),
                ListTile(
                  leading: const Icon(Icons.screen_rotation, color: Colors.green),
                  title: const Text('Adaptación inteligente'),
                  subtitle: const Text('La interfaz se adapta a tus necesidades'),
                  onTap: () {
                    Navigator.pop(context);
                    // Simulamos una acción de adaptación de interfaz
                    final action = MCPAction(
                      type: MCPActionType.suggestion,
                      message: "He notado que usas frecuentemente funciones científicas. ¿Quiero reordenar los botones para facilitar tu trabajo?",
                      action: () {
                        // Activar el modo científico
                        setState(() {
                          _showScientificButtons = true;
                          _updateMCPContext();
                        });
                      },
                      icon: Icons.view_module,
                    );
                    
                    MCPNotificationManager().showAction(context, action);
                  },
                ),
                const Divider(),
                ListTile(
                  leading: const Icon(Icons.api, color: Colors.deepPurple),
                  title: const Text('Ejecutar diagnóstico MCP'),
                  subtitle: const Text('Análisis completo de tus patrones'),
                  onTap: () {
                    Navigator.pop(context);
                    // Ejecutar diagnóstico completo
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(
                        content: Text('Analizando patrones de uso...'),
                        duration: Duration(seconds: 2),
                      ),
                    );
                    
                    // Simular tiempo de análisis
                    Future.delayed(const Duration(seconds: 2), () {
                      MCPService().executeAutomaticAction(context);
                      
                      // Mostrar resultados de diagnóstico
                      final action = MCPAction(
                        type: MCPActionType.notification,
                        message: "Diagnóstico MCP completado",
                        action: () {},
                        icon: Icons.analytics,
                        data: "Patrones detectados: 3\nAcciones predichas: 2\nOptimizaciones sugeridas: 1",
                      );
                      
                      MCPNotificationManager().showAction(context, action);
                    });
                  },
                ),
              ],
            ),
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: const Text('Cerrar'),
            ),
          ],
        );
      },
    );
  }

  void _showSettingsDialog() {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text('Configuración'),
          content: const SingleChildScrollView(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Próximamente: opciones de configuración'),
              ],
            ),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('Cerrar'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: _scaffoldKey,
      appBar: AppBar(
        title: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text('Calculadora Científica'),
            const SizedBox(width: 8),
            // Indicador de MCP Predictivo
            Container(
              padding: const EdgeInsets.symmetric(
                horizontal: 6,
                vertical: 2,
              ),
              decoration: BoxDecoration(
                color: Colors.purple.withOpacity(0.2),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Row(
                children: [
                  Icon(
                    Icons.psychology,
                    size: 14,
                    color: Colors.purple[700],
                  ),
                  const SizedBox(width: 4),
                  Text(
                    'MCP',
                    style: TextStyle(
                      color: Colors.purple[700],
                      fontSize: 10,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
        centerTitle: true,
        elevation: 2,
        actions: [
          Tooltip(
            message: _showScientificButtons ? 'Modo básico' : 'Modo científico',
            child: Switch(
              value: _showScientificButtons,
              onChanged: _toggleScientificMode,
              activeColor: Theme.of(context).colorScheme.primary,
            ),
          ),
          IconButton(
            icon: const Icon(Icons.history),
            tooltip: 'Historial',
            onPressed: _showHistoryDialog,
          ),
          const SizedBox(width: 8),
        ],
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            DrawerHeader(
              decoration: BoxDecoration(
                color: Theme.of(context).colorScheme.primary,
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  const Icon(
                    Icons.calculate_rounded,
                    color: Colors.white,
                    size: 40,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    'Calculadora Científica',
                    style: TextStyle(
                      color: Theme.of(context).colorScheme.onPrimary,
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    'Versión 1.0.0',
                    style: TextStyle(
                      color: Theme.of(context).colorScheme.onPrimary.withOpacity(0.8),
                      fontSize: 14,
                    ),
                  ),
                ],
              ),
            ),
            ListTile(
              leading: const Icon(Icons.history),
              title: const Text('Historial'),
              onTap: () {
                Navigator.pop(context);
                _showHistoryDialog();
              },
            ),
            const Divider(),
            // Nuevo ítem para el MCP
            ListTile(
              leading: const Icon(Icons.assistant),
              title: const Text('Asistente MCP'),
              subtitle: const Text('Recomendaciones inteligentes'),
              onTap: () {
                Navigator.pop(context);
                _showMCPDialog();
              },
            ),
            const Divider(),
            ListTile(
              leading: const Icon(Icons.settings),
              title: const Text('Configuración'),
              onTap: () {
                Navigator.pop(context);
                _showSettingsDialog();
              },
            ),
            ListTile(
              leading: const Icon(Icons.dark_mode),
              title: const Text('Tema oscuro'),
              trailing: Switch(
                value: Theme.of(context).brightness == Brightness.dark,
                onChanged: (value) {
                  // Aquí iría la lógica para cambiar el tema
                  Navigator.pop(context);
                },
              ),
            ),
            const Divider(),
            ListTile(
              leading: const Icon(Icons.info_outline),
              title: const Text('Acerca de'),
              onTap: () {
                Navigator.pop(context);
                showAboutDialog(
                  context: context,
                  applicationName: 'Calculadora Científica',
                  applicationVersion: '1.0.0',
                  applicationIcon: const Icon(Icons.calculate_rounded),
                  children: const [
                    Text('Una calculadora científica avanzada con múltiples funcionalidades.'),
                    SizedBox(height: 12),
                    Text('Desarrollada con Flutter.'),
                  ],
                );
              },
            ),
          ],
        ),
      ),
      body: SafeArea(
        child: Column(
          children: [
            // Display
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: CalculatorDisplay(
                input: _input,
                output: _output,
              ),
            ),
            
            // Keyboard
            CalculatorKeyboard(
              onButtonPressed: _onButtonPressed,
              showScientificButtons: _showScientificButtons,
            ),
          ],
        ),
      ),
    );
  }
}

    