import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class CalculatorKeyboard extends StatelessWidget {
  final Function(String) onButtonPressed;
  final bool showScientificButtons;
  final Function(bool) onModeChanged;
  final VoidCallback onHistoryPressed;
  final VoidCallback onSettingsPressed;
  final VoidCallback onThemePressed;
  final int currentIndex;
  final Function(int) onTabSelected;

  const CalculatorKeyboard({
    super.key,
    required this.onButtonPressed,
    required this.showScientificButtons,
    this.onModeChanged = _defaultCallback,
    this.onHistoryPressed = _defaultVoidCallback,
    this.onSettingsPressed = _defaultVoidCallback,
    this.onThemePressed = _defaultVoidCallback,
    this.currentIndex = 0,
    this.onTabSelected = _defaultIndexCallback,
  });

  // Default callbacks to avoid null checks
  static void _defaultCallback(bool value) {}
  static void _defaultVoidCallback() {}
  static void _defaultIndexCallback(int index) {}

  @override
  Widget build(BuildContext context) {
    // Cambiado de Column a Expanded para evitar el error de altura ilimitada
    return Expanded(
      flex: 5,
      child: Column(
        children: [
          // Scientific buttons (conditional)
          if (showScientificButtons)
            _buildScientificButtons(context),
          
          // Basic calculator buttons
          _buildBasicButtons(context),
        ],
      ),
    );
  }

  Widget _buildScientificButtons(BuildContext context) {
    return AnimatedContainer(
      duration: const Duration(milliseconds: 300),
      curve: Curves.easeInOut,
      padding: const EdgeInsets.fromLTRB(8.0, 4.0, 8.0, 12.0),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.secondaryContainer.withOpacity(0.3),
        borderRadius: const BorderRadius.vertical(bottom: Radius.circular(16)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildButton(context, "sin", isFunction: true, tooltip: "Seno"),
              _buildButton(context, "cos", isFunction: true, tooltip: "Coseno"),
              _buildButton(context, "tan", isFunction: true, tooltip: "Tangente"),
              _buildButton(context, "π", isSpecial: true, tooltip: "Pi (3.1415...)"),
            ],
          ),
          const SizedBox(height: 8),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildButton(context, "x²", isFunction: true, tooltip: "Cuadrado"),
              _buildButton(context, "x³", isFunction: true, tooltip: "Cubo"),
              _buildButton(context, "xʸ", isFunction: true, tooltip: "Potencia"),
              _buildButton(context, "e", isSpecial: true, tooltip: "Número e (2.7182...)"),
            ],
          ),
          const SizedBox(height: 8),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildButton(context, "log", isFunction: true, tooltip: "Logaritmo base 10"),
              _buildButton(context, "ln", isFunction: true, tooltip: "Logaritmo natural"),
              _buildButton(context, "√", isFunction: true, tooltip: "Raíz cuadrada"),
              _buildButton(context, "(", isOperator: true, tooltip: "Paréntesis izquierdo"),
              _buildButton(context, ")", isOperator: true, tooltip: "Paréntesis derecho"),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildBasicButtons(BuildContext context) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          children: [
            Expanded(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  _buildButton(context, "C", isClear: true),
                  _buildButton(context, "⌫", isOperator: true),
                  _buildButton(context, "%", isOperator: true),
                  _buildButton(context, "÷", isOperator: true),
                ],
              ),
            ),
            Expanded(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  _buildButton(context, "7"),
                  _buildButton(context, "8"),
                  _buildButton(context, "9"),
                  _buildButton(context, "×", isOperator: true),
                ],
              ),
            ),
            Expanded(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  _buildButton(context, "4"),
                  _buildButton(context, "5"),
                  _buildButton(context, "6"),
                  _buildButton(context, "-", isOperator: true),
                ],
              ),
            ),
            Expanded(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  _buildButton(context, "1"),
                  _buildButton(context, "2"),
                  _buildButton(context, "3"),
                  _buildButton(context, "+", isOperator: true),
                ],
              ),
            ),
            Expanded(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  _buildButton(context, "0", flex: 2),
                  _buildButton(context, "."),
                  _buildButton(context, "=", isEquals: true),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildButton(BuildContext context, String text, {
    bool isOperator = false, 
    bool isClear = false, 
    bool isEquals = false,
    bool isFunction = false,
    bool isSpecial = false,
    String? tooltip,
    int flex = 1
  }) {
    Color backgroundColor;
    Color textColor;
    Color splashColor;
    IconData? iconData;
    
    if (isEquals) {
      backgroundColor = Theme.of(context).colorScheme.primary;
      textColor = Theme.of(context).colorScheme.onPrimary;
      splashColor = Theme.of(context).colorScheme.onPrimary.withOpacity(0.3);
    } else if (isOperator) {
      backgroundColor = Theme.of(context).colorScheme.primaryContainer;
      textColor = Theme.of(context).colorScheme.onPrimaryContainer;
      splashColor = Theme.of(context).colorScheme.onPrimaryContainer.withOpacity(0.3);
    } else if (isClear) {
      backgroundColor = Theme.of(context).colorScheme.errorContainer;
      textColor = Theme.of(context).colorScheme.onErrorContainer;
      splashColor = Theme.of(context).colorScheme.onErrorContainer.withOpacity(0.3);
    } else if (isFunction || isSpecial) {
      backgroundColor = Theme.of(context).colorScheme.secondaryContainer;
      textColor = Theme.of(context).colorScheme.onSecondaryContainer;
      splashColor = Theme.of(context).colorScheme.onSecondaryContainer.withOpacity(0.3);
    } else {
      backgroundColor = Theme.of(context).colorScheme.surfaceVariant;
      textColor = Theme.of(context).colorScheme.onSurfaceVariant;
      splashColor = Theme.of(context).colorScheme.onSurfaceVariant.withOpacity(0.3);
    }
    
    // Asignar iconos en lugar de texto para algunos botones
    if (text == "⌫") {
      iconData = Icons.backspace_outlined;
    } else if (text == "C") {
      iconData = Icons.clear;
    } else if (text == "=") {
      iconData = Icons.done;
    }
    
    return Expanded(
      flex: flex,
      child: Padding(
        padding: const EdgeInsets.all(4.0),
        child: Tooltip(
          message: tooltip ?? text,
          child: Material(
            color: backgroundColor,
            borderRadius: BorderRadius.circular(16),
            elevation: 2,
            shadowColor: Colors.black26,
            child: InkWell(
              borderRadius: BorderRadius.circular(16),
              splashColor: splashColor,
              highlightColor: splashColor.withOpacity(0.5),
              onTap: () {
                HapticFeedback.lightImpact(); // Retroalimentación táctil
                onButtonPressed(text);
              },
              child: Container(
                alignment: Alignment.center,
                padding: const EdgeInsets.all(8),
                child: iconData != null
                    ? Icon(iconData, color: textColor, size: 24)
                    : Text(
                        text,
                        style: TextStyle(
                          fontSize: 22,
                          fontWeight: isFunction || isOperator || isSpecial || isEquals
                              ? FontWeight.bold
                              : FontWeight.normal,
                          color: textColor,
                        ),
                      ),
              ),
            ),
          ),
        ),
      ),
    );
  }

  /// Construye un Drawer (Sidebar) personalizado para la calculadora
  static Widget buildDrawer(BuildContext context, {
    required VoidCallback onHistoryPressed,
    required VoidCallback onSettingsPressed,
    required VoidCallback onThemePressed,
  }) {
    return Drawer(
      elevation: 16.0,
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
              onHistoryPressed();
            },
          ),
          const Divider(),
          ListTile(
            leading: const Icon(Icons.settings),
            title: const Text('Configuración'),
            onTap: () {
              Navigator.pop(context);
              onSettingsPressed();
            },
          ),
          ListTile(
            leading: const Icon(Icons.color_lens),
            title: const Text('Cambiar tema'),
            onTap: () {
              Navigator.pop(context);
              onThemePressed();
            },
          ),
          const Divider(),
          ListTile(
            leading: const Icon(Icons.info_outline),
            title: const Text('Acerca de'),
            onTap: () {
              Navigator.pop(context);
              _showAboutDialog(context);
            },
          ),
        ],
      ),
    );
  }

  /// Construye un AppBar personalizado para la calculadora
  static PreferredSizeWidget buildAppBar(BuildContext context, {
    required String title,
    required bool showScientificButtons,
    required Function(bool) onModeChanged,
  }) {
    return AppBar(
      title: Text(title),
      centerTitle: true,
      elevation: 0,
      backgroundColor: Theme.of(context).colorScheme.surface,
      foregroundColor: Theme.of(context).colorScheme.onSurface,
      actions: [
        Tooltip(
          message: showScientificButtons ? 'Modo básico' : 'Modo científico',
          child: Switch(
            value: showScientificButtons,
            onChanged: onModeChanged,
            activeColor: Theme.of(context).colorScheme.primary,
            activeTrackColor: Theme.of(context).colorScheme.primaryContainer,
            inactiveThumbColor: Theme.of(context).colorScheme.surfaceVariant,
            inactiveTrackColor: Theme.of(context).colorScheme.outline,
          ),
        ),
        const SizedBox(width: 8),
      ],
    );
  }

  /// Construye un BottomNavigationBar para la calculadora
  static Widget buildBottomNavigationBar(BuildContext context, {
    required int currentIndex,
    required Function(int) onTabSelected,
  }) {
    return BottomNavigationBar(
      currentIndex: currentIndex,
      onTap: onTabSelected,
      type: BottomNavigationBarType.fixed,
      backgroundColor: Theme.of(context).colorScheme.surface,
      selectedItemColor: Theme.of(context).colorScheme.primary,
      unselectedItemColor: Theme.of(context).colorScheme.onSurfaceVariant,
      elevation: 8.0,
      items: const [
        BottomNavigationBarItem(
          icon: Icon(Icons.calculate),
          label: 'Calculadora',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.functions),
          label: 'Funciones',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.architecture),
          label: 'Conversión',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.history_edu),
          label: 'Historial',
        ),
      ],
    );
  }

  /// Muestra un diálogo de información sobre la aplicación
  static void _showAboutDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Acerca de Calculadora Científica'),
        content: const SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text('Una calculadora científica avanzada con múltiples funcionalidades.'),
              SizedBox(height: 12),
              Text('Desarrollada con Flutter.'),
              SizedBox(height: 12),
              Text('© 2023 - Todos los derechos reservados'),
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
}
