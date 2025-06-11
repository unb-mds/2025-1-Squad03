import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:flutter/gestures.dart';

class LoginForm extends StatefulWidget {
  final VoidCallback onToggleView;
  const LoginForm({super.key, required this.onToggleView});

  @override
  State<LoginForm> createState() => _LoginFormState();
}

class _LoginFormState extends State<LoginForm> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  bool _obscurePassword = true;
  bool _rememberMe = false;
  final TapGestureRecognizer _forgotPasswordRecognizer = TapGestureRecognizer();
  final TapGestureRecognizer _signupRecognizer = TapGestureRecognizer();

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    _forgotPasswordRecognizer.dispose();
    _signupRecognizer.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.95),
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.2),
            blurRadius: 32,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 32),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Text(
            'Login',
            style: GoogleFonts.poppins(
              fontSize: 28,
              fontWeight: FontWeight.bold,
              color: Colors.black,
            ),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 24),
          // Email
          TextField(
            controller: _emailController,
            keyboardType: TextInputType.emailAddress,
            style: GoogleFonts.poppins(fontSize: 16),
            decoration: InputDecoration(
              prefixIcon: const Icon(Icons.email_outlined, color: Colors.black54),
              hintText: 'Email',
              filled: true,
              fillColor: Colors.white,
              contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 16),
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(10),
                borderSide: const BorderSide(color: Color(0xFFE2E8F0)),
              ),
              enabledBorder: OutlineInputBorder(
                borderRadius: BorderRadius.circular(10),
                borderSide: const BorderSide(color: Color(0xFFE2E8F0)),
              ),
              focusedBorder: OutlineInputBorder(
                borderRadius: BorderRadius.circular(10),
                borderSide: const BorderSide(color: Color(0xFF1B469B), width: 2),
              ),
            ),
          ),
          const SizedBox(height: 16),
          // Senha
          TextField(
            controller: _passwordController,
            obscureText: _obscurePassword,
            style: GoogleFonts.poppins(fontSize: 16),
            decoration: InputDecoration(
              prefixIcon: const Icon(Icons.lock_outline, color: Colors.black54),
              hintText: 'Senha',
              filled: true,
              fillColor: Colors.white,
              contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 16),
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(10),
                borderSide: const BorderSide(color: Color(0xFFE2E8F0)),
              ),
              enabledBorder: OutlineInputBorder(
                borderRadius: BorderRadius.circular(10),
                borderSide: const BorderSide(color: Color(0xFFE2E8F0)),
              ),
              focusedBorder: OutlineInputBorder(
                borderRadius: BorderRadius.circular(10),
                borderSide: const BorderSide(color: Color(0xFF1B469B), width: 2),
              ),
              suffixIcon: IconButton(
                icon: Icon(_obscurePassword ? Icons.visibility_off : Icons.visibility, color: Colors.black54),
                onPressed: () => setState(() => _obscurePassword = !_obscurePassword),
              ),
            ),
          ),
          const SizedBox(height: 10),
          // Lembrar-me e Esqueceu a senha
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Row(
                children: [
                  Checkbox(
                    value: _rememberMe,
                    onChanged: (v) => setState(() => _rememberMe = v ?? false),
                    activeColor: const Color(0xFF1B469B),
                  ),
                  Text('Lembrar-me', style: GoogleFonts.poppins(fontSize: 14, color: Colors.grey[700])),
                ],
              ),
              RichText(
                text: TextSpan(
                  text: 'Esqueceu a senha?',
                  style: GoogleFonts.poppins(
                    fontSize: 14,
                    color: const Color(0xFF6366F1),
                    decoration: TextDecoration.underline,
                  ),
                  recognizer: _forgotPasswordRecognizer..onTap = () {
                    // TODO: ação de esqueci minha senha
                  },
                ),
              ),
            ],
          ),
          const SizedBox(height: 10),
          // Botão Entrar
          SizedBox(
            height: 48,
            child: ElevatedButton(
              onPressed: () {},
              style: ElevatedButton.styleFrom(
                backgroundColor: const Color(0xFF1B469B),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                elevation: 0,
              ),
              child: Text(
                'Entrar',
                style: GoogleFonts.poppins(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
              ),
            ),
          ),
          // Separador
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 18),
            child: Row(
              children: [
                const Expanded(child: Divider(color: Color(0xFFE2E8F0), thickness: 1)),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 8),
                  child: Container(
                    color: Colors.white,
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                    child: Text('ou', style: GoogleFonts.poppins(fontSize: 14, color: Colors.grey[500])),
                  ),
                ),
                const Expanded(child: Divider(color: Color(0xFFE2E8F0), thickness: 1)),
              ],
            ),
          ),
          // Botão Google
          SizedBox(
            height: 48,
            child: OutlinedButton(
              onPressed: () {},
              style: OutlinedButton.styleFrom(
                backgroundColor: Colors.white,
                side: const BorderSide(color: Color(0xFFE2E8F0)),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  SizedBox(
                    width: 22,
                    height: 22,
                    child: SvgPicture.string(
                      '''<svg viewBox="0 0 24 24"><path fill="#EA4335" d="M5.266 9.765A7.077 7.077 0 0 1 12 4.909c1.69 0 3.218.6 4.418 1.582L19.91 3C17.782 1.145 15.055 0 12 0 7.27 0 3.198 2.698 1.24 6.65l4.026 3.115Z"/><path fill="#34A853" d="M16.04 18.013c-1.09.703-2.474 1.078-4.04 1.078a7.077 7.077 0 0 1-6.723-4.823l-4.04 3.067A11.965 11.965 0 0 0 12 24c2.933 0 5.735-1.043 7.834-3l-3.793-2.987Z"/><path fill="#4A90E2" d="M19.834 21c2.195-2.048 3.62-5.096 3.62-9 0-.71-.109-1.473-.272-2.182H12v4.637h6.436c-.317 1.559-1.17 2.766-2.395 3.558L19.834 21Z"/><path fill="#FBBC05" d="M5.277 14.268A7.12 7.12 0 0 1 4.909 12c0-.782.125-1.533.357-2.235L1.24 6.65A11.934 11.934 0 0 0 0 12c0 1.92.445 3.73 1.237 5.335l4.04-3.067Z"/></svg>''',
                    ),
                  ),
                  const SizedBox(width: 10),
                  Text(
                    'Entrar com o Google',
                    style: GoogleFonts.poppins(fontSize: 16, color: Colors.black87, fontWeight: FontWeight.w500),
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(height: 10),
          // Botão Visitante
          SizedBox(
            height: 48,
            child: ElevatedButton(
              onPressed: () {},
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.black,
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                elevation: 0,
              ),
              child: Text(
                'Entrar como Visitante',
                style: GoogleFonts.poppins(fontSize: 16, color: Colors.white, fontWeight: FontWeight.w500),
              ),
            ),
          ),
          const SizedBox(height: 16),
          // Link para cadastro
          Center(
            child: RichText(
              text: TextSpan(
                text: 'Não tem uma conta? ',
                style: GoogleFonts.poppins(fontSize: 15, color: Colors.black),
                children: [
                  TextSpan(
                    text: 'Cadastre-se',
                    style: GoogleFonts.poppins(
                      color: Colors.black,
                      decoration: TextDecoration.underline,
                      fontWeight: FontWeight.w500,
                    ),
                    recognizer: _signupRecognizer..onTap = widget.onToggleView,
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
} 