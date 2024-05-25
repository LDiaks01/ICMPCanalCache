
To test the project in UDP mode with AES encryption, follow these steps:

1. Build the Netlab architecture.
2. Launch on h1:
    ```bash
    ./creation_interface.sh 1 # Get the IP address 10.87.87.1
    ./alice/config.sh # Configure iptables rules
    ```
3. Launch on h2:
    ```bash
    ./creation_interface.sh 2 # Get the IP address 10.87.87.2
    ./bob/config.sh # Configure iptables rules
    ```
4. Once the above steps are completed, we are ready to start the tunnel.
    - On h1, navigate to the `alice` directory and execute the script:
      ```bash
      sudo python3 launcher.py
      ```
    - On h3, navigate to the `bob` directory and execute the script:
      ```bash
      sudo python3 launcher.py
      ```
    These two Python scripts set up the Scapy interceptors and builders.
5. Finally, on h1, run the following command:
    ```bash
    socat - UDP4:10.87.87.2:6789,bind=10.87.87.1:6789
    ```
    And on h3, run the following command:
    ```bash
    socat - UDP4:10.87.87.1:6789,bind=10.87.87.2:6789
    ```

Enjoy the covert channel!

---------------------------------------------------------------------------------------------------------------


Pour tester le projet en mode UDP avec le chiffrement AES, suivez ces étapes :

1. Construisez l'architecture Netlab.
2. Lancez sur h1 :
        ```bash
        ./creation_interface.sh 1 # Obtenez l'adresse IP 10.87.87.1
        ./alice/config.sh # Configurez les règles iptables
        ```
3. Lancez sur h2 :
        ```bash
        ./creation_interface.sh 2 # Obtenez l'adresse IP 10.87.87.2
        ./bob/config.sh # Configurez les règles iptables
        ```
4. Une fois les étapes ci-dessus terminées, nous sommes prêts à démarrer le tunnel.
        - Sur h1, naviguez vers le répertoire `alice` et exécutez le script :
            ```bash
            sudo python3 launcher.py
            ```
        - Sur h3, naviguez vers le répertoire `bob` et exécutez le script :
            ```bash
            sudo python3 launcher.py
            ```
        Ces deux scripts Python mettent en place les intercepteurs et les constructeurs Scapy.
5. Enfin, sur h1, exécutez la commande suivante :
        ```bash
        socat - UDP4:10.87.87.2:6789,bind=10.87.87.1:6789
        ```
        Et sur h3, exécutez la commande suivante :
        ```bash
        socat - UDP4:10.87.87.1:6789,bind=10.87.87.2:6789
        ```

Profitez du canal caché !