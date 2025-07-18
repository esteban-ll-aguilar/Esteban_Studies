import 'package:calculadora_cientifica_app/screens/home_page.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'screens/calculator_screen.dart';
import 'mcp/mcp.dart'; // Importamos el MCP
import 'dart:async'; // Para Timer

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown,
  ]);
  SystemChrome.setSystemUIOverlayStyle(
    const SystemUiOverlayStyle(
      statusBarColor: Colors.transparent,
      statusBarIconBrightness: Brightness.light,
    ),
  );
  
  // Inicializamos el servicio MCP
  final mcpService = MCPService();
  
  // Configuramos el sistema MCP con acciones de ejemplo
  _initializeMCP(mcpService);
  
  runApp(const MyApp());
}

// Inicializar MCP con algunos datos de entrenamiento para demostración
void _initializeMCP(MCPService mcpService) {
  // Secuencia de acciones para entrenar el modelo predictivo
  final trainingActions = [
    '+', '2', '=',
    '+', '3', '=',
    '+', '2', '=',
    '×', '2', '=',
    '÷', '4', '=',
    'sin', '30', ')',
    'sin', '45', ')',
    'sin', '60', ')',
    '+', '10', '=',
    '+', '10', '=',
    '√', '16', ')',
  ];
  
  // Ejecutar las acciones de entrenamiento con un retraso para simular uso real
  Timer.periodic(const Duration(milliseconds: 50), (timer) {
    if (trainingActions.isEmpty) {
      timer.cancel();
      return;
    }
    
    final action = trainingActions.removeAt(0);
    mcpService.trackUserAction(action);
    
    if (trainingActions.isEmpty) {
      timer.cancel();
    }
  });
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  ThemeMode _themeMode = ThemeMode.system;
  final GlobalKey<NavigatorState> _navigatorKey = GlobalKey<NavigatorState>();

  void toggleTheme(ThemeMode mode) {
    setState(() {
      _themeMode = mode;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Calculadora Científica',
      debugShowCheckedModeBanner: false,
      navigatorKey: _navigatorKey,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.blue,
          brightness: Brightness.light,
          primary: Colors.blue,
          secondary: Colors.teal,
          tertiary: Colors.orange,
        ),
        useMaterial3: true,
        fontFamily: 'Roboto',
        appBarTheme: const AppBarTheme(
          centerTitle: true,
          elevation: 2,
        ),
        drawerTheme: const DrawerThemeData(
          elevation: 16.0,
          backgroundColor: Colors.white,
          width: 280.0,
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16),
            ),
          ),
        ),
        bottomNavigationBarTheme: const BottomNavigationBarThemeData(
          selectedItemColor: Colors.blue,
          unselectedItemColor: Colors.grey,
          type: BottomNavigationBarType.fixed,
          elevation: 8.0,
        ),
      ),
      darkTheme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.blue,
          brightness: Brightness.dark,
        ),
        useMaterial3: true,
        fontFamily: 'Roboto',
        appBarTheme: const AppBarTheme(
          centerTitle: true,
          elevation: 2,
        ),
        bottomNavigationBarTheme: BottomNavigationBarThemeData(
          selectedItemColor: Colors.lightBlue[300],
          unselectedItemColor: Colors.grey,
          type: BottomNavigationBarType.fixed,
          elevation: 8.0,
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16),
            ),
          ), 
        ),
      ),
      themeMode: _themeMode,
      home: Builder(
        builder: (context) {
          // Configuramos un listener para las acciones del MCP
          MCPService().actionStream.listen((action) {
            // Usamos el MCPNotificationManager para mostrar las acciones
            MCPNotificationManager().showAction(context, action);
          });
          
          return const HomePage();
        },
      ),
    );
  }
}
