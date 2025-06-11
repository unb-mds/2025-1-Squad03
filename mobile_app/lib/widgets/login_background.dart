import 'dart:ui';
import 'package:flutter/material.dart';

class LoginBackground extends StatelessWidget {
  const LoginBackground({super.key});

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        Container(color: const Color(0xFF1a1a1a)),
        const SmokeEffect(
          color: Color(0xFF6B19C9),
          width: 300,
          height: 300,
          top: 0.10,
          left: 0.05,
          type: SmokeType.type1,
        ),
        const SmokeEffect(
          color: Color(0xFFE63783),
          width: 400,
          height: 400,
          top: 0.60,
          left: 0.70,
          type: SmokeType.type2,
        ),
        const SmokeEffect(
          color: Color(0xFFF0C419),
          width: 350,
          height: 350,
          top: 0.30,
          left: 0.60,
          type: SmokeType.type3,
        ),
        const SmokeEffect(
          color: Color(0xFF6B19C9),
          width: 250,
          height: 250,
          top: 0.70,
          left: 0.20,
          type: SmokeType.type1,
        ),
        const SmokeEffect(
          color: Color(0xFFE63783),
          width: 200,
          height: 200,
          top: 0.15,
          left: 0.80,
          type: SmokeType.type2,
        ),
      ],
    );
  }
}

enum SmokeType { type1, type2, type3 }

class SmokeEffect extends StatefulWidget {
  final Color color;
  final double width;
  final double height;
  final double top;
  final double left;
  final SmokeType type;

  const SmokeEffect({
    super.key,
    required this.color,
    required this.width,
    required this.height,
    required this.top,
    required this.left,
    required this.type,
  });

  @override
  State<SmokeEffect> createState() => _SmokeEffectState();
}

class _SmokeEffectState extends State<SmokeEffect> with SingleTickerProviderStateMixin {
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: Duration(
        seconds: widget.type == SmokeType.type1
            ? 25
            : widget.type == SmokeType.type2
                ? 30
                : 35,
      ),
      vsync: this,
    )..repeat(reverse: true);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  Matrix4 _getTransform(double t) {
    double dx = 0, dy = 0, scale = 1;
    if (widget.type == SmokeType.type1) {
      // float1
      if (t < 0.33) {
        dx = 50 * t / 0.33;
        dy = -30 * t / 0.33;
        scale = 1 + 0.1 * t / 0.33;
      } else if (t < 0.66) {
        dx = 50 - 80 * (t - 0.33) / 0.33;
        dy = -30 + 80 * (t - 0.33) / 0.33;
        scale = 1.1 - 0.2 * (t - 0.33) / 0.33;
      } else {
        dx = -30 + 50 * (t - 0.66) / 0.34;
        dy = 50 - 90 * (t - 0.66) / 0.34;
        scale = 0.9 + 0.15 * (t - 0.66) / 0.34;
      }
    } else if (widget.type == SmokeType.type2) {
      // float2
      if (t < 0.33) {
        dx = -40 * t / 0.33;
        dy = 20 * t / 0.33;
        scale = 1 - 0.05 * t / 0.33;
      } else if (t < 0.66) {
        dx = -40 + 70 * (t - 0.33) / 0.33;
        dy = 20 - 60 * (t - 0.33) / 0.33;
        scale = 0.95 + 0.1 * (t - 0.33) / 0.33;
      } else {
        dx = 30 - 50 * (t - 0.66) / 0.34;
        dy = -40 + 70 * (t - 0.66) / 0.34;
        scale = 1.05 - 0.15 * (t - 0.66) / 0.34;
      }
    } else {
      // float3
      if (t < 0.33) {
        dx = 30 * t / 0.33;
        dy = 40 * t / 0.33;
        scale = 1 + 0.1 * t / 0.33;
      } else if (t < 0.66) {
        dx = 30 - 70 * (t - 0.33) / 0.33;
        dy = 40 - 70 * (t - 0.33) / 0.33;
        scale = 1.1 - 0.15 * (t - 0.33) / 0.33;
      } else {
        dx = -40 + 60 * (t - 0.66) / 0.34;
        dy = -30 + 50 * (t - 0.66) / 0.34;
        scale = 0.95 + 0.1 * (t - 0.66) / 0.34;
      }
    }
    return Matrix4.identity()
      ..translate(dx, dy)
      ..scale(scale);
  }

  @override
  Widget build(BuildContext context) {
    final screen = MediaQuery.of(context).size;
    return Positioned(
      top: widget.top * screen.height,
      left: widget.left * screen.width,
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, child) {
          final t = _controller.value;
          return Opacity(
            opacity: 0.6,
            child: Transform(
              transform: _getTransform(t),
              child: ImageFiltered(
                imageFilter: ImageFilter.blur(sigmaX: 80, sigmaY: 80),
                child: Container(
                  width: widget.width,
                  height: widget.height,
                  decoration: BoxDecoration(
                    color: widget.color,
                    borderRadius: BorderRadius.circular(999),
                  ),
                ),
              ),
            ),
          );
        },
      ),
    );
  }
} 