import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:math' as math;

class NetworkCalculator extends StatefulWidget {
  const NetworkCalculator({super.key});

  @override
  State<NetworkCalculator> createState() => _NetworkCalculatorState();
}

class _NetworkCalculatorState extends State<NetworkCalculator> with AutomaticKeepAliveClientMixin {
  final TextEditingController _ipController = TextEditingController();
  final TextEditingController _maskController = TextEditingController();
  final TextEditingController _cidrController = TextEditingController();
  final TextEditingController _subnetCountController = TextEditingController();
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();
  
  // Resultados
  String _networkAddress = '';
  String _broadcastAddress = '';
  String _firstUsableIp = '';
  String _lastUsableIp = '';
  String _totalHosts = '';
  String _maskInDotted = '';
  String _wildcard = '';
  List<Map<String, String>> _subnets = [];
  bool _isValidInput = false;
  
  // Estado actual de la calculadora
  String _currentTab = 'subneteo';
  
  @override
  void initState() {
    super.initState();
    _ipController.text = '192.168.1.1';
    _cidrController.text = '24';
    _updateMaskFromCidr();
    _calculateNetwork();
  }
  
  @override
  void dispose() {
    _ipController.dispose();
    _maskController.dispose();
    _cidrController.dispose();
    _subnetCountController.dispose();
    super.dispose();
  }
  
  void _updateMaskFromCidr() {
    try {
      int cidr = int.parse(_cidrController.text);
      if (cidr >= 0 && cidr <= 32) {
        // Convertir CIDR a máscara de red en notación decimal con puntos
        int mask = (0xffffffff << (32 - cidr)) & 0xffffffff;
        String dottedMask = '${(mask >> 24) & 0xff}.${(mask >> 16) & 0xff}.${(mask >> 8) & 0xff}.${mask & 0xff}';
        _maskController.text = dottedMask;
      }
    } catch (e) {
      // No hacer nada si el CIDR no es válido
    }
  }
  
  void _updateCidrFromMask() {
    try {
      List<String> octets = _maskController.text.split('.');
      if (octets.length == 4) {
        int mask = 0;
        for (int i = 0; i < 4; i++) {
          mask |= int.parse(octets[i]) << (24 - i * 8);
        }
        
        // Contar bits 1 para determinar CIDR
        int cidr = 0;
        for (int i = 31; i >= 0; i--) {
          if ((mask & (1 << i)) != 0) {
            cidr++;
          } else {
            break;
          }
        }
        
        _cidrController.text = cidr.toString();
      }
    } catch (e) {
      // No hacer nada si la máscara no es válida
    }
  }
  
  List<int> _ipToIntList(String ip) {
    List<String> parts = ip.split('.');
    return parts.map((part) => int.parse(part)).toList();
  }
  
  String _intListToIp(List<int> ipList) {
    return ipList.join('.');
  }
  
  bool _isValidIp(String ip) {
    try {
      List<int> ipList = _ipToIntList(ip);
      if (ipList.length != 4) return false;
      for (int octet in ipList) {
        if (octet < 0 || octet > 255) return false;
      }
      return true;
    } catch (e) {
      return false;
    }
  }
  
  bool _isValidMask(String mask) {
    try {
      List<int> maskList = _ipToIntList(mask);
      if (maskList.length != 4) return false;
      
      // Convertir la máscara a un entero de 32 bits
      int intMask = 0;
      for (int i = 0; i < 4; i++) {
        if (maskList[i] < 0 || maskList[i] > 255) return false;
        intMask |= maskList[i] << (24 - i * 8);
      }
      
      // Verificar que la máscara sea continua (todos los 1s seguidos por todos los 0s)
      int shifted = ~intMask + 1;
      return (intMask & shifted) == 0 && intMask != 0;
    } catch (e) {
      return false;
    }
  }
  
  void _calculateNetwork() {
    String ip = _ipController.text;
    String mask = _maskController.text;
    
    if (!_isValidIp(ip) || !_isValidMask(mask)) {
      setState(() {
        _isValidInput = false;
      });
      return;
    }
    
    setState(() {
      _isValidInput = true;
      
      // Convertir IP y máscara a enteros
      List<int> ipOctets = _ipToIntList(ip);
      List<int> maskOctets = _ipToIntList(mask);
      
      // Calcular dirección de red
      List<int> networkOctets = List<int>.filled(4, 0);
      for (int i = 0; i < 4; i++) {
        networkOctets[i] = ipOctets[i] & maskOctets[i];
      }
      _networkAddress = _intListToIp(networkOctets);
      
      // Calcular wildcard (inverso de la máscara)
      List<int> wildcardOctets = List<int>.filled(4, 0);
      for (int i = 0; i < 4; i++) {
        wildcardOctets[i] = 255 - maskOctets[i];
      }
      _wildcard = _intListToIp(wildcardOctets);
      
      // Calcular dirección de broadcast
      List<int> broadcastOctets = List<int>.filled(4, 0);
      for (int i = 0; i < 4; i++) {
        broadcastOctets[i] = networkOctets[i] | wildcardOctets[i];
      }
      _broadcastAddress = _intListToIp(broadcastOctets);
      
      // Calcular primera IP utilizable
      List<int> firstIpOctets = List<int>.from(networkOctets);
      firstIpOctets[3] += 1;
      _firstUsableIp = _intListToIp(firstIpOctets);
      
      // Calcular última IP utilizable
      List<int> lastIpOctets = List<int>.from(broadcastOctets);
      lastIpOctets[3] -= 1;
      _lastUsableIp = _intListToIp(lastIpOctets);
      
      // Calcular total de hosts
      int cidr = int.parse(_cidrController.text);
      int hostBits = 32 - cidr;
      int totalHosts = math.pow(2, hostBits).toInt() - 2;
      _totalHosts = totalHosts > 0 ? totalHosts.toString() : '0';
      
      // Máscara en notación de puntos
      _maskInDotted = mask;
      
      // Calcular subredes si es necesario
      _calculateSubnets();
    });
  }
  
  void _calculateSubnets() {
    _subnets = [];
    
    if (_subnetCountController.text.isEmpty) return;
    
    try {
      int subnetsRequired = int.parse(_subnetCountController.text);
      if (subnetsRequired <= 0) return;
      
      // Calcular bits necesarios para el número de subredes
      int bitsNeeded = (math.log(subnetsRequired) / math.log(2)).ceil();
      int cidr = int.parse(_cidrController.text);
      int newCidr = cidr + bitsNeeded;
      
      if (newCidr > 30) {
        // No se pueden crear tantas subredes
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('No se pueden crear tantas subredes con esta configuración')),
        );
        return;
      }
      
      // Tamaño de cada subred
      int subnetSize = math.pow(2, 32 - newCidr).toInt();
      
      // Iniciar desde la dirección de red
      List<int> ipOctets = _ipToIntList(_networkAddress);
      int ipInt = (ipOctets[0] << 24) | (ipOctets[1] << 16) | (ipOctets[2] << 8) | ipOctets[3];
      
      for (int i = 0; i < subnetsRequired; i++) {
        int subnetIpInt = ipInt + (i * subnetSize);
        
        // Dirección de red de la subred
        String subnetIp = '${(subnetIpInt >> 24) & 0xff}.${(subnetIpInt >> 16) & 0xff}.${(subnetIpInt >> 8) & 0xff}.${subnetIpInt & 0xff}';
        
        // Dirección de broadcast de la subred
        int broadcastIpInt = subnetIpInt + subnetSize - 1;
        String broadcastIp = '${(broadcastIpInt >> 24) & 0xff}.${(broadcastIpInt >> 16) & 0xff}.${(broadcastIpInt >> 8) & 0xff}.${broadcastIpInt & 0xff}';
        
        // Primera IP utilizable
        int firstIpInt = subnetIpInt + 1;
        String firstIp = '${(firstIpInt >> 24) & 0xff}.${(firstIpInt >> 16) & 0xff}.${(firstIpInt >> 8) & 0xff}.${firstIpInt & 0xff}';
        
        // Última IP utilizable
        int lastIpInt = broadcastIpInt - 1;
        String lastIp = '${(lastIpInt >> 24) & 0xff}.${(lastIpInt >> 16) & 0xff}.${(lastIpInt >> 8) & 0xff}.${lastIpInt & 0xff}';
        
        _subnets.add({
          'red': subnetIp,
          'mascara': '/${newCidr}',
          'primera': firstIp,
          'ultima': lastIp,
          'broadcast': broadcastIp,
          'hosts': (subnetSize - 2).toString()
        });
      }
    } catch (e) {
      // Manejar errores
    }
  }
  
  void _onIpChanged(String value) {
    _calculateNetwork();
  }
  
  void _onMaskChanged(String value) {
    _updateCidrFromMask();
    _calculateNetwork();
  }
  
  void _onCidrChanged(String value) {
    _updateMaskFromCidr();
    _calculateNetwork();
  }
  
  void _onSubnetCountChanged(String value) {
    _calculateNetwork();
  }
  
  Widget _buildInputField(String label, TextEditingController controller, Function(String) onChanged, {String? hint, TextInputType? keyboardType}) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8.0),
      child: TextFormField(
        controller: controller,
        decoration: InputDecoration(
          labelText: label,
          hintText: hint,
          border: const OutlineInputBorder(),
          contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 16),
        ),
        keyboardType: keyboardType ?? TextInputType.text,
        onChanged: onChanged,
      ),
    );
  }
  
  Widget _buildResultItem(String label, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            label,
            style: const TextStyle(
              fontWeight: FontWeight.bold,
            ),
          ),
          Text(
            value,
            style: TextStyle(
              color: Theme.of(context).colorScheme.primary,
            ),
          ),
        ],
      ),
    );
  }
  
  Widget _buildSubnetCalculator() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        _buildInputField('Dirección IP', _ipController, _onIpChanged, 
          hint: '192.168.1.1', 
          keyboardType: TextInputType.number),
        Row(
          children: [
            Expanded(
              flex: 2,
              child: _buildInputField('Máscara', _maskController, _onMaskChanged, 
                hint: '255.255.255.0', 
                keyboardType: TextInputType.number),
            ),
            const SizedBox(width: 16),
            Expanded(
              flex: 1,
              child: _buildInputField('CIDR', _cidrController, _onCidrChanged, 
                hint: '24', 
                keyboardType: TextInputType.number),
            ),
          ],
        ),
        _buildInputField('Número de subredes', _subnetCountController, _onSubnetCountChanged, 
          hint: 'Opcional', 
          keyboardType: TextInputType.number),
        
        const SizedBox(height: 16),
        const Divider(),
        const SizedBox(height: 8),
        
        // Resultados
        if (_isValidInput) ...[
          const Text(
            'Información de la Red:',
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 8),
          _buildResultItem('Dirección de Red:', _networkAddress),
          _buildResultItem('Máscara de Subred:', _maskInDotted),
          _buildResultItem('CIDR:', '/${_cidrController.text}'),
          _buildResultItem('Wildcard:', _wildcard),
          _buildResultItem('Broadcast:', _broadcastAddress),
          _buildResultItem('Primera IP utilizable:', _firstUsableIp),
          _buildResultItem('Última IP utilizable:', _lastUsableIp),
          _buildResultItem('Total de Hosts:', _totalHosts),
          
          if (_subnets.isNotEmpty) ...[
            const SizedBox(height: 16),
            const Text(
              'Subredes:',
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8),
            SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: DataTable(
                columns: const [
                  DataColumn(label: Text('Red')),
                  DataColumn(label: Text('Máscara')),
                  DataColumn(label: Text('Primera IP')),
                  DataColumn(label: Text('Última IP')),
                  DataColumn(label: Text('Broadcast')),
                  DataColumn(label: Text('Hosts')),
                ],
                rows: _subnets.map((subnet) => DataRow(
                  cells: [
                    DataCell(Text(subnet['red']!)),
                    DataCell(Text(subnet['mascara']!)),
                    DataCell(Text(subnet['primera']!)),
                    DataCell(Text(subnet['ultima']!)),
                    DataCell(Text(subnet['broadcast']!)),
                    DataCell(Text(subnet['hosts']!)),
                  ],
                )).toList(),
              ),
            ),
          ],
        ],
      ],
    );
  }
  
  Widget _buildIPConverter() {
    return const Center(
      child: Text('Conversor de IP - Próximamente'),
    );
  }
  
  Widget _buildCIDRChart() {
    // Lista de mascaras CIDR y sus equivalentes
    final List<Map<String, String>> cidrTable = [
      {'cidr': '/32', 'mask': '255.255.255.255', 'hosts': '1'},
      {'cidr': '/31', 'mask': '255.255.255.254', 'hosts': '2'},
      {'cidr': '/30', 'mask': '255.255.255.252', 'hosts': '4'},
      {'cidr': '/29', 'mask': '255.255.255.248', 'hosts': '8'},
      {'cidr': '/28', 'mask': '255.255.255.240', 'hosts': '16'},
      {'cidr': '/27', 'mask': '255.255.255.224', 'hosts': '32'},
      {'cidr': '/26', 'mask': '255.255.255.192', 'hosts': '64'},
      {'cidr': '/25', 'mask': '255.255.255.128', 'hosts': '128'},
      {'cidr': '/24', 'mask': '255.255.255.0', 'hosts': '256'},
      {'cidr': '/23', 'mask': '255.255.254.0', 'hosts': '512'},
      {'cidr': '/22', 'mask': '255.255.252.0', 'hosts': '1,024'},
      {'cidr': '/21', 'mask': '255.255.248.0', 'hosts': '2,048'},
      {'cidr': '/20', 'mask': '255.255.240.0', 'hosts': '4,096'},
      {'cidr': '/19', 'mask': '255.255.224.0', 'hosts': '8,192'},
      {'cidr': '/18', 'mask': '255.255.192.0', 'hosts': '16,384'},
      {'cidr': '/17', 'mask': '255.255.128.0', 'hosts': '32,768'},
      {'cidr': '/16', 'mask': '255.255.0.0', 'hosts': '65,536'},
      {'cidr': '/8', 'mask': '255.0.0.0', 'hosts': '16,777,216'},
    ];
    
    return SingleChildScrollView(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Tabla de Referencia CIDR',
              style: TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 16),
            DataTable(
              columns: const [
                DataColumn(label: Text('CIDR')),
                DataColumn(label: Text('Máscara')),
                DataColumn(label: Text('Hosts')),
              ],
              rows: cidrTable.map((item) => DataRow(
                cells: [
                  DataCell(Text(item['cidr']!)),
                  DataCell(Text(item['mask']!)),
                  DataCell(Text(item['hosts']!)),
                ],
              )).toList(),
            ),
          ],
        ),
      ),
    );
  }
  
  @override
  Widget build(BuildContext context) {
    super.build(context);
    
    return Scaffold(
      key: _scaffoldKey,
      appBar: AppBar(
        title: const Text('Calculadora de Redes'),
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.info_outline),
            onPressed: () {
              showAboutDialog(
                context: context,
                applicationName: 'Calculadora de Redes',
                applicationVersion: '1.0.0',
                applicationIcon: const Icon(Icons.router),
                children: const [
                  Text('Una herramienta para cálculo de redes y subredes IP.'),
                  SizedBox(height: 12),
                  Text('Incluye subneteo, conversión IP y referencias CIDR.'),
                ],
              );
            },
          ),
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
                    Icons.router,
                    color: Colors.white,
                    size: 40,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    'Calculadora de Redes',
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
              leading: const Icon(Icons.wifi),
              title: const Text('Calculadora de Subredes'),
              selected: _currentTab == 'subneteo',
              onTap: () {
                setState(() {
                  _currentTab = 'subneteo';
                });
                Navigator.pop(context);
              },
            ),
            ListTile(
              leading: const Icon(Icons.swap_horiz),
              title: const Text('Conversor IP'),
              selected: _currentTab == 'conversor',
              onTap: () {
                setState(() {
                  _currentTab = 'conversor';
                });
                Navigator.pop(context);
              },
            ),
            ListTile(
              leading: const Icon(Icons.table_chart),
              title: const Text('Tabla CIDR'),
              selected: _currentTab == 'tabla',
              onTap: () {
                setState(() {
                  _currentTab = 'tabla';
                });
                Navigator.pop(context);
              },
            ),
            const Divider(),
            ListTile(
              leading: const Icon(Icons.help_outline),
              title: const Text('Ayuda'),
              onTap: () {
                Navigator.pop(context);
                showDialog(
                  context: context,
                  builder: (context) => AlertDialog(
                    title: const Text('Ayuda'),
                    content: const SingleChildScrollView(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Text('Cómo usar la calculadora de redes:', style: TextStyle(fontWeight: FontWeight.bold)),
                          SizedBox(height: 8),
                          Text('1. Ingrese una dirección IP válida.'),
                          Text('2. Especifique la máscara de red o el valor CIDR.'),
                          Text('3. Opcionalmente, indique el número de subredes deseadas.'),
                          Text('4. Los resultados se mostrarán automáticamente.'),
                        ],
                      ),
                    ),
                    actions: [
                      TextButton(
                        onPressed: () => Navigator.of(context).pop(),
                        child: const Text('Entendido'),
                      ),
                    ],
                  ),
                );
              },
            ),
          ],
        ),
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: SingleChildScrollView(
            child: _currentTab == 'subneteo' 
                ? _buildSubnetCalculator()
                : _currentTab == 'conversor'
                    ? _buildIPConverter()
                    : _buildCIDRChart(),
          ),
        ),
      ),
    );
  }
  
  @override
  bool get wantKeepAlive => true;
}
