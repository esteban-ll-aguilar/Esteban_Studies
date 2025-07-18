import 'package:flutter/material.dart';
import 'dart:math' as math;
import 'mcp_action.dart';
import 'mcp_ai_engine.dart';

/// Widget avanzado para mostrar recomendaciones de IA con animaciones y efectos visuales
class MCPAIRecommendationWidget extends StatefulWidget {
  final MCPAction action;
  final VoidCallback onAccept;
  final VoidCallback onDismiss;
  final Function(bool)? onFeedback;

  const MCPAIRecommendationWidget({
    super.key,
    required this.action,
    required this.onAccept,
    required this.onDismiss,
    this.onFeedback,
  });

  @override
  State<MCPAIRecommendationWidget> createState() => _MCPAIRecommendationWidgetState();
}

class _MCPAIRecommendationWidgetState extends State<MCPAIRecommendationWidget>
    with TickerProviderStateMixin {
  
  late AnimationController _slideController;
  late AnimationController _pulseController;
  late AnimationController _confidenceController;
  
  late Animation<Offset> _slideAnimation;
  late Animation<double> _pulseAnimation;
  late Animation<double> _confidenceAnimation;
  
  bool _isExpanded = false;
  bool _showFeedback = false;

  @override
  void initState() {
    super.initState();
    
    // Configurar animaciones
    _slideController = AnimationController(
      duration: const Duration(milliseconds: 500),
      vsync: this,
    );
    
    _pulseController = AnimationController(
      duration: const Duration(milliseconds: 1500),
      vsync: this,
    );
    
    _confidenceController = AnimationController(
      duration: const Duration(milliseconds: 800),
      vsync: this,
    );
    
    _slideAnimation = Tween<Offset>(
      begin: const Offset(1.0, 0.0),
      end: Offset.zero,
    ).animate(CurvedAnimation(
      parent: _slideController,
      curve: Curves.elasticOut,
    ));
    
    _pulseAnimation = Tween<double>(
      begin: 1.0,
      end: 1.1,
    ).animate(CurvedAnimation(
      parent: _pulseController,
      curve: Curves.easeInOut,
    ));
    
    _confidenceAnimation = Tween<double>(
      begin: 0.0,
      end: _getConfidenceLevel(),
    ).animate(CurvedAnimation(
      parent: _confidenceController,
      curve: Curves.easeOutCubic,
    ));
    
    // Iniciar animaciones
    _slideController.forward();
    _confidenceController.forward();
    
    // Pulso para recomendaciones de alta prioridad
    if (_isHighPriority()) {
      _pulseController.repeat(reverse: true);
    }
  }

  @override
  void dispose() {
    _slideController.dispose();
    _pulseController.dispose();
    _confidenceController.dispose();
    super.dispose();
  }

  double _getConfidenceLevel() {
    // Extraer nivel de confianza de los metadatos si está disponible
    if (widget.action.data is Map<String, dynamic>) {
      final data = widget.action.data as Map<String, dynamic>;
      return (data['confidence'] as double?) ?? 0.8;
    }
    return 0.8; // Valor por defecto
  }

  bool _isHighPriority() {
    return widget.action.type == MCPActionType.prediction ||
           widget.action.type == MCPActionType.automatic;
  }

  Color _getTypeColor() {
    switch (widget.action.type) {
      case MCPActionType.prediction:
        return Colors.purple;
      case MCPActionType.automatic:
        return Colors.green;
      case MCPActionType.suggestion:
        return Colors.blue;
      case MCPActionType.notification:
        return Colors.orange;
    }
  }

  String _getTypeLabel() {
    switch (widget.action.type) {
      case MCPActionType.prediction:
        return 'PREDICCIÓN IA';
      case MCPActionType.automatic:
        return 'ACCIÓN AUTOMÁTICA';
      case MCPActionType.suggestion:
        return 'SUGERENCIA';
      case MCPActionType.notification:
        return 'NOTIFICACIÓN';
    }
  }

  @override
  Widget build(BuildContext context) {
    return SlideTransition(
      position: _slideAnimation,
      child: AnimatedBuilder(
        animation: _pulseAnimation,
        builder: (context, child) {
          return Transform.scale(
            scale: _pulseAnimation.value,
            child: Container(
              margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              child: Material(
                elevation: 8,
                borderRadius: BorderRadius.circular(20),
                color: Colors.transparent,
                child: Container(
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(20),
                    gradient: LinearGradient(
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                      colors: [
                        _getTypeColor().withOpacity(0.1),
                        _getTypeColor().withOpacity(0.05),
                        Colors.white.withOpacity(0.9),
                      ],
                    ),
                    border: Border.all(
                      color: _getTypeColor().withOpacity(0.3),
                      width: 2,
                    ),
                    boxShadow: [
                      BoxShadow(
                        color: _getTypeColor().withOpacity(0.2),
                        blurRadius: 15,
                        offset: const Offset(0, 5),
                      ),
                    ],
                  ),
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      _buildHeader(),
                      _buildContent(),
                      if (_isExpanded) _buildExpandedContent(),
                      _buildActions(),
                      if (_showFeedback) _buildFeedbackSection(),
                    ],
                  ),
                ),
              ),
            ),
          );
        },
      ),
    );
  }

  Widget _buildHeader() {
    return Container(
      padding: const EdgeInsets.all(16),
      child: Row(
        children: [
          // Icono animado
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: _getTypeColor().withOpacity(0.2),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Icon(
              widget.action.icon,
              color: _getTypeColor(),
              size: 24,
            ),
          ),
          const SizedBox(width: 16),
          
          // Información principal
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Etiqueta de tipo
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                  decoration: BoxDecoration(
                    color: _getTypeColor(),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Text(
                    _getTypeLabel(),
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 10,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                const SizedBox(height: 8),
                
                // Mensaje principal
                Text(
                  widget.action.message,
                  style: const TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.w600,
                    color: Colors.black87,
                  ),
                ),
              ],
            ),
          ),
          
          // Botón de expansión
          IconButton(
            onPressed: () {
              setState(() {
                _isExpanded = !_isExpanded;
              });
            },
            icon: AnimatedRotation(
              turns: _isExpanded ? 0.5 : 0,
              duration: const Duration(milliseconds: 300),
              child: const Icon(Icons.expand_more),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildContent() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16),
      child: Column(
        children: [
          // Barra de confianza
          _buildConfidenceBar(),
          
          // Datos adicionales si existen
          if (widget.action.data != null) _buildDataPreview(),
        ],
      ),
    );
  }

  Widget _buildConfidenceBar() {
    return Container(
      margin: const EdgeInsets.symmetric(vertical: 8),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                'Nivel de Confianza IA',
                style: TextStyle(
                  fontSize: 12,
                  color: Colors.grey[600],
                  fontWeight: FontWeight.w500,
                ),
              ),
              Text(
                '${(_getConfidenceLevel() * 100).toInt()}%',
                style: TextStyle(
                  fontSize: 12,
                  color: _getTypeColor(),
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
          const SizedBox(height: 4),
          AnimatedBuilder(
            animation: _confidenceAnimation,
            builder: (context, child) {
              return LinearProgressIndicator(
                value: _confidenceAnimation.value,
                backgroundColor: Colors.grey[300],
                valueColor: AlwaysStoppedAnimation<Color>(_getTypeColor()),
                minHeight: 6,
              );
            },
          ),
        ],
      ),
    );
  }

  Widget _buildDataPreview() {
    if (widget.action.data == null) return const SizedBox.shrink();
    
    return Container(
      margin: const EdgeInsets.symmetric(vertical: 8),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.grey[100],
        borderRadius: BorderRadius.circular(8),
        border: Border.all(color: Colors.grey[300]!),
      ),
      child: Row(
        children: [
          Icon(
            Icons.data_object,
            size: 16,
            color: Colors.grey[600],
          ),
          const SizedBox(width: 8),
          Expanded(
            child: Text(
              widget.action.data.toString(),
              style: TextStyle(
                fontSize: 12,
                color: Colors.grey[700],
                fontFamily: 'monospace',
              ),
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildExpandedContent() {
    return AnimatedContainer(
      duration: const Duration(milliseconds: 300),
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Divider(),
          
          // Información técnica
          _buildTechnicalInfo(),
          
          const SizedBox(height: 16),
          
          // Análisis de contexto
          _buildContextAnalysis(),
        ],
      ),
    );
  }

  Widget _buildTechnicalInfo() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Información Técnica',
          style: TextStyle(
            fontSize: 14,
            fontWeight: FontWeight.bold,
            color: Colors.grey[800],
          ),
        ),
        const SizedBox(height: 8),
        
        _buildInfoRow('Timestamp', widget.action.timestamp.toString()),
        _buildInfoRow('Tipo de IA', _getAITypeDescription()),
        _buildInfoRow('Algoritmo', _getAlgorithmDescription()),
      ],
    );
  }

  Widget _buildContextAnalysis() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Análisis de Contexto',
          style: TextStyle(
            fontSize: 14,
            fontWeight: FontWeight.bold,
            color: Colors.grey[800],
          ),
        ),
        const SizedBox(height: 8),
        
        Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: _getTypeColor().withOpacity(0.1),
            borderRadius: BorderRadius.circular(8),
          ),
          child: Text(
            _getContextAnalysisText(),
            style: TextStyle(
              fontSize: 12,
              color: Colors.grey[700],
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildInfoRow(String label, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 2),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            width: 80,
            child: Text(
              '$label:',
              style: TextStyle(
                fontSize: 12,
                color: Colors.grey[600],
                fontWeight: FontWeight.w500,
              ),
            ),
          ),
          Expanded(
            child: Text(
              value,
              style: TextStyle(
                fontSize: 12,
                color: Colors.grey[800],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildActions() {
    return Container(
      padding: const EdgeInsets.all(16),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.end,
        children: [
          // Botón de feedback
          if (widget.onFeedback != null)
            TextButton.icon(
              onPressed: () {
                setState(() {
                  _showFeedback = !_showFeedback;
                });
              },
              icon: const Icon(Icons.feedback_outlined, size: 16),
              label: const Text('Feedback'),
              style: TextButton.styleFrom(
                foregroundColor: Colors.grey[600],
              ),
            ),
          
          const SizedBox(width: 8),
          
          // Botón de rechazo
          if (widget.action.type == MCPActionType.suggestion || 
             widget.action.type == MCPActionType.prediction)
            TextButton(
              onPressed: () {
                _slideController.reverse().then((_) {
                  widget.onDismiss();
                });
              },
              child: const Text('No, gracias'),
              style: TextButton.styleFrom(
                foregroundColor: Colors.grey[600],
              ),
            ),
          
          const SizedBox(width: 8),
          
          // Botón de acción principal
          ElevatedButton.icon(
            onPressed: () {
              widget.action.action();
              _slideController.reverse().then((_) {
                widget.onAccept();
              });
            },
            icon: Icon(_getActionIcon()),
            label: Text(_getActionLabel()),
            style: ElevatedButton.styleFrom(
              backgroundColor: _getTypeColor(),
              foregroundColor: Colors.white,
              elevation: 4,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(12),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildFeedbackSection() {
    return AnimatedContainer(
      duration: const Duration(milliseconds: 300),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.grey[50],
        borderRadius: const BorderRadius.only(
          bottomLeft: Radius.circular(20),
          bottomRight: Radius.circular(20),
        ),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            '¿Te fue útil esta recomendación?',
            style: TextStyle(
              fontSize: 14,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 12),
          
          Row(
            children: [
              _buildFeedbackButton(
                icon: Icons.thumb_up,
                label: 'Útil',
                isPositive: true,
                onTap: () {
                  widget.onFeedback?.call(true);
                  setState(() {
                    _showFeedback = false;
                  });
                },
              ),
              const SizedBox(width: 12),
              _buildFeedbackButton(
                icon: Icons.thumb_down,
                label: 'No útil',
                isPositive: false,
                onTap: () {
                  widget.onFeedback?.call(false);
                  setState(() {
                    _showFeedback = false;
                  });
                },
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildFeedbackButton({
    required IconData icon,
    required String label,
    required bool isPositive,
    required VoidCallback onTap,
  }) {
    final color = isPositive ? Colors.green : Colors.red;
    
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(8),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
        decoration: BoxDecoration(
          border: Border.all(color: color.withOpacity(0.3)),
          borderRadius: BorderRadius.circular(8),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(icon, size: 16, color: color),
            const SizedBox(width: 8),
            Text(
              label,
              style: TextStyle(
                color: color,
                fontWeight: FontWeight.w500,
              ),
            ),
          ],
        ),
      ),
    );
  }

  IconData _getActionIcon() {
    switch (widget.action.type) {
      case MCPActionType.automatic:
        return Icons.check;
      case MCPActionType.prediction:
      case MCPActionType.suggestion:
        return Icons.arrow_forward;
      case MCPActionType.notification:
        return Icons.close;
    }
  }

  String _getActionLabel() {
    switch (widget.action.type) {
      case MCPActionType.automatic:
        return 'Entendido';
      case MCPActionType.prediction:
      case MCPActionType.suggestion:
        return 'Aplicar';
      case MCPActionType.notification:
        return 'Cerrar';
    }
  }

  String _getAITypeDescription() {
    switch (widget.action.type) {
      case MCPActionType.prediction:
        return 'Red Neuronal Predictiva';
      case MCPActionType.automatic:
        return 'Sistema de Reglas Automáticas';
      case MCPActionType.suggestion:
        return 'Análisis de Patrones';
      case MCPActionType.notification:
        return 'Sistema de Notificaciones';
    }
  }

  String _getAlgorithmDescription() {
    switch (widget.action.type) {
      case MCPActionType.prediction:
        return 'Backpropagation + Clustering';
      case MCPActionType.automatic:
        return 'Análisis de Contexto';
      case MCPActionType.suggestion:
        return 'Detección de Secuencias';
      case MCPActionType.notification:
        return 'Filtros Temporales';
    }
  }

  String _getContextAnalysisText() {
    switch (widget.action.type) {
      case MCPActionType.prediction:
        return 'Esta predicción se basa en el análisis de tus últimas 50 acciones y patrones de uso detectados por la red neuronal.';
      case MCPActionType.automatic:
        return 'Acción ejecutada automáticamente basada en reglas predefinidas y el contexto actual de la aplicación.';
      case MCPActionType.suggestion:
        return 'Sugerencia generada mediante análisis de patrones de comportamiento y clustering de usuarios similares.';
      case MCPActionType.notification:
        return 'Notificación informativa basada en eventos del sistema y preferencias del usuario.';
    }
  }
}
