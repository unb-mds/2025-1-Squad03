import 'package:flutter/material.dart';

class ComoFuncionaSection extends StatelessWidget {
  const ComoFuncionaSection({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 64),
      decoration: BoxDecoration(
        color: Colors.black.withOpacity(0.5),
      ),
      child: Column(
        children: [
          const Text(
            'COMO FUNCIONA',
            style: TextStyle(
              color: Colors.white,
              fontSize: 32,
              fontWeight: FontWeight.bold,
              fontFamily: 'PermanentMarker',
            ),
          ),
          const SizedBox(height: 48),
          LayoutBuilder(
            builder: (context, constraints) {
              bool isWide = constraints.maxWidth > 900;
              final cards = [
                _buildFeatureCard(
                  icon: Icons.assignment,
                  title: 'VISUALIZE SEU FLUXO',
                  description: 'Veja todas as disciplinas do seu curso organizadas por semestre e pré-requisitos.',
                  gradientColors: const [Color(0xFF9333EA), Color(0xFFEC4899)],
                ),
                _buildFeatureCard(
                  icon: Icons.add_circle_outline,
                  title: 'ADICIONE OPTATIVAS',
                  description: 'Personalize seu fluxograma adicionando matérias optativas de acordo com seus interesses.',
                  gradientColors: const [Color(0xFFEC4899), Color(0xFFF97316)],
                ),
                _buildFeatureCard(
                  icon: Icons.check_circle_outline,
                  title: 'ACOMPANHE SEU PROGRESSO',
                  description: 'Marque as disciplinas já cursadas e visualize seu progresso no curso de forma clara.',
                  gradientColors: const [Color(0xFFF97316), Color(0xFFEAB308)],
                ),
              ];
              if (isWide) {
                return Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: cards
                      .map((card) => Expanded(
                            child: Padding(
                              padding: const EdgeInsets.symmetric(horizontal: 16.0),
                              child: card,
                            ),
                          ))
                      .toList(),
                );
              } else {
                return Column(
                  children: cards
                      .map((card) => Padding(
                            padding: const EdgeInsets.symmetric(vertical: 16.0),
                            child: card,
                          ))
                      .toList(),
                );
              }
            },
          ),
        ],
      ),
    );
  }

  Widget _buildFeatureCard({
    required IconData icon,
    required String title,
    required String description,
    required List<Color> gradientColors,
  }) {
    return Container(
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.1),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(
          color: Colors.white.withOpacity(0.1),
        ),
      ),
      child: Column(
        children: [
          Container(
            width: 64,
            height: 64,
            decoration: BoxDecoration(
              gradient: LinearGradient(
                colors: gradientColors,
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
              borderRadius: BorderRadius.circular(32),
            ),
            child: Icon(
              icon,
              color: Colors.white,
              size: 32,
            ),
          ),
          const SizedBox(height: 16),
          Text(
            title,
            style: const TextStyle(
              color: Colors.white,
              fontSize: 20,
              fontWeight: FontWeight.bold,
              fontFamily: 'PermanentMarker',
            ),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 8),
          Text(
            description,
            style: TextStyle(
              color: Colors.grey[300],
              fontSize: 16,
            ),
            textAlign: TextAlign.center,
          ),
        ],
      ),
    );
  }
} 