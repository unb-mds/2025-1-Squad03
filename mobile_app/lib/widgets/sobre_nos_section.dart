import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_svg/flutter_svg.dart';

class SobreNosSection extends StatelessWidget {
  const SobreNosSection({super.key});

  @override
  Widget build(BuildContext context) {
    final isWide = MediaQuery.of(context).size.width > 900;
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 64, horizontal: 0),
      color: Colors.black.withOpacity(0.5),
      child: Column(
        children: [
          Text(
            'SOBRE NÓS',
            style: GoogleFonts.permanentMarker(
              color: Colors.white,
              fontSize: 32,
              letterSpacing: 1.5,
              shadows: const [
                Shadow(
                  color: Color.fromARGB(120, 0, 0, 0),
                  offset: Offset(2, 2),
                  blurRadius: 4,
                ),
              ],
            ),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 32),
          // Card de descrição
          Center(
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 1200),
              child: Container(
                margin: const EdgeInsets.only(bottom: 32),
                padding: const EdgeInsets.all(32),
                decoration: BoxDecoration(
                  color: Colors.white.withOpacity(0.10),
                  borderRadius: BorderRadius.circular(24),
                  border: Border.all(color: Colors.white.withOpacity(0.2)),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withOpacity(0.15),
                      blurRadius: 16,
                      offset: const Offset(0, 4),
                    ),
                  ],
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    RichText(
                      textAlign: TextAlign.justify,
                      text: TextSpan(
                        style: GoogleFonts.poppins(
                          color: Colors.white,
                          fontSize: 18,
                        ),
                        children: [
                          const TextSpan(text: 'O '),
                          TextSpan(text: 'NoFluxoUnB', style: const TextStyle(fontWeight: FontWeight.bold)),
                          const TextSpan(text: ' é criado na disciplina de '),
                          TextSpan(text: 'Métodos de Desenvolvimento de Software', style: const TextStyle(fontWeight: FontWeight.bold)),
                          const TextSpan(text: ', ministrada pela professora '),
                          TextSpan(text: 'Carla Rocha', style: const TextStyle(fontWeight: FontWeight.bold)),
                          const TextSpan(text: ', com a proposta de desenvolver um software inovador para a comunidade. Nossa proposta foi desenvolver um software que facilita o planejamento acadêmico dos estudantes da UnB, oferecendo um fluxograma interativo, intuitivo e de fácil uso. Visualize matérias equivalentes, selecione disciplinas futuras e receba recomendações personalizadas com inteligência artificial.'),
                        ],
                      ),
                    ),
                    const SizedBox(height: 12),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        const Icon(Icons.chat_bubble_outline, color: Colors.white70, size: 18),
                        const SizedBox(width: 6),
                        Text(
                          'Observação: ',
                          style: GoogleFonts.poppins(
                            color: Colors.white.withOpacity(0.8),
                            fontSize: 14,
                            fontStyle: FontStyle.italic,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        Flexible(
                          child: Text(
                            'Inicialmente disponível para cursos da FGA/UnB, com perspectiva de expansão!',
                            style: GoogleFonts.poppins(
                              color: Colors.white.withOpacity(0.8),
                              fontSize: 14,
                              fontStyle: FontStyle.italic,
                            ),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 18),
                    // Lista de features centralizada de verdade
                    Center(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          _featureItem('UX moderna:', 'Interface visual clara, responsiva e fácil de navegar.'),
                          _featureItem('Inteligência Artificial:', 'Sugestão de disciplinas alinhadas aos interesses do estudante.'),
                          _featureItem('Personalização:', 'Planejamento acadêmico inteligente e eficiente, adaptado ao perfil do aluno.'),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
          // Cards dos membros
          _membrosGrid(isWide),
        ],
      ),
    );
  }

  Widget _featureItem(String title, String desc) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Container(
            width: 28,
            height: 28,
            margin: const EdgeInsets.only(right: 10),
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                colors: [Color(0xFFEC4899), Color(0xFF8B5CF6)],
                begin: Alignment.centerLeft,
                end: Alignment.centerRight,
              ),
              shape: BoxShape.circle,
            ),
            child: Center(
              child: SvgPicture.string(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16"><path stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none" d="M5 13l4 4L19 7"/></svg>',
              ),
            ),
          ),
          ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 800),
            child: RichText(
              textAlign: TextAlign.left,
              text: TextSpan(
                style: GoogleFonts.poppins(
                  color: Colors.white,
                  fontSize: 15,
                ),
                children: [
                  TextSpan(text: title, style: const TextStyle(fontWeight: FontWeight.bold)),
                  TextSpan(text: ' $desc'),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _membrosGrid(bool isWide) {
    final membros = [
      _membroCard('Guilherme Gusmão', 'https://github.com/gusmoles.png'),
      _membroCard('Vitor Marconi', 'https://github.com/Vitor-Trancoso.png'),
      _membroCard('Gustavo Choueiri', 'https://github.com/staann.png'),
      _membroCard('Felipe Lopes', 'https://github.com/darkymeubem.png'),
      _membroCard('Vinícius Pereira', 'https://github.com/Vinicius-Ribeiro04.png'),
      _membroCard('Arthur Fernandes', 'https://github.com/hisarxt.png'),
      _membroCard('Erick Alves', 'https://github.com/erickaalves.png'),
    ];
    // Primeira linha: 4 cards, segunda linha: 3 cards centralizados
    return Column(
      children: [
        Wrap(
          alignment: WrapAlignment.center,
          spacing: 24,
          runSpacing: 24,
          children: membros.take(4).toList(),
        ),
        const SizedBox(height: 24),
        Wrap(
          alignment: WrapAlignment.center,
          spacing: 24,
          runSpacing: 24,
          children: membros.skip(4).toList(),
        ),
      ],
    );
  }

  Widget _membroCard(String nome, String imgUrl) {
    return Container(
      width: 220,
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.10),
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: Colors.white.withOpacity(0.10)),
      ),
      child: Column(
        children: [
          Container(
            width: 90,
            height: 90,
            margin: const EdgeInsets.only(bottom: 12),
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              border: Border.all(color: Colors.white, width: 4),
            ),
            child: ClipOval(
              child: Image.network(imgUrl, fit: BoxFit.cover),
            ),
          ),
          Text(
            nome,
            style: GoogleFonts.permanentMarker(
              color: Colors.white,
              fontSize: 20,
            ),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 4),
          Text(
            'Desenvolvedor',
            style: GoogleFonts.poppins(
              color: Colors.grey[300],
              fontSize: 14,
            ),
            textAlign: TextAlign.center,
          ),
        ],
      ),
    );
  }
} 