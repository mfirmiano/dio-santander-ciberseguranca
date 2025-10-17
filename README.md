# Testes de Penetração com Kali Linux e Metasploitable

Este repositório documenta os testes realizados em um ambiente controlado de **pentest**, utilizando **Kali Linux** como sistema atacante e **Metasploitable 2** como máquina alvo. Todos os experimentos foram feitos em laboratório virtual isolado, apenas para fins de estudo.

---

## 🎯 Objetivo
Explorar vulnerabilidades conhecidas em serviços da Metasploitable, praticando técnicas de **força bruta**, **password spraying** e **automação de login**, utilizando a ferramenta **Medusa** para ataques com *Wordlists*.

---

## 🧱 Ambiente de Testes

| Componente | Descrição |
|-------------|------------|
| Kali Linux | Sistema atacante, versão 2025.1 |
| Metasploitable 2 | Sistema alvo vulnerável |
| Ferramenta usada | Medusa (modular brute force tool) |
| Rede | Host-Only / Local Virtual Network |

---

## 🔧 Ferramentas Utilizadas

- **Medusa** — Ataques de força bruta a serviços (FTP, SMB, HTTP, etc.)  
- **DVWA (Damn Vulnerable Web Application)** — Testes automatizados em formulário web  
- **Wordlists** — Dicionários de senhas padrão usados para ataques (por exemplo: `/usr/share/wordlists/rockyou.txt`)  

---

## 🧠 Ataques Realizados

### 1. **FTP – Força Bruta**
Foi configurado o ataque de força bruta para encontrar credenciais válidas de login no serviço **FTP** da Metasploitable:

medusa -h 192.168.56.101 -u msfadmin -P /usr/share/wordlists/rockyou.txt -M ftp


**Descrição:**
- `-h`: IP do alvo  
- `-u`: usuário testado  
- `-P`: caminho da wordlist usada  
- `-M ftp`: módulo de ataque FTP  

O objetivo era testar a resistência de credenciais simples. Após várias tentativas, uma senha válida foi identificada, comprovando a vulnerabilidade do serviço.

---

### 2. **Automação de login – DVWA (Formulário Web)**
Simulação de múltiplas tentativas de login automatizadas no **DVWA**, usando o módulo HTTP do Medusa:

medusa -h 192.168.56.101 -u admin -P /usr/share/wordlists/rockyou.txt -M http -m FORM:/dvwa/login.php:username=^USER^&password=^PASS^:Login\ Failed


**Parâmetros principais:**
- `FORM`: especifica os campos de formulário e resposta de falha
- `^USER^` / `^PASS^`: variáveis substituídas durante o ataque
- `Login Failed`: texto retornado quando o login falha

---

### 3. **SMB – Password Spraying e Enumeração de Usuários**
Ataque com foco em **tentativas limitadas e distribuídas**, evitando bloqueios de conta.

Primeiro, foi feita **enumeração de usuários**:
enum4linux -U 192.168.56.101


Com a lista obtida, foi realizado o ataque **password spraying**:
medusa -h 192.168.56.101 -U usuarios.txt -p 123456 -M smbnt


**Descrição:**
- `-U`: arquivo contendo lista de usuários enumerados  
- `-p`: senha única aplicada em todos os usuários  
- `-M smbnt`: módulo SMB utilizado  

---

## 📊 Resultados e Conclusões

- O serviço **FTP** aceitava credenciais padrão, mostrando falha de segurança crítica.  
- O **DVWA** demonstrou vulnerabilidade a ataques automatizados, indicando necessidade de CAPTCHA ou políticas de bloqueio.  
- O serviço **SMB** respondeu positivamente a *password spraying*, reforçando a importância de senhas complexas e gerenciamento de tentativas.

---

## ⚠️ Aviso Legal

Este projeto é **exclusivamente educacional**.  
Todos os testes foram executados em **ambiente controlado e privado**.  
Jamais utilize estas técnicas em sistemas sem autorização expressa do proprietário.

---

## 📚 Créditos

- **Ferramenta:** Medusa – Modular Brute Forcer  
- **Alvo:** Metasploitable 2 by Rapid7  
- **Ambiente:** Kali Linux Offensive Security
- **DIO:** Santander Bootcamp Cibersegurança 2025
