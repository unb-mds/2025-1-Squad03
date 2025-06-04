import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../constants/app_colors.dart';

class Header extends StatelessWidget {
  const Header({super.key});

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        // Título centralizado
        Align(
          alignment: Alignment.center,
          child: Padding(
            padding: const EdgeInsets.only(top: 40.0), // Ajuste vertical do título
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
        Positioned(
          top: 0.0, // Ajuste vertical para ficar ainda mais para cima
          right: 24.0, // Ajuste horizontal para o canto direito
          child: TextButton(
            onPressed: () {
              // TODO: Navegar para a tela inicial (HOME)
            },
            child: Text(
              'HOME',
              style: GoogleFonts.permanentMarker(
                fontSize: 24, // Tamanho da fonte pela metade (48 / 2)
                color: AppColors.white,
                shadows: [
                  Shadow(
                    color: AppColors.black.withOpacity(0.3),
                    offset: const Offset(1, 1), // Ajuste o offset da sombra para o tamanho menor
                    blurRadius: 2, // Ajuste o blurRadius da sombra para o tamanho menor
                  ),
                ],
              ),
            ),
          ),
        ),
      ],
    );
  }
} 