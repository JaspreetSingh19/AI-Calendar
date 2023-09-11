# AI Calendar

**Project Description:** Use to create meetings with other users .

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Create meetings with others users easily.You can also check your upcoming
meetings in it. It also checks other user's meeting before creating a new meeting if user has available time slots or not.
## Getting Started

Start the project by following the installation steps.
For swagger response samples are also added.

* You will get a token in response of login api, you can use this token for authentication,by adding the value in Authorization like "Bearer {token}"
### Prerequisites

- Python (version 3.9)
- Django (version 4.2.5)
- Django Rest (version 3.14.0)

### Installation


```bash
# Clone the repository
git clone https://github.com/JaspreetSingh19/AI-Calendar.git

# Change directory to the project folder
cd AI-Calendar

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate
# For Pycharm
Add New Interpreter >

# Install project dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
