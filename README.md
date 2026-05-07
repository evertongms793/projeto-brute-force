# 🔐 Simulação de Malware com Python (Ransomware e Keylogger)

## 📌 Introdução

Este projeto tem como objetivo demonstrar, de forma educativa e em ambiente controlado, o funcionamento básico de malwares como Ransomware e Keylogger. A proposta é compreender como essas ameaças atuam e, principalmente, como podemos nos proteger delas.

---

## 🧠 O que é Ransomware?

Ransomware é um tipo de malware que bloqueia ou criptografa o acesso a sistemas, arquivos ou pastas, impedindo o uso normal pelo usuário. Após isso, o atacante exige o pagamento de um resgate para restaurar o acesso aos dados.

### 🔐 Funcionamento

O ransomware bloqueia os arquivos através de criptografia, tornando o acesso impossível sem a chave de descriptografia.

### ⚠️ Forma de infecção

O ransomware pode entrar no computador quando o usuário acessa links maliciosos, baixa arquivos infectados ou interage com conteúdos não confiáveis.

---

## 💻 Simulação de Ransomware

Neste projeto, foi criada uma simulação utilizando Python, onde um arquivo de texto tem seu conteúdo alterado (invertido), representando a criptografia dos dados.

### 📌 Etapas:

* Leitura do arquivo
* Modificação do conteúdo
* Escrita no arquivo (simulando bloqueio)
* Recuperação do conteúdo (simulando descriptografia)

---

## ⌨️ O que é Keylogger?

Keylogger é um tipo de malware que registra as teclas digitadas pelo usuário, geralmente sem que ele perceba.

### 🎯 Objetivo do ataque

Um atacante utiliza um keylogger para capturar informações sensíveis, como senhas, dados bancários e credenciais de acesso.

---

## 💻 Simulação de Keylogger

Foi desenvolvido um script em Python que captura dados digitados pelo usuário (via input) e armazena em um arquivo `.txt`.

### 📌 Funcionamento:

* Captura de entrada do usuário
* Armazenamento em arquivo (`log.txt`)
* Registro contínuo de dados

---

## 🛡️ Medidas de Proteção

Para se proteger de ransomware e keylogger, é importante:

* Utilizar senhas fortes
* Habilitar autenticação multifator (MFA)
* Evitar clicar em links suspeitos
* Não baixar arquivos de fontes desconhecidas
* Manter o sistema atualizado
* Utilizar antivírus e firewall
* Realizar backups frequentes

---

## 🎯 Conclusão

Com este projeto, foi possível compreender na prática como funcionam ataques de ransomware e keylogger, além de reforçar a importância da segurança digital. A simulação contribuiu para o aprendizado de conceitos fundamentais de cibersegurança e despertou maior interesse pela área.

---

## 🚀 Tecnologias Utilizadas

* Python

---

## ⚠️ Aviso

Este projeto tem finalidade exclusivamente educacional. Todas as simulações foram realizadas em ambiente controlado, sem qualquer intenção de uso malicioso.




## 💻 Códigos Utilizados

### 🔐 Simulação de Ransomware

```python
arquivo = "teste.txt"

# Criptografar
with open(arquivo, "r") as f:
    conteudo = f.read()

conteudo_crip = conteudo[::-1]

with open(arquivo, "w") as f:
    f.write(conteudo_crip)

print("Arquivo criptografado (simulação)")

# Descriptografar
with open(arquivo, "r") as f:
    conteudo = f.read()

conteudo_original = conteudo[::-1]

with open(arquivo, "w") as f:
    f.write(conteudo_original)

print("Arquivo recuperado!")
```

---

### ⌨️ Simulação de Keylogger

```python
texto = input("Digite algo: ")

with open("log.txt", "a") as arquivo:
    arquivo.write(texto + "\n")

print("Teclas registradas (simulação)")
```
