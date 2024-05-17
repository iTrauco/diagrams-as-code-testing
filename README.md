# Graphviz Test Environment Setup Script

This bash script provides an interactive menu for setting up a sterile test environment for Graphviz, removing the current Graphviz environment, initializing sample Graphviz code for Google Cloud Platform (GCP), running the sample code to create a diagram, and more.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Script Directory:**
   ```bash
   cd graphviz-test-env-setup
   ```

3. **Run the Script:**
   ```bash
   ./graphviz_setup.sh
   ```

4. **Follow the On-Screen Menu:**
   - Choose the desired option by entering the corresponding number and pressing Enter.

## Functionality

- **Set up a Sterile Test Environment (Option 1):**
  - Installs Graphviz and any required dependencies to create a clean test environment.

- **Remove the Current Graphviz Environment (Option 2):**
  - Uninstalls Graphviz and cleans up any related files or directories.

- **Use a Preexisting Graphviz Installation (Option 3):**
  - Checks if Graphviz is already installed and provides information accordingly.

- **Initialize Sample Graphviz Code for GCP (Option 4):**
  - Creates a sample Python code to generate a diagram for Google Cloud Platform using Graphviz.

- **Run Sample Graphviz Code to Create Diagram (Option 5):**
  - Executes the sample Python code to create the GCP architecture diagram and opens the generated PNG file.

- **Exit (Option 6):**
  - Exits the script.

