import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../constants/app_colors.dart';
import '../screens/home_screen.dart'; // Importa a HomeScreen
import '../screens/auth/auth_page.dart'; // Importa a página de autenticação

class AppNavbar extends StatefulWidget {
  const AppNavbar({super.key});

  @override
  State<AppNavbar> createState() => _AppNavbarState();
}

class _AppNavbarState extends State<AppNavbar> {
  bool _isHoveringHome = false;
  bool _isHoveringAbout = false;

  @override
  Widget build(BuildContext context) {
    return Container(
      color: AppColors.black.withOpacity(0.5), // Cor de fundo semi-transparente para a navbar
      padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 8.0), // Aumenta o padding vertical
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween, // Mantém espaço entre a esquerda e a direita
        children: [
          // Título/Logo à esquerda com padding
          Padding(
            padding: const EdgeInsets.only(left: 50.0), // Aumenta o padding à esquerda
            child: Text(
              'NOFLX UNB',
              style: GoogleFonts.permanentMarker(
                fontSize: 36, // Tamanho da fonte do título
                color: AppColors.white,
                shadows: [
                  const Shadow(
                    color: Color.fromARGB(77, 0, 0, 0), // Mantido Color.fromARGB para consistência
                    offset: Offset(2, 2),
                    blurRadius: 4,
                  ),
                ],
              ),
            ),
          ),
          // Links de navegação e botão agrupados à direita
          Row(
            mainAxisSize: MainAxisSize.min, // Ocupa o mínimo de espaço horizontal
            children: [
              TextButton(
                onPressed: () {
                  // Navegar para a HomeScreen (se já não estiver nela)
                   Navigator.pushAndRemoveUntil(
                    context,
                    MaterialPageRoute(builder: (context) => const HomeScreen()),
                    (Route<dynamic> route) => false, // Remove todas as rotas anteriores
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
                    fontSize: 19, // Tamanho de fonte menor para a navbar
                    color: _isHoveringHome ? AppColors.primary : AppColors.white, // Muda a cor ao passar o mouse
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(width: 16), // Espaço entre os links
              TextButton(
                onPressed: () {
                  // TODO: Implementar navegação para a tela Sobre Nós
                },
                 onHover: (isHovering) {
                  setState(() {
                    _isHoveringAbout = isHovering;
                  });
                },
                child: Text(
                  'SOBRE NÓS',
                  style: GoogleFonts.permanentMarker(
                    fontSize: 19,
                    color: _isHoveringAbout ? AppColors.primary : AppColors.white,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(width: 24), // Espaço entre os links e o botão
              // Botão de Acesso à direita
              ElevatedButton(
                onPressed: () {
                  // Navegar para a página de autenticação
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => const AuthPage(),
                    ),
                  );
                },
                 style: ElevatedButton.styleFrom(
                   backgroundColor: Colors.transparent, // Fundo transparente para o gradiente
                   elevation: 0, // Remove qualquer elevação padrão
                   shadowColor: Colors.transparent, // Garante que não há sombra
                   padding: const EdgeInsets.symmetric(horizontal: 2, vertical: 12), // Reduz ainda mais o padding horizontal
                   shape: RoundedRectangleBorder(
                     borderRadius: BorderRadius.circular(30.0),
                   ),
                 ),
                child: Ink(
                  decoration: BoxDecoration(
                    gradient: const LinearGradient(
                      colors: [AppColors.purple, AppColors.pink], // Alterado para gradiente roxo para rosa
                      begin: Alignment.centerLeft,
                      end: Alignment.centerRight,
                    ),
                    borderRadius: BorderRadius.circular(30.0),
                  ),
                  child: Container(
                    constraints: const BoxConstraints(minWidth: 260.0, minHeight: 40.0), // Aumenta o minWidth para 280.0
                    alignment: Alignment.center,
                    child: Text(
                      'ACESSE NOSSO SISTEMA',
                      textAlign: TextAlign.center,
                      style: GoogleFonts.permanentMarker(
                        fontSize: 19,
                        fontWeight: FontWeight.bold,
                        color: AppColors.white,
                      ),
                    ),
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
} 