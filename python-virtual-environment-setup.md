## Python virtual environment setup

1. To create a virtual environment inside the project

   ```sh
   $ python -m venv env
   ```

2. To activate the virtual environment

   ```sh
   $ env\scripts\activate
   ```

3. To check the list of package that has been installed

   ```sh
   $ pip list
   ```

4. To install any package in that environment

   ```sh
   $ pip install numpy
   ```

5. Create a requirement.txt

   ```sh
   $ pip freeze > requirement.txt
   ```

6. To deactivate a virtual environment

   ```sh
   $ deactivate
   ```
