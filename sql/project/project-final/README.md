# Interactive Periodic Table Web Application

An interactive web application built with Flask that allows users to explore the periodic table of elements, view detailed information, manage element data (Create, Read, Update, Delete), and compare elements.

## Features

*   **Interactive Periodic Table Grid:** Displays elements on the homepage, color-coded by type.
*   **Element Details Modal:** Click an element on the grid to view its key details in a pop-up modal.
*   **Dedicated Element View Page:** A separate page for each element (`/element/view/<atomic_number>`) showing comprehensive information, including images and specific properties like electron shells and ionization energies.
*   **Search Functionality:** Real-time search by element name or symbol on the main periodic table page.
*   **Filter by Element Type:** Buttons to filter elements on the main page based on their classification (e.g., alkali metal, noble gas).
*   **CRUD Operations for Elements:**
    *   **Create:** Add new elements to the database via a dedicated form (`/element/new`) with input validation.
    *   **Read:** View element data through the main grid, detail modal, dedicated view page, and the "Manage Elements" page.
    *   **Update:** Edit information for existing elements using a pre-filled form (`/element/edit/<atomic_number>`).
    *   **Delete:** Remove elements from the database with a confirmation prompt, accessible from the element detail modal.
*   **Manage Elements Page:** A tabular view (`/elements`) of all elements, featuring:
    *   Client-side searching/filtering within the table.
    *   Sortable columns.
    *   Direct links to view, edit, or delete each element.
*   **Compare Elements Page:** A tool (`/compare`) to select up to three elements and view their properties side-by-side for easy comparison.
*   **Tooltips:** Hovering over an element in the main grid displays a tooltip with its atomic number, symbol, and name.
*   **Group/Period Highlighting:** Clicking an element on the main grid highlights other elements belonging to the same group and period.
*   **Data Population:** Element data is initially loaded from `PeriodicTableJSON.json` using a Python script (`populate_db.py`).
*   **Responsive Design:** User interface elements are designed to be functional across different screen sizes.

## Technologies Used

*   **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-WTF, Flask-Migrate
*   **Database:** SQLite
*   **Frontend:** HTML, CSS, JavaScript
*   **Data Source:** `PeriodicTableJSON.json` for initial element data.

## Project Structure

The project generally follows an MVC (Model-View-Controller) pattern.

```
project-final/
├── periodic_table_app/         # Main application directory
│   ├── app/                    # Core application package
│   │   ├── __init__.py         # Initializes Flask app, extensions
│   │   ├── models.py           # Database models (Element)
│   │   ├── routes.py           # Controller logic, API endpoints
│   │   ├── forms.py            # WTForms definitions
│   │   ├── static/             # CSS, JavaScript, images
│   │   │   └── css/style.css
│   │   └── templates/          # HTML templates
│   │       ├── layout.html
│   │       ├── index.html
│   │       ├── element_view.html
│   │       ├── create_element.html
│   │       ├── edit_element.html
│   │       ├── element_list.html
│   │       ├── compare_elements.html
│   │       └── macros.html
│   ├── migrations/             # Flask-Migrate database migration scripts
│   ├── run.py                  # Entry point to run the Flask application
│   ├── config.py               # Application configuration (DB URI, Secret Key)
│   ├── populate_db.py          # Script to populate the database
│   └── PeriodicTableJSON.json  # Raw element data
├── requirements.txt            # Python dependencies
├── .gitignore                  # Files to be ignored by Git
└── README.md                   # This file
```
*(Note: The virtual environment `.venv` is expected to be located one level above `project-final/`, e.g., in `sql/project/.venv`)*

## Prerequisites

*   Python (3.8+ recommended)
*   `pip` (Python package installer)
*   `git` (for cloning the repository)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd project-final
    ```

2.  **Set up and activate the virtual environment:**
    This project expects the virtual environment (`.venv`) to be located in the parent directory of `project-final` (e.g., `sql/project/.venv`).

    *   If you are in the `project-final` directory:
        ```bash
        # Create the .venv in the parent directory if it doesn't exist
        # python -m venv ../.venv # Uncomment and run if .venv is not present in parent

        # Activate the virtual environment (from project-final directory)
        source ../.venv/bin/activate  # On Linux/macOS
        # ..\.venv\Scripts\activate  # On Windows
        ```

3.  **Install dependencies:**
    (Ensure your virtual environment is active and you are in the `project-final` directory)
    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

All database commands should be run from the `periodic_table_app` directory, with the virtual environment active.

1.  **Navigate to the application directory:**
    ```bash
    cd periodic_table_app
    ```

2.  **Initialize Flask-Migrate (if setting up for the first time):**
    This step is only needed if the `migrations` folder does not already exist in `periodic_table_app/`.
    ```bash
    flask db init
    ```

3.  **Create database migrations:**
    If you've just run `flask db init` or made changes to `models.py`:
    ```bash
    flask db migrate -m "Initial database setup" 
    ```
    *(Use a descriptive message for subsequent migrations.)*

4.  **Apply migrations to the database:**
    This creates/updates the `app.db` SQLite file.
    ```bash
    flask db upgrade
    ```

## Populating the Database

The initial set of element data is loaded from `PeriodicTableJSON.json`.

1.  Ensure you are in the `project-final/periodic_table_app/` directory.
2.  Ensure your virtual environment is active.
3.  Run the population script:
    ```bash
    python populate_db.py
    ```
    This will populate the `element` table in your `app.db` database.

## Running the Application

1.  Ensure you are in the `project-final/periodic_table_app/` directory.
2.  Ensure your virtual environment (`../.venv` relative to `project-final`) is active.
    ```bash
    # If not already active and you are in periodic_table_app/
    # source ../../.venv/bin/activate # Linux/macOS
    # ..\..\.venv\Scripts\activate # Windows
    ```
3.  Start the Flask development server:
    ```bash
    python run.py
    ```
4.  Open your web browser and navigate to `http://127.0.0.1:5000/`.

## How to Use

*   **Homepage (`/` or `/index`):**
    *   **View Table:** The main periodic table is displayed. Elements are styled based on their type.
    *   **Hover for Tooltip:** Hover over any element to see a quick view of its atomic number, symbol, and name.
    *   **Click for Details:** Click an element to open a modal with more detailed information. This action also highlights other elements in the same group and period on the main grid.
    *   **Search:** Use the search bar at the top to filter elements by name or symbol in real-time.
    *   **Filter by Type:** Click the buttons below the search bar (e.g., "Alkali Metal", "Noble Gas") to filter the displayed elements by their type. Click "All Types" to reset.
    *   **Navigation:** Use the top navigation bar to go to "Manage Elements", "Compare Elements", or "Add New Element".

*   **Element Detail Modal (on Homepage):**
    *   Provides a snapshot of the element's properties.
    *   **"View Full Page" button:** Takes you to the dedicated page for that element with even more details.
    *   **"Edit Element" button:** Opens the form to modify the element's data.
    *   **"Delete Element" button:** Allows deletion of the element after a confirmation.

*   **Dedicated Element View Page (`/element/view/<atomic_number>`):**
    *   Accessed via the "View Full Page" button or from the "Manage Elements" page.
    *   Displays all available information for a single element, including images (if available), electron shell configurations, and ionization energies, presented in a structured format.

*   **Add New Element (`/element/new`):**
    *   Accessible via the "Add New Element" button in the navigation/layout.
    *   Provides a form to input all relevant details for a new chemical element. Fields include atomic number, symbol, name, phase, type, and various physical properties.
    *   Includes form validation to ensure data integrity (e.g., atomic number and symbol must be unique).

*   **Edit Element (`/element/edit/<atomic_number>`):**
    *   Accessible from the element detail modal or the "Manage Elements" page.
    *   The form is pre-populated with the selected element's current data, allowing for modifications.

*   **Manage Elements Page (`/elements`):**
    *   Lists all elements from the database in a sortable and filterable table.
    *   **Search Table:** Use the input field to filter the table by name or symbol.
    *   **Sort Columns:** Click on column headers (e.g., "Name", "Atomic Number") to sort the table.
    *   **Actions:** Each row provides links/buttons to "View" the full element page, "Edit" the element, or "Delete" the element.

*   **Compare Elements Page (`/compare`):**
    *   Allows selection of up to three different elements from dropdown lists.
    *   After submitting the selection, displays a side-by-side comparison of the chosen elements' properties in a grid format, making it easy to see differences and similarities.

## Screenshots

*(To be added: Please include screenshots of key application views, such as:*
*   *The main periodic table page with filters and search.*
*   *The element details modal.*
*   *The dedicated element view page.*
*   *The form for adding/editing an element.*
*   *The "Manage Elements" page with its table.*
*   *The "Compare Elements" page showing a comparison.)*

## Contributing

(Optional: If you wish to allow contributions, outline guidelines here, e.g., for reporting bugs or suggesting features.)

## License

(Optional: Specify a license for your project, e.g., MIT License.) 