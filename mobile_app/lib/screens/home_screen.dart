import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../constants/app_colors.dart';
import '../widgets/animated_background.dart';
import '../widgets/app_navbar.dart';
import 'auth/auth_page.dart'; // Importa a página de autenticação
import 'package:flutter_svg/flutter_svg.dart'; // Importa o flutter_svg

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          const AnimatedBackground(), // Fundo animado
          SafeArea(
            child: Column(
              children: [
                const AppNavbar(), // Navbar no topo
                Expanded(
                  child: SingleChildScrollView(
                    child: Padding(
                      padding: const EdgeInsets.all(24.0),
                      child: Row( // Adiciona um Row para layout lado a lado
                        crossAxisAlignment: CrossAxisAlignment.start, // Alinha o conteúdo no topo
                        children: [
                          Expanded( // Texto principal e botão na esquerda, com flex maior
                            flex: 2, // Dá mais espaço para o texto (ajuste conforme necessário)
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start, // Alinhar conteúdo à esquerda
                              children: [
                                // Título principal
                                Text(
                                  'TENHA SEU\nFLUXOGRAMA\nMUITO RÁPIDO',
                                  style: GoogleFonts.permanentMarker(
                                    fontSize: 56, // Tamanho grande para o título
                                    color: AppColors.white,
                                    shadows: [
                                      Shadow(
                                        color: AppColors.black.withOpacity(0.3),
                                        offset: const Offset(3, 3),
                                        blurRadius: 6,
                                      ),
                                    ],
                                  ),
                                ),
                                const SizedBox(height: 24), // Espaço entre o título e o texto descritivo
                                // Texto descritivo
                                Text(
                                  'O NO FLUXO UNB TE AJUDA A VER O FLUXOGRAMA DO SEU CURSO E AINDA TE\nPERMITE ADICIONAR MATÉRIAS OPTATIVAS DE ACORDO COM SUAS ÁREAS DE\nINTERESSE!',
                                  style: GoogleFonts.poppins(
                                    fontSize: 16,
                                    color: AppColors.white.withOpacity(0.9),
                                  ),
                                ),
                                const SizedBox(height: 40), // Espaço entre o texto descritivo e o botão
                                // Botão principal
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
                                        colors: [AppColors.primary, AppColors.primaryDark], // Gradiente similar ao do fundo
                                        begin: Alignment.centerLeft,
                                        end: Alignment.centerRight,
                                      ),
                                      borderRadius: BorderRadius.circular(30.0),
                                    ),
                                    child: Container(
                                      constraints: const BoxConstraints(minWidth: 50.0, minHeight: 40.0), // Mantém o minWidth, o padding controlará mais
                                      alignment: Alignment.center,
                                      child: Text(
                                        'ACESSE NOSSO SISTEMA',
                                        textAlign: TextAlign.center,
                                        style: GoogleFonts.poppins(
                                          fontSize: 16,
                                          fontWeight: FontWeight.bold,
                                          color: AppColors.white,
                                        ),
                                      ),
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ), // Mantemos o Expanded aqui e adicionamos flex
                          // Ícone SVG à direita e textos sobre ele usando Stack (agora encapsulado)
                          Expanded( // Envolve o novo widget em Expanded para distribuição de espaço
                            flex: 2, // Dá espaço horizontal (ajuste conforme necessário)
                            child: Padding(
                              padding: const EdgeInsets.only(left: 24.0), // Espaço entre o texto e o ícone
                              child: SvgPicture.asset(
                                'assets/icons/computer_phone.svg',
                                width: 600, // Você pode ajustar a largura aqui conforme necessário
                              ), // Usa o SvgPicture.asset diretamente aqui
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
} 