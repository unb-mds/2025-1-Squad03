import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../constants/app_colors.dart';

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
      padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 16.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween, // Distribui espaço entre os elementos
        children: [
          // Título centralizado (usando Expanded e Center para forçar centralização em um Row)
          Expanded(
            child: Center(
              child: Text(
                'NOFLX UNB',
                style: GoogleFonts.permanentMarker(
                  fontSize: 48,
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
              // TODO: Navegar para a tela inicial (HOME)
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