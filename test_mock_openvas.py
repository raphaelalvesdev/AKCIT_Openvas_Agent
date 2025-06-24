#!/usr/bin/env python3
"""
Mock/Simulação do OpenVAS para testes de desenvolvimento
Esta versão simula as respostas do OpenVAS sem precisar da instalação real
"""

class MockGVMWorkflow:
    def run(self):
        return """
🔧 SIMULAÇÃO - OpenVAS Task Creation
====================================

✅ Task criada com sucesso!

📋 Detalhes da Task:
- Task ID: task-12345-67890-abcdef
- Nome: Security_Assessment_Mock
- Target: 192.168.1.1
- Configuração: Full and fast
- Status: Iniciada

⏱️ Progresso:
- Task iniciada às 10:30:25
- Tempo estimado: 15-30 minutos
- Status atual: Scanning ports...

📊 Monitoramento:
Para verificar o progresso, execute:
- Interface Web: https://localhost:9392
- CLI: gvm-cli socket --xml '<get_tasks task_id="task-12345"/>'

⚠️ NOTA: Esta é uma simulação para desenvolvimento.
"""

class MockResultManager:
    def result(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<get_results_response status="200" status_text="OK">
  <result id="result-001">
    <name>OpenSSL CVE-2022-0778</name>
    <host>192.168.1.1</host>
    <port>443/tcp</port>
    <nvt oid="1.3.6.1.4.1.25623.1.0.147789">
      <name>OpenSSL Infinite Loop DoS Vulnerability</name>
      <cvss_base>7.5</cvss_base>
      <family>SSL and TLS</family>
    </nvt>
    <description>The remote host is running a version of OpenSSL that is affected by a denial of service vulnerability.</description>
    <threat>High</threat>
  </result>
  <result id="result-002">
    <name>HTTP Information Disclosure</name>
    <host>192.168.1.1</host>
    <port>80/tcp</port>
    <nvt oid="1.3.6.1.4.1.25623.1.0.111111">
      <name>HTTP Server Information Disclosure</name>
      <cvss_base>4.3</cvss_base>
      <family>Web Servers</family>
    </nvt>
    <description>The remote web server reveals sensitive information in HTTP headers.</description>
    <threat>Medium</threat>
  </result>
</get_results_response>"""

# Substituir temporariamente as classes originais
if __name__ == "__main__":
    print("=== TESTE COM MOCK OPENVAS ===")
    
    # Testar workflow
    mock_workflow = MockGVMWorkflow()
    result1 = mock_workflow.run()
    print("1. Mock Workflow Result:")
    print(result1)
    
    # Testar result manager
    mock_results = MockResultManager()
    result2 = mock_results.result()
    print("\n2. Mock Results:")
    print(result2[:500] + "...")
    
    print("\n✅ Mock funcionando! Pronto para testes de desenvolvimento.")
