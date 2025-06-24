#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from .crew import AkcitOpenvasAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'target_host': '192.168.1.1',  # IP ou host alvo para scan
        'scan_name': 'Security Assessment',  # Nome da tarefa de scan
        'port_range': 'Full and fast',  # Tipo de configuração de portas
        'task_name': 'Vulnerability_Scan_2025',  # Nome específico da tarefa
        'current_year': str(datetime.now().year)
    }
    
    try:
        AkcitOpenvasAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'target_host': '192.168.1.100',
        'scan_name': 'Training Security Assessment',
        'port_range': 'Full and fast',
        'task_name': 'Training_Vulnerability_Scan',
        'current_year': str(datetime.now().year)
    }
    try:
        AkcitOpenvasAgent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AkcitOpenvasAgent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'target_host': '10.0.0.1',
        'scan_name': 'Test Security Assessment',
        'port_range': 'Full and fast',
        'task_name': 'Test_Vulnerability_Scan',
        'current_year': str(datetime.now().year)
    }
    
    try:
        AkcitOpenvasAgent().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
