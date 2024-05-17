#!/bin/bash

set_up_env() {
    echo "Setting up a sterile test environment for Graphviz..."
    # Install Graphviz and any required dependencies
    sudo apt update
    sudo apt install -y graphviz
    echo "Sterile test environment set up."
}

create_sample_code() {
    cat <<EOF > gcp_sample.py
from graphviz import Digraph

# Create a new Digraph
dot = Digraph()

# Add nodes
dot.node('A', 'Google Cloud Platform')
dot.node('B', 'Compute Engine')
dot.node('C', 'Cloud Storage')

# Add edges
dot.edges(['AB', 'AC'])

# Render the graph
dot.render('gcp_architecture', format='png', cleanup=True)
EOF
    echo "Sample code for Google Cloud Platform created."
}

remove_env() {
    echo "Removing the current Graphviz environment..."
    # Uninstall Graphviz and clean up any related files or directories
    sudo apt remove -y graphviz
    echo "Current Graphviz environment removed."
}

use_previous() {
    echo "Using a preexisting Graphviz installation..."
    # Check if Graphviz is installed
    if command -v dot &>/dev/null; then
        echo "Graphviz is already installed."
    else
        echo "Graphviz is not installed."
    fi
}

initialize_sample() {
    if [[ -f "gcp_sample.py" ]]; then
        echo "Sample code for Google Cloud Platform already exists."
    else
        create_sample_code
    fi
}

run_sample() {
    if [[ -f "gcp_sample.py" ]]; then
        echo "Running sample code..."
        python3 gcp_sample.py
        if [[ -f "gcp_architecture.png" ]]; then
            xdg-open gcp_architecture.png
        else
            echo "Failed to find the generated PNG file."
        fi
    else
        echo "Sample code for Google Cloud Platform does not exist. Please initialize it first."
    fi
}

while true; do
    echo "Select an option:"
    echo "1. Set up a sterile test environment"
    echo "2. Remove the current Graphviz environment"
    echo "3. Use a preexisting Graphviz installation"
    echo "4. Initialize sample Graphviz code for GCP"
    echo "5. Run sample Graphviz code to create diagram"
    echo "6. Exit"
    read -p "Enter option: " option

    case $option in
        1) set_up_env ;;
        2) remove_env ;;
        3) use_previous ;;
        4) initialize_sample ;;
        5) run_sample ;;
        6) echo "Exiting..."; break ;;
        *) echo "Invalid option." ;;
    esac
done

