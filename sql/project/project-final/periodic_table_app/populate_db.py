import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Element

def populate_elements():
    """Populates the database with periodic table elements from JSON."""
    app = create_app()
    with app.app_context():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(current_dir, 'data', 'PeriodicTableJSON.json')

        try:
            with open(json_file_path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"Error: JSON file not found at {json_file_path}")
            return
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {json_file_path}")
            return

        elements_data = data.get('elements', [])

        if not elements_data:
            print("No elements found in the JSON file.")
            return

        for el_data in elements_data:
            atomic_number = el_data.get('number')
            if atomic_number is None:
                print(f"Skipping element due to missing atomic number: {el_data.get('name')}")
                continue

            existing_element = Element.query.filter_by(atomic_number=atomic_number).first()
            
            element_fields = {
                'atomic_number': atomic_number,
                'symbol': el_data.get('symbol'),
                'name': el_data.get('name'),
                'atomic_mass': el_data.get('atomic_mass'),
                'group': el_data.get('group'),
                'period': el_data.get('period'),
                'element_type': el_data.get('category'),
                'description': el_data.get('summary'),
                'appearance': el_data.get('appearance'),
                'boil': el_data.get('boil'),
                'density': el_data.get('density'),
                'discovered_by': el_data.get('discovered_by'),
                'melt': el_data.get('melt'),
                'molar_heat': el_data.get('molar_heat'),
                'named_by': el_data.get('named_by'),
                'phase': el_data.get('phase'),
                'source': el_data.get('source'),
                'bohr_model_image': el_data.get('bohr_model_image'),
                'bohr_model_3d': el_data.get('bohr_model_3d'),
                'spectral_img': el_data.get('spectral_img'),
                'xpos': el_data.get('xpos'),
                'ypos': el_data.get('ypos'),
                'shells': json.dumps(el_data.get('shells')) if el_data.get('shells') is not None else None,
                'electron_configuration': el_data.get('electron_configuration'),
                'electron_configuration_semantic': el_data.get('electron_configuration_semantic'),
                'electron_affinity': el_data.get('electron_affinity'),
                'electronegativity_pauling': el_data.get('electronegativity_pauling'),
                'ionization_energies': json.dumps(el_data.get('ionization_energies')) if el_data.get('ionization_energies') is not None else None,
                'cpk_hex': el_data.get('cpk-hex'),
                'image_title': el_data.get('image', {}).get('title'),
                'image_url': el_data.get('image', {}).get('url'),
                'image_attribution': el_data.get('image', {}).get('attribution'),
                'block': el_data.get('block')
            }

            
            required_fields_check = {
                k: v for k, v in element_fields.items() 
                if k in ['symbol', 'name', 'atomic_mass'] and v is None
            }
            if required_fields_check:
                print(f"Skipping element {el_data.get('name', 'Unknown')} due to missing required fields: {list(required_fields_check.keys())}")
                continue


            if existing_element:
                for key, value in element_fields.items():
                    setattr(existing_element, key, value)
                print(f"Updated {existing_element.name}")
            else:
                element = Element(**element_fields)
                db.session.add(element)
                print(f"Added {element.name}")
        
        try:
            db.session.commit()
            print("Database population/update complete.")
        except Exception as e:
            db.session.rollback()
            print(f"Error committing to database: {e}")

if __name__ == '__main__':
    populate_elements() 