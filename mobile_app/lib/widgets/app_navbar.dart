import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../constants/app_colors.dart';
import '../screens/home_screen.dart'; // Importa a HomeScreen

class AppNavbar extends StatefulWidget {
  const AppNavbar({super.key});

  @override
  State<AppNavbar> createState() => _AppNavbarState();
}

class _AppNavbarState extends State<AppNavbar> {
  bool _isHoveringHome = false;

  @override
  Widget build(BuildContext context) {
    return Container(
      color: AppColors.black.withOpacity(0.5), // Cor de fundo semi-transparente para a navbar
      padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 1.0), // Diminui o padding vertical novamente
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween, // Distribui espaço entre os elementos
        children: [
          // Título centralizado (usando Expanded e Center para forçar centralização em um Row)
          Expanded(
            child: Center(
              child: Text(
                'NOFLX UNB',
                style: GoogleFonts.permanentMarker(
                  fontSize: 36, // Diminui o tamanho da fonte do título
                  color: AppColors.white,
                  shadows: [
                    Shadow(
                      color: AppColors.black.withOpacity(0.3),
                      offset: const Offset(2, 2),
                      blurRadius: 4,
                    ),
                  ],
                ),
              ),
            ),
          ),
          // Botão HOME no canto superior direito
          TextButton(
            onPressed: () {
              // Navegar para a HomeScreen
              Navigator.push( // Usando push para simplificar por enquanto
                context,
                MaterialPageRoute(
                  builder: (context) => const HomeScreen(),
                ),
              );
            },
            onHover: (isHovering) {
              setState(() {
                _isHoveringHome = isHovering;
              });
            },
            child: Text(
              'HOME',
              style: GoogleFonts.permanentMarker(
                fontSize: 16, // Tamanho de fonte menor para a navbar
                color: _isHoveringHome ? AppColors.primary : AppColors.white, // Muda a cor ao passar o mouse
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ],
      ),
    );
  }
} 