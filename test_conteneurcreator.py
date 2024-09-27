import pytest
import subprocess
from conteneurcreator import is_docker_installed

# Test to verify detection of Linux system
def test_system_detection_linux(monkeypatch):
    monkeypatch.setattr('platform.system', lambda: "Linux")
    from platform import system
    assert system() == "Linux"

# Test to verify detection of Windows system
def test_system_detection_windows(monkeypatch):
    monkeypatch.setattr('platform.system', lambda: "Windows")
    from platform import system
    assert system() == "Windows"

# Test to verify detection of an unknown OS
def test_system_detection_unknown(monkeypatch):
    monkeypatch.setattr('platform.system', lambda: "UnknownOS")
    from platform import system
    assert system() == "UnknownOS"

# Test to verify that Docker is installed
def test_is_docker_installed(monkeypatch):
    # Mock the subprocess.run method to simulate successful Docker installation
    def mock_run(*args, **kwargs):
        return subprocess.CompletedProcess(args, returncode=0)  # Simulating success
    monkeypatch.setattr(subprocess, 'run', mock_run)
    
    # Call the function and assert the expected outcome
    assert is_docker_installed() is True

# Test to verify that Docker is not installed
def test_is_docker_not_installed(monkeypatch):
    # Mock the subprocess.run method to simulate Docker not being found
    def mock_run_fail(*args, **kwargs):
        raise FileNotFoundError("Docker command not found")
    
    monkeypatch.setattr(subprocess, 'run', mock_run_fail)
    
    # Call the function and assert the expected outcome
    assert is_docker_installed() is False
