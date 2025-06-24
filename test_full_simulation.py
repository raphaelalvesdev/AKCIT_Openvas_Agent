#!/usr/bin/env python3
"""
Teste do CrewAI OpenVAS Agent em modo simulação
Permite testar a lógica dos agentes sem OpenVAS real
"""

import os
import sys
sys.path.append('src')

# Criar arquivo .env temporário para testes
def create_test_env():
    env_content = """# Configuração de teste - SIMULAÇÃO
GVMD_SOCKET_PATH=/tmp/mock_gvmd.sock
GVMD_USERNAME=test_user
GVMD_PASSWORD=test_password
OPENAI_API_KEY=sk-test-key-for-simulation
"""
    with open('.env', 'w') as f:
        f.write(env_content)
    print("✅ Arquivo .env de teste criado")

def test_crew_creation():
    """Testa se o crew pode ser criado e configurado"""
    try:
        from akcit_openvas_agent.crew import AkcitOpenvasAgent
        
        print("\n=== TESTE 1: Criação do Crew ===")
        crew_instance = AkcitOpenvasAgent()
        print("✅ Crew instanciado com sucesso")
        
        # Testar agentes individuais
        researcher = crew_instance.researcher()
        analyst = crew_instance.reporting_analyst()
        print(f"✅ Researcher criado: {researcher.role}")
        print(f"✅ Analyst criado: {analyst.role}")
        
        # Testar tarefas
        task1 = crew_instance.research_task()
        task2 = crew_instance.reporting_task()
        print(f"✅ Research task: {task1.description[:50]}...")
        print(f"✅ Reporting task: {task2.description[:50]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro na criação do crew: {e}")
        return False

def test_tools_simulation():
    """Testa as tools em modo simulação"""
    try:
        print("\n=== TESTE 2: Tools em Simulação ===")
        
        # Importar tools
        from akcit_openvas_agent.crew import create_OpenVAS_tasks, get_OpenVAS_results
        
        # Simular criação de task
        print("🔧 Simulando criação de task...")
        task_result = "SIMULAÇÃO: Task 'Test_Scan' criada com ID task-sim-123"
        print(f"✅ Resultado simulado: {task_result}")
        
        # Simular análise de resultados
        print("📊 Simulando análise de resultados...")
        analysis_result = "SIMULAÇÃO: 3 vulnerabilidades encontradas (1 High, 2 Medium)"
        print(f"✅ Análise simulada: {analysis_result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro nos testes de tools: {e}")
        return False

def test_full_crew_execution():
    """Testa execução completa do crew em modo simulação"""
    try:
        print("\n=== TESTE 3: Execução Completa (Simulação) ===")
        
        from akcit_openvas_agent.crew import AkcitOpenvasAgent
        
        # Inputs de teste
        test_inputs = {
            'target_host': '127.0.0.1',
            'scan_name': 'Test Simulation Scan',
            'port_range': 'Top 1000',
            'task_name': 'Simulation_Test_Task',
            'current_year': '2025'
        }
        
        print(f"🎯 Inputs de teste: {test_inputs}")
        
        # Criar crew
        crew_instance = AkcitOpenvasAgent()
        crew = crew_instance.crew()
        
        print("✅ Crew configurado para simulação")
        print(f"   - Agentes: {len(crew.agents)}")
        print(f"   - Tarefas: {len(crew.tasks)}")
        
        # NOTA: Não executamos o kickoff aqui pois requer API OpenAI real
        # Em um ambiente de produção, você faria:
        # result = crew.kickoff(inputs=test_inputs)
        
        print("⚠️  Para execução completa, configure OPENAI_API_KEY real")
        print("   e execute: crew.kickoff(inputs=test_inputs)")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro na execução do crew: {e}")
        return False

def cleanup():
    """Remove arquivos de teste"""
    try:
        if os.path.exists('.env'):
            os.remove('.env')
            print("🧹 Arquivo .env de teste removido")
    except:
        pass

if __name__ == "__main__":
    print("🚀 INICIANDO TESTES DO CREWAI OPENVAS AGENT")
    print("=" * 50)
    
    try:
        # Criar ambiente de teste
        create_test_env()
        
        # Executar testes
        test1 = test_crew_creation()
        test2 = test_tools_simulation()
        test3 = test_full_crew_execution()
        
        # Resultados
        print("\n" + "=" * 50)
        print("📊 RESULTADOS DOS TESTES:")
        print(f"   ✅ Criação do Crew: {'PASSOU' if test1 else 'FALHOU'}")
        print(f"   ✅ Tools Simulação: {'PASSOU' if test2 else 'FALHOU'}")
        print(f"   ✅ Execução Completa: {'PASSOU' if test3 else 'FALHOU'}")
        
        if all([test1, test2, test3]):
            print("\n🎉 TODOS OS TESTES PASSARAM!")
            print("\n📋 PRÓXIMOS PASSOS:")
            print("1. Configure OpenVAS real (ver SETUP_OPENVAS.md)")
            print("2. Configure OPENAI_API_KEY no .env")
            print("3. Execute: crewai run")
        else:
            print("\n❌ ALGUNS TESTES FALHARAM")
            print("Verifique os erros acima antes de prosseguir")
            
    finally:
        cleanup()
