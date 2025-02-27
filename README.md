# Django REST Framework API Documentation

This API is built using Django REST Framework (DRF) and provides functionality for user profiles, authentication, and profile feed items. Below is a detailed explanation of the available endpoints and how to use them.

---

## API Endpoints

### 1. **Hello ApiView**
- **URL:** `/api/hello-view/`
- **Methods:**
  - `GET`: Returns a welcome message and a list of features of the `APIView`.
  - `POST`: Accepts a `name` field and returns a personalized greeting.
  - `PUT`, `PATCH`, `DELETE`: Placeholder methods for updating and deleting objects.

**Example Request:**
```bash
GET /hello-view/  
```
**Response**:  
```json
  {"message": "Hello!",
  "an_apiview": [
    "Uses HTTP methods as function (POST, GET, PUT, PATCH, DELETE)",
    "Is similar to a traditional Django View"
  ]
}
```

### 2. **Hello ViewSet**
- **URL:** `/api/hello-viewset/`
- Methods:
  - `GET`: Returns a welcome message and a list of features of the `ViewSet`.
  - `POST`: Accepts `name` and `age` fields and returns a personalized greeting.
**Example Request:**
```bash
GET /hello-viewset/  
```
**Response**:
```json
{
  "message": "Hello!",
  "a_viewset": [
    "Uses action (List, Create, Update, etc.)",
    "Improve functionality with less coding"
  ]
}
```

### 3. **User Profiles**
- **URL:** `/api/profile/`
- **Methods**:
  - `GET`: Retrieves a list of all user profiles.
  - `POST`: Creates a new user profile.  
  - `PUT`, `PATCH`: Updates an existing user profile.
  - `DELETE`: Delete a user profile.  
- **Authentication**: Token Authentication is required for all operations.
- **Search Functionality**: You can search for profiles by `name` or `email` using the `search` query parameter.  
**Example Request:**
```bash
GET /api/profile/?search=John
```
**Response**:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
]
```
### 4. **User Login**
- **URL:** `/api/login/`
- Methods:
  - `POST`: Authenticates a user and returns a token for accessing protected endpoints.  
  
**Example Request:**
```bash
POST /api/login/
{
  "username": "john",
  "password": "password123"
}
```
**Response**:
```json
{
  "token": "abc123xyz456"
}
```

### 5. **Profile Feed Item**
- **URL:** `/api/feed/`
- **Methods**:
  - `GET`: Retrieves a list of all profile feed items.
  - `POST`: Creates a new profile feed item.
  - `PUT`, `PATCH`: Updates an existing profile feed item.
  - `DELETE`: Deletes a profile feed item.  
- **Authentication**: Token Authentication is required for all operations.
- **Permissions**: Only the owner of a feed item can update or delete it.

**Example Request:**
```bash
POST /api/feed/
{
  "status_text": "This is a new status update."
}
```
**Response**:
```json
{
  "id": 1,
  "user_profile": 1,
  "status_text": "This is a new status update.",
  "created_on": "2023-10-01T12:00:00Z"
}
```
---
## Vagrant Setup

This project includes a `Vagrantfile` to set up a virtualized development environment using Vagrant. Follow the steps below to get started.

### 1. **Install Vagrant**
Ensure Vagrant is installed on your machine. You can download it from the official website:
- [Vagrant Downloads](https://www.vagrantup.com/downloads)

### 2. **Install VirtualBox**
Vagrant requires a virtualization provider. VirtualBox is recommended and can be downloaded here:
- [VirtualBox Downloads](https://www.virtualbox.org/wiki/Downloads)

### 3. **Clone the Repository**
Clone the project repository to your local machine:
```bash
git clone https://github.com/sina83-max/profiles-rest-api.git
```

### 4. **Navigate to the Project Directory**
Change to the project directory where the `Vagrantfile` is located:
```bash
cd .
```

### 5. **Start the Vagrant Environment**
Run the following command to start the Vagrant virtual machine:
```bash
vagrant up
```
This will:
- Download the `bento/ubuntu-22.04` box (if not already downloaded).
- Configure the virtual machine with port forwarding (guest port `8000` to host port `8000`).
- Run provisioning scripts to set up the environment.

### 6. **SSH into the Vagrant Machine**
Once the virtual machine is up and running, SSH into it:
```bash
vagrant ssh
```

### 7. **Set Up the Project Inside the VM**
Inside the Vagrant VM, navigate to the shared project directory:
```bash
cd /vagrant
```

### 8. **Install Dependencies**
Install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```

### 9. **Run Migrations**
Apply database migrations to set up the necessary tables:
```bash
python manage.py migrate
```

### 10. **Start the Development Server**
Run the Django development server:
```bash
python manage.py runserver 0.0.0.0:8000
```

The API will be accessible on your host machine at:
```
http://localhost:8000/
```

### 11. **Stopping the Vagrant Machine**
To stop the Vagrant machine, run:
```bash
vagrant halt
```

To completely remove the Vagrant machine, run:
```bash
vagrant destroy
```

---

### **Vagrantfile Details**
The `Vagrantfile` provided in this project includes the following configurations:
- **Base Box:** `bento/ubuntu-22.04` (a lightweight Ubuntu 22.04 image).
- **Port Forwarding:** Maps guest port `8000` to host port `8000` for easy access to the API.
- **Provisioning Script:**
  - Disables automatic package updates to avoid conflicts during setup.
  - Installs essential packages (`python3-venv`, `zip`).
  - Sets up a Python alias in `.bash_aliases` to use `python3` by default.

### **Customizing the Vagrantfile**
You can modify the `Vagrantfile` to suit your needs. For example:
- Change the base box to a different OS.
- Add additional provisioning steps.
- Configure more port forwarding rules.

For more information, refer to the [Vagrant Documentation](https://www.vagrantup.com/docs).

---

## Troubleshooting
- **Port Conflict:** If port `8000` is already in use on your host machine, change the `forwarded_port` configuration in the `Vagrantfile`.
- **Provisioning Errors:** If provisioning fails, run `vagrant provision` to re-run the provisioning scripts.
- **Network Issues:** Ensure VirtualBox is properly installed and configured on your machine.


