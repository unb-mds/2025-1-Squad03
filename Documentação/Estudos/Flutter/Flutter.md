# 🧠 O que é Flutter?

Flutter é um framework de desenvolvimento de aplicações criado pelo Google que permite construir **aplicativos nativos para Android, iOS, web e desktop** a partir de uma única base de código, utilizando a linguagem **Dart**.

---

## 💎 Vantagens do Flutter

- 🚀 **Desempenho Nativo**: Aplicações compiladas diretamente para código nativo.
- 🔄 **Hot Reload**: Veja alterações no código quase instantaneamente sem reiniciar o app.
- 🧩 **UI Rica e Personalizável**: Widgets altamente customizáveis e bonitos, seguindo Material Design e Cupertino.
- 📦 **Base de Código Única**: Um único projeto para Android, iOS, Web e Desktop.
- 📱 **Compatibilidade com Dispositivos Antigos**: Funciona bem mesmo em versões mais antigas dos sistemas operacionais.
- 🌐 **Comunidade Ativa e Suporte do Google**: Grande quantidade de pacotes e plugins disponíveis.
- 🧪 **Facilidade de Testes**: Suporte nativo a testes de unidade, widget e integração.

---

# 📦 Guia de Instalação do Flutter

Este guia irá te ajudar a instalar o Flutter no seu sistema (Windows, macOS ou Linux) passo a passo.

---

## 🔽 1. Baixando o Flutter

Acesse o site oficial do Flutter:  
👉 [Link oficial para download do Flutter](https://flutter.dev/docs/get-started/install)

Escolha seu sistema operacional e baixe o SDK.

---

## 📁 2. Extraia o Flutter

Extraia o arquivo `.zip` ou `.tar.xz` baixado para o local de sua preferência:

### Linux/macOS
```bash
cd ~
mkdir development
cd development
unzip ~/Downloads/flutter_linux_x.x.x-stable.zip
```

### Windows
Use o Explorer para extrair o `.zip` para `C:\src\flutter` (evite espaços no caminho).

---

## 🛣 3. Adicione o Flutter ao PATH

### Windows
1. Vá em **Painel de Controle > Sistema > Configurações Avançadas do Sistema**.
2. Clique em **Variáveis de Ambiente**.
3. Em **Variáveis de sistema**, selecione `Path` > **Editar**.
4. Adicione: `C:\src\flutter\bin`

### macOS / Linux
Adicione ao final do seu `~/.bashrc`, `~/.zshrc` ou `~/.bash_profile`:

```bash
export PATH="$PATH:$HOME/development/flutter/bin"
```

Depois, rode:

```bash
source ~/.bashrc  # ou .zshrc, dependendo do terminal
```

---

## ✅ 4. Verifique a instalação

Execute:

```bash
flutter doctor
```

Esse comando verifica se você tem os requisitos adicionais instalados e configura o ambiente.

---

## 🧩 5. Instale um Editor de Código

Recomenda-se o **Visual Studio Code** ou o **Android Studio**:

- [VS Code](https://code.visualstudio.com/)
- [Android Studio](https://developer.android.com/studio)

Instale as extensões do Flutter e Dart no editor escolhido.

---

## 📱 6. Configure um Emulador (opcional)

### Android Studio
1. Abra o Android Studio.
2. Vá em **More Actions > Virtual Device Manager**.
3. Clique em **Create Device**.
4. Selecione um modelo (Pixel, Nexus, etc).
5. Baixe uma imagem do sistema (API 30 ou superior).
6. Inicie o emulador.

---

## 🧪 7. Teste a Instalação

Crie um novo projeto de teste:

```bash
flutter create my_app
cd my_app
flutter run
```

---

## 🚀 Pronto!

Agora você está com o Flutter instalado e pronto para desenvolver seus aplicativos!

---
