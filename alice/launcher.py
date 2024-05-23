import subprocess

# Lancer script1.py dans un processus séparé
process1 = subprocess.Popen(['python3', 'packet_tracker.py'])

# Lancer script2.py dans un autre processus séparé
process2 = subprocess.Popen(['python3', 'icmp_extractor.py'])

# Attendre que les deux processus se terminent
process1.wait()
process2.wait()

print("Les deux scripts se sont terminés.")
